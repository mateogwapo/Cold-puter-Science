Temperature = 3
numbers = [5, -10, 15]

def FinalResult():
	ans=0
	for number in numbers:
		if int(number) < 0:
			ans +=1
		print (ans)
FinalResult()