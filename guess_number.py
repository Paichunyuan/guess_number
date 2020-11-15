import random

r = random.randint(1, 100)

while True:
	guess = input("請填入您要猜的數字: ")
	guess = int(guess)
	if guess == r:
		print("你猜對了!")
		break
	elif guess < r:
		print("比答案小")
	else:
		print("比答案大")