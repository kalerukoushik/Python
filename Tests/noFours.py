import random
def calculateWithoutFours():
	total = int(input("Enter Amount: "))
	strTotal = str(total)
	if(total < 4):
		calculateWithoutFours()
	elif(('4' not in strTotal)):
		print("You can present the amount ", total)
	else:
		print('You can present the check as : ')
		for i in range(1, total+1):
			num1 = random.randint(1, total)
			num2 = total-num1
			number1=str(num1)
			number2=str(num2)
			if(('4' in number1) or ('4' in number2)):
				return
			else:
				print(num1, num2)
				print()

calculateWithoutFours()