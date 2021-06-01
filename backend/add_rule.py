from fuzzy_logic.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_logic.fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_logic.fuzzy_variable import FuzzyVariable
from fuzzy_logic.inference_engine import FuzzySystem
import warnings
warnings.filterwarnings("ignore")

conf = FuzzyInputVariable('Confidentiality', 0, 100, 100)
conf.add_trapezoidal('High', 55,65,100,100)
conf.add_trapezoidal('Medium', 25, 35, 55,65)
conf.add_trapezoidal('Low', 0, 0, 25,35)

integrity = FuzzyInputVariable('Integrity', 0, 100, 100)
integrity.add_trapezoidal('High', 55,65,100,100)
integrity.add_trapezoidal('Medium', 25, 35, 55,65)
integrity.add_trapezoidal('Low', 0, 0, 25,35)

availability = FuzzyInputVariable('Availability', 0, 100, 100)
availability.add_trapezoidal('High', 55,65,100,100)
availability.add_trapezoidal('Medium', 25, 35, 55,65)
availability.add_trapezoidal('Low', 0, 0, 25,35)

sensitivity = FuzzyOutputVariable('Sensitivity', 0, 100, 100)
sensitivity.add_triangular('High', 66, 83, 100)
sensitivity.add_triangular('Medium', 33, 49.5, 66)
sensitivity.add_triangular('Low', 0, 16.5, 33)

system = FuzzySystem()
system.add_input_variable(conf)
system.add_input_variable(integrity)
system.add_input_variable(availability)
system.add_output_variable(sensitivity)

# Rule 1
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Medium',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 2
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'High',
		'Availability':'Medium'},
		{'Sensitivity':'High'})

# Rule 3
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Medium',
		'Availability':'Medium'},
		{'Sensitivity':'Medium'})

# Rule 4
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Low',
		'Availability':'Low'},
		{'Sensitivity':'Low'})
#
output = system.evaluate_output({
				'Confidentiality':100,
				'Integrity':100,
				'Availability':50
		})

print(output)
# print('fuzzification\n-------------\n', info['fuzzification'])
# print('rules\n-----\n', info['rules'])

system.plot_system()