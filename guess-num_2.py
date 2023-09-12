import random
start = int(input('請決定隨機數字範圍開始值：'))
end = int(input('請決定隨機數字範圍結束值：'))

start_2 = str(start)
end_2 = str(end)

ans = random.randint(start, end)
count = 0
while True:
	count = count + 1
	x = int(input('請猜一個' + start_2 + '~' + end_2 + '的數字：'))
	if x == ans:
		print('猜對了！程式即將結束！')
		print('這是你猜的第', count,'次' )
		break
	elif x > ans:
		print('比答案大！')
	elif x < ans:
		print('比答案小！')
	print('這是你猜的第', count,'次' )
