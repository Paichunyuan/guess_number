import random

r = random.randint(1, 100)

count = 0

while True:
	count = count + 1
	guess = input("請填入您要猜的數字: ")
	guess = int(guess)
	if guess == r:
		print("你猜對了!")
		print('這是你猜的第', count, '次')
		break
	elif guess < r:
		print("比答案小")
	else:
		print("比答案大")
	print('這是你猜的第', count, '次')