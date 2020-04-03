s=['$876,001','$543,903','$2453,896']

length = len(s)
i=0

while i<length:
	
	a=s[i].replace("$","")
	b=a.replace(",","")
	b=int(b)
	s[i]=b
	i=i+1



print(s)

