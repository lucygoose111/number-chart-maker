import os
from data_create_tools.calc import Calculator
from data_create_tools.rng import get_random_num;

number = None
t_table_type = None
num_chart_type = None
num_visible = False

input_file_name = input('Choose file name ')

chart_type = input('Choose chart type: ')

# If chart is a times table
if chart_type == 't_table':	

	input_choose_numdata_t_table = input("Random limit or choose limit: ")
 
	if input_choose_numdata_t_table == "choose":
		input_choice_num = input('What number: ')
		number = int(input_choice_num)

	elif input_choose_numdata_t_table == 'random':
		rn = get_random_num(1, 100)
		number = rn

	t_table_type = input_choose_numdata_t_table


# If chart is a counting chart
elif chart_type == 'num_chart':
	input_choose_numdata_num_chart= input("Random limit or choose limit: ")

	if input_choose_numdata_num_chart == "choose":
		input_choice_num = input('What number: ')
		number = int(input_choice_num)

	elif input_choose_numdata_num_chart == 'random':
		rn = get_random_num(1, 20000)
		number = rn

	input_num_visible = input('y/n Will the numbers be visible? ')

	if input_num_visible == 'y':
		num_visible = True

	elif input_num_visible == 'n':
		num_visible = False

	num_chart_type = input_choose_numdata_num_chart

if number == None:
	exit()
# To create the JSON file the JavaScript will read
with open(input_file_name+'.json', 'w') as main_data:
	main_data.write('{')
	main_data.write(f'"chartType": "{chart_type}",')
	main_data.write(f'"number":{number},')
	main_data.write(f'"inputChooseNumDataTTable": "{t_table_type}",')
	main_data.write(f'"inputChooseNumDataNumChart": "{num_chart_type}",')
	if num_visible == True:
		main_data.write(f'"numVisible": true')
	elif num_visible == False:
		main_data.write(f'"numVisible": false')
	main_data.write('}')