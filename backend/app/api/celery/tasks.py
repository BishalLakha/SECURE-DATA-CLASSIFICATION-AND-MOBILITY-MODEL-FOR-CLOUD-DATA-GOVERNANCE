from time import sleep
import traceback
from celery import states
from celery.exceptions import Ignore
from encrypt import AESCipher,ECCAESCipher
from worker import celery
import pandas as pd
import requests
import time
import sys

aes = AESCipher("1234")
ecc = ECCAESCipher(1234)

aes_time = 0
ecc_time = 0


# @celery.task(name='hello.task', bind=True)
# def hello_world(self, name):
#     try:
#         if name == 'error':
#             k = 1 / 0
#         for i in range(60):
#             sleep(1)
#             self.update_state(state='PROGRESS', meta={'done': i, 'total': 60})
#         return {"result": "hello {}".format(str(name))}
#     except Exception as ex:
#         self.update_state(
#             state=states.FAILURE,
#             meta={
#                 'exc_type': type(ex).__name__,
#                 'exc_message': traceback.format_exc().split('\n')
#             })
#         raise ex


@celery.task(name='save_in_db.task', bind=True)
def save_in_db(self, df, sensitivity,filename):
    global aes_time
    global ecc_time

    try:
        df = pd.DataFrame.from_dict(df)
        original_df_size = sys.getsizeof(df)

        for column in df.columns.tolist():
            sens = sensitivity.get(column, None)

            self.update_state(state='PROGRESS',
                              meta={'processing_feature': column, 'total': len(df.columns.tolist()), 'aes_time': aes_time,
                                    'ecc_time': ecc_time})

            if sens is not None:
                if (sens <= 66) and (sens > 33):
                    now = time.time()
                    df[column] = df[column].apply(lambda x: aes.encrypt(x))
                    aes_time = time.time() - now
                elif sens > 66:
                    now = time.time()
                    df[column] = df[column].apply(lambda x: ecc.encrypt_ECC(x.encode('utf-8').strip(),self,column))
                    # df[column] = df[column].apply(lambda x: aes.encrypt(x))
                    ecc_time = time.time() - now

        encrypted_df_size = sys.getsizeof(df)

        now = time.time()
        for index, row in df.iterrows():
            r = requests.post('http://backend:8000/api/v1/fuzzy/classify/save-user-data/', json=row.to_dict())
            self.update_state(state='PROGRESS', meta={'done': index, 'total': len(df)})

        db_save_time = time.time() - now

        return {"message": "Saved data contained in {}".format(str(filename)),'aes_time': aes_time,"ecc_time":ecc_time,
                "db_save_time":db_save_time,"original_df_size":original_df_size,"encrypted_df_size":encrypted_df_size}

    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n')
            })
        raise ex