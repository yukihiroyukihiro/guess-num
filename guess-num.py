import random

ans = random.randint(1, 100)
while True:
	x = int(input('請猜一個1~100的整數：'))
	if x == ans:
		print('猜對了！程式即將結束！')
		break
	elif x > ans:
		print('比答案大！')
	elif x < ans:
		print('比答案小！')
