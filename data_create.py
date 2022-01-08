import subprocess
import os
from data_create_tools.calc import Calculator

number = None
t_table_type = None
num_chart_type = None

chart_type = input('Choose chart type: ')


if chart_type == 't_table':	

	input_choose_numdata_t_table = input("Random limit or choose limit: ")

	if input_choose_numdata_t_table == "choice":
		input_choice_num = input('What number: ')
		number = int(input_choice_num)

	elif input_choose_numdata_t_table == 'random':
		subprocess.run('py data_create_tools/rng.py')
		with open('data_create_tools/randomNumber.txt') as rng_num:
			for rn in rng_num:
				number = int(rn)

	t_table_type = input_choose_numdata_t_table


elif chart_type == 'num_chart':
	input_choose_numdata_num_chart= input("Random limit or choose limit: ")

	if input_choose_numdata_num_chart == "choice":
		input_choice_num = input('What number: ')
		number = int(input_choice_num)

	elif input_choose_numdata_num_chart == 'random':
		subprocess.run('py data_create_tools/rng.py')
		with open('data_create_tools/randomNumber.txt') as rng_num:
			for rn in rng_num:
				number = int(rn)

	num_chart_type = input_choose_numdata_num_chart
	os.system('delete_created_rng.bat')

with open('mainData.json', 'w') as main_data:
	main_data.write('{')
	main_data.write(f'"chartType": {chart_type}')
	main_data.write(f'"number":{number}')
	main_data.write(f'"inputChooseNumDataTTable": {t_table_type}')
	main_data.write(f'"inputChooseNumDataNumChart: {num_chart_type}"')
	main_data.write(f'"numberSquareCount": {Calculator.multiply(number, number)}')
	main_data.write('}')