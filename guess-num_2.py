import random

ans = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	x = int(input('請猜一個1~100的整數：'))
	if x == ans:
		print('猜對了！程式即將結束！')
		print('這是你猜的第', count,'次' )
		break
	elif x > ans:
		print('比答案大！')
	elif x < ans:
		print('比答案小！')
	print('這是你猜的第', count,'次' )
