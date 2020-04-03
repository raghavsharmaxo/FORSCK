s=['','','','','','','']
a=float(input("HOW MANY ITEMS DO YOU REQUIRE:"))
i=0
while i<3:
    b=input("ENTER ITEM:")
    s[i]=b
    p=input("DONE?")
    if p.startswith("D"):
        break
    else:
        i=i+1
    
   

        

print("__________________________________________________________")    
print("SELECED ITEMS ARE:")
for x in s:
    print(x)

print("__________________________________________________________")    