name=input("enter your full name")
email=input("enter your email id")
mobile=input("enter your mobile number ")
age=int(input("enter your age"))

if name.count(" ")>=1 and name[0]!=" " and name[-1]==" " :
    if email.count("@")!=0 and email[0]!="@" :
        if len(mobile)==10 and mobile.isdigit() and mobile[0]!=0 :
            if 18 <= age<=60 :
                print("User Profile is VALID")
            else:
                print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")
