i=0
while i<50:
	if i%3==0 and i%5!=0:
		print("Fizz")
	elif i%5==0 and i%3!=0:
		print("Buzz")
	elif i%3==0 or i%5==0:
		print("FizzBuzz")
	else:
		print(i)
	i=i+1
	
