n= int (input("enter number of students "))
l=[0]*n
r=input("enter registration number")
D=int(r[-1])

for i in range(n) :
    print("enter marks of student ",i+1)
    l[i]=int(input())
Ignore=[]
Low_Risk=[]
High_Risk=[]
Medium_Risk=[]
Critical_Risk=[]
a=0
b=0
for i in range(n) :
    if l[i]<0 :
        a+=1
    elif 0<=l[i]<=30 :
        Low_Risk.append(l[i])
        b+=1
    elif 31<=l[i]<=60 :
        Medium_Risk.append(l[i])
        b += 1
    elif 61<=l[i]<100 :
        High_Risk.append(l[i])
        b += 1
    else:
        Critical_Risk.append(l[i])
        b += 1

print("last digit of registration number is ",D)
print("Low Risk : ",Low_Risk)
print("Medium Risk : ",Medium_Risk)
print("High Risk : ",High_Risk)
print("Critical Risk : ",Critical_Risk)





if D%2 ==0 :
    x = len(Low_Risk)
    print("Last digit of registration is even so removing Low Risk")

    Low_Risk=[]
else :
    print("Last digit of registration is odd so removing Critical Risk")
    x = len(Critical_Risk)
    for i in range(n) :

        Critical_Risk = []

print ("After Personalized Filtering:")
print("Low Risk : ",Low_Risk)
print("Medium Risk : ",Medium_Risk)
print("High Risk : ",High_Risk)
print("Critical Risk : ",Critical_Risk)


print("total valid entries : ",b)
print("ignored entries : ",a)
print("removed because of personalization : ",x)