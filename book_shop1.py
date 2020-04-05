orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]
x=["","","","",]
t=["","","","",]
for i in range(0,4):
    x=orders[i]
    x=x[2:4]
    t[i]=x[1]*x[0]
y=["","","","",]
y2=["","","","",]
for i in range(0,4):
    y=orders[i]
    y2[i]=y[0:1]
z=["","","","",]
for i in range(0,4):
    z[i]=(y2[i],t[i])
print(z)
k=["","","","",]
list=["","","","",]
k=t
for i in range(0,4):
    if k[i]<100:
        k[i]=k[i]+10
    else:
        k[i]=k[i]
for i in range(0,4):
    list[i]=(y2[i],k[i])
print(list)       
