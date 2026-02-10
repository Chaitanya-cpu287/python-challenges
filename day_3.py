n=int(input("enter no.of students "))
l=[0]*n
for i in range(n):
    print("enter marks of student ",i+1)
    l[i]=int (input())
print("Marks list is ",l)
a=0
b=0
number = (input("enter Registration number"))
print("if sum of Registration number is odd , then add 10 otherwise add 8 ")
print("Registration number is  ",number)

s=0
for x in number :
    s+=int(x)
print("sum of registration number is ",s)

if s%2==0:
    print("its even")
    for i in range(len(l)) :
        l[i]+=8
else:
    print("its odd")
    for i in range(len(l)) :
        l[i]+=10

print("new mark list is ",l)


for j in range(len(l)) :

    if 90 <= l[j]<=100 :
        print(l[j], " - Excellent")
        a+=1
    elif  75 <= l[j]<=89 :
        print(l[j], " - Very Good")
        a += 1
    elif  60 <= l[j]<=74 :
        print(l[j], " - Good")
        a += 1
    elif  40 <= l[j]<=59 :
        print(l[j], " - Average")
        a += 1
    elif  0 <= l[j]<=39 :
        print(l[j], " - Fail")
        b+=1
    else:
        print("Invalid marks")
print ("total valid students are " ,a)
print ("total failed students are " ,b)