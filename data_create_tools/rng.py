import random

random_num = random.randint(1, 3000)

with open('randomNumber.txt', 'w') as rng_num:
	rng_num.write(str(random_num))
