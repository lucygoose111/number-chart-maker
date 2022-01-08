class Calculator:

	def __init__(self):
		self.operators = ['+', '-', '*', '/']

	def add(num1, num2):
		result = num1 + num2
		return result

	def subtract(num1, num2):
		result = num1 - num2
		return result

	def multiply(num1, num2):
		result = num1 * num2
		return result

	def divide(num1, num2):
		result = num1 / num2
		return result

	def exponent(num, exponent):
		result = num**exponent
		return result
