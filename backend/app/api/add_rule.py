from .fuzzy_logic.fuzzy_variable_output import FuzzyOutputVariable
from .fuzzy_logic.fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_logic.fuzzy_variable import FuzzyVariable
from .fuzzy_logic.inference_engine import FuzzySystem

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
		{'Confidentiality':'High',
			'Integrity':'High',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 2
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'Medium',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 3
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'Low',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 4
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'Medium',
		'Availability':'Medium'},
		{'Sensitivity':'High'})

# Rule 5
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'Medium',
		'Availability':'Low'},
		{'Sensitivity':'High'})

# Rule 6
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'Low',
		'Availability':'Medium'},
		{'Sensitivity':'High'})

# Rule 7
system.add_rule(
		{'Confidentiality':'High',
			'Integrity':'Low',
		'Availability':'Low'},
		{'Sensitivity':'High'})


# Rule 8
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'High',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 9
system.add_rule(
		{'Confidentiality':'Medium',
			'Integrity':'High',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 10
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Medium',
		'Availability':'High'},
		{'Sensitivity':'High'})

# Rule 11
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Low',
		'Availability':'High'},
		{'Sensitivity':'High'})


# Rule 12
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'High',
		'Availability':'Medium'},
		{'Sensitivity':'High'})


# Rule 13
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'High',
		'Availability':'Low'},
		{'Sensitivity':'High'})

# Rule 14
system.add_rule(
		{'Confidentiality':'Medium',
			'Integrity':'Medium',
		'Availability':'Low'},
		{'Sensitivity':'Medium'})

# Rule 15
system.add_rule(
		{'Confidentiality':'Medium',
			'Integrity':'Medium',
		'Availability':'Medium'},
		{'Sensitivity':'Medium'})

# Rule 16
system.add_rule(
		{'Confidentiality':'Medium',
			'Integrity':'Medium',
		'Availability':'Low'},
		{'Sensitivity':'Medium'})


# Rule 17
system.add_rule(
		{'Confidentiality':'Medium',
			'Integrity':'Low',
		'Availability':'Low'},
		{'Sensitivity':'Low'})

# Rule 18
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Medium',
		'Availability':'Medium'},
		{'Sensitivity':'Medium'})


# Rule 19
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Low',
		'Availability':'Medium'},
		{'Sensitivity':'Low'})

# Rule 20
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Low',
		'Availability':'Low'},
		{'Sensitivity':'Low'})


# Rule 21
system.add_rule(
		{'Confidentiality':'Low',
			'Integrity':'Medium',
		'Availability':'Low'},
		{'Sensitivity':'Low'})


# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Medium',
# 		'Availability':'High'},
# 		{'Sensitivity':'High'})
#
# # Rule 2
# system.add_rule(
# 		{'Confidentiality':'High',
# 			'Integrity':'High',
# 		'Availability':'Medium'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 3
# system.add_rule(
# 		{'Confidentiality':'High',
# 			'Integrity':'High',
# 		'Availability':'High'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 4
# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Low',
# 		'Availability':'High'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 5
# system.add_rule(
# 		{'Confidentiality':'Medium',
# 			'Integrity':'Low',
# 		'Availability':'High'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 6
# system.add_rule(
# 		{'Confidentiality':'Medium',
# 			'Integrity':'Medium',
# 		'Availability':'High'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 7
# system.add_rule(
# 		{'Confidentiality':'Medium',
# 			'Integrity':'High',
# 		'Availability':'Medium'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 4
# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Low',
# 		'Availability':'High'},
# 		{'Sensitivity':'High'})
#
#
# # Rule 3
# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Medium',
# 		'Availability':'Medium'},
# 		{'Sensitivity':'Medium'})
#
# # Rule 4
# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Low',
# 		'Availability':'Low'},
# 		{'Sensitivity':'Low'})
#
#
# # Rule 6
# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Medium',
# 		'Availability':'Low'},
# 		{'Sensitivity':'Low'})
#
# # Rule 7
# system.add_rule(
# 		{'Confidentiality':'Low',
# 			'Integrity':'Low',
# 		'Availability':'Medium'},
# 		{'Sensitivity':'Low'})
#
# # Rule 8
# system.add_rule(
# 		{'Confidentiality':'Medium',
# 			'Integrity':'Medium',
# 		'Availability':'Medium'},
# 		{'Sensitivity':'Medium'})
#
#
#
#
# # system.add_rule(
# # 		{'Confidentiality':'High',
# # 			'Integrity':'High',
# # 		'Availability':'High'},
# # 		{'Sensitivity':'Medium'})
# #
#
# # print('fuzzification\n-------------\n', info['fuzzification'])
# # print('rules\n-----\n', info['rules'])
#

if __name__ == "__main__":
	features = {'Confidentiality':95,
			'Integrity':95,
			'Availability':95}

	output = system.evaluate_output(features)
	print(output)
	# system.plot_system()


