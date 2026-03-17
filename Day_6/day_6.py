n=int(input("enter no.of transactions : "))

tr=[]

for i in range(n) :
    a=int(input ("enter transaction " + str(i+1) +" amount : "))
    tr.append(a)

dic={
    "normal":[],
    "large" :[],
    "high_risk":[],
    "invalid":[]
}

for i in tr:
    if i<=0:
        dic["invalid"].append(i)
    elif 1<=i<=500:
        dic["normal"].append(i)
    elif 501<=i<=2000:
        dic["large"].append(i)
    else:
        dic["high_risk"].append(i)

c=len(tr)
t_sum=sum(tr)

x=False
y=False
z=False

if c>5:
    x=True
if t_sum>5000:
    y=True
if len(dic["high_risk"])>=3:
    z=True


print("categorized transactions : ")
print("\n invalid transactions :",dic["invalid"])
print("\n large transactions :",dic["large"])
print("\n normal transactions :",dic["normal"])
print("\n high risk transactions :",dic["high_risk"])

print("\n total transaction value : ",t_sum)

print(" \n no.of transactions : \n ",c)



if x and y and z :
    print("High Risk")
elif (x and y) or (y and z) or (z and x) :
    print("Moderate Risk")
elif x or y or z :
    print("Low Risk")
else:
    print("Low Risk")



