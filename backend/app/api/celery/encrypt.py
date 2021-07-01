import hashlib
from Crypto import Random
from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii

from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]


class ECCAESCipher:
    def __init__(self,key):
        self.privKey = key
        self.curve = registry.get_curve('brainpoolP256r1')
        self.pubKey = self.privKey * self.curve.g

    def _encrypt_AES_GCM(self,msg, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        return (ciphertext, aesCipher.nonce, authTag)

    def _decrypt_AES_GCM(self,ciphertext, nonce, authTag, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext

    def _ecc_point_to_256_bit_key(self,point):
        sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
        sha.update(int.to_bytes(point.y, 32, 'big'))
        return sha.digest()

    def encrypt_ECC(self,msg,celery_update,feature):
        ciphertextPrivKey = secrets.randbelow(self.curve.field.n)
        sharedECCKey = ciphertextPrivKey * self.pubKey
        secretKey = self._ecc_point_to_256_bit_key(sharedECCKey)
        ciphertext, nonce, authTag = self._encrypt_AES_GCM(msg, secretKey)
        ciphertextPubKey = ciphertextPrivKey * self.curve.g
        # return (ciphertext, nonce, authTag, ciphertextPubKey)
        celery_update.update_state(state='PROGRESS', meta={'Process': "ECC Encryption", "Feature":feature})

        return binascii.hexlify(ciphertext).decode()

    def decrypt_ECC(self,encryptedMsg):
        (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
        sharedECCKey = self.privKey * ciphertextPubKey
        secretKey = self._ecc_point_to_256_bit_key(sharedECCKey)
        plaintext = self._decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
        return plaintext


if __name__ == "__main__":
    a = AESCipher("Balla")
    enc = a.encrypt("Apple")
    print(enc)
    print(a.decrypt(enc))

    b = ECCAESCipher(123)

    print(b'app'.decode())

