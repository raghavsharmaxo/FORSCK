age=int(input("ENTER YOUR AGE:"))

if(age==0 or age<=1):
	print("INFANT")
	
elif(age==1 or age<=18):
	print("CHILD")
	
elif(age==18 or age<=60):
	print("ADULT")
	
elif(age==60):
	print("SENIOR CITIZEN")