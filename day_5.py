# Disaster Resource Dispatch System
# Name: chaitanya
# L value: 9
# PLI value: 0
# Applied Rule: Rule A (Remove Low Demand)

n=int(input("enter no.of resource requests : "))

l=[0]*n
for i in range(n) :
    print("enter request no ",i+1)
    l[i]=int(input())

print("list of resource requirements ",l)

low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_requests=[]

x=0
for i in range(n) :
    if l[i] <0:
        print(l[i],"  invalid request ")
        invalid_requests.append(l[i])
    elif l[i]==0 :
        print(l[i], "  No Demand")

    elif 1<=l[i]<=20:
        print(l[i], "  Low Demand")
        low_demand.append(l[i])
        x += 1
    elif 21<=l[i]<=50:
        print(l[i], "  Moderate Demand")
        moderate_demand.append(l[i])
        x += 1
    else :
        print(l[i], "  High Demand")
        high_demand.append(l[i])
        x += 1

print(" lists before PLI are : ")
print("Low Demand : ",low_demand)
print("Moderate Demand : ",moderate_demand)
print("High Demand : ",high_demand)
print("Invalid Requests : ",invalid_requests)

name="chaitanya"
l=len(name)
PLI=l%3
if PLI==0:
    a=len(low_demand)
    low_demand=[]
elif PLI==1:
    a = len(high_demand)
    high_demand=[]
else:
    a=len(low_demand)+len(high_demand)+len(invalid_requests)
    low_demand = []
    high_demand = []
    invalid_requests = []

print("total no.of valid requests are : ",x)
print("total no.of removed requests due to PLI are  : ", a)
print("length of name is : ",l)
print("PLI is : ", PLI)
print("final lists after PLI are : ")
print("Low Demand : ",low_demand)
print("Moderate Demand : ",moderate_demand)
print("High Demand : ",high_demand)
print("Invalid Requests : ",invalid_requests)









