student_id=(input("enter student id"))
email=input("enter email id")
p=  input("enter password")
r= input("enter referral code")

if len(student_id)==7 and student_id[0:3]=="CSE" and student_id[3]=="-" and student_id[4:].isdigit() :
    if email.count(".")>=1 and email.count("@")==1 and email[0]!= "@" and email[-1]!= "@" and email[-4:]==".edu" :
        if len(p)>=8 and p[0].isupper() and (p.count("0")+p.count("1")+p.count("2")+p.count("3")+p.count("5")+p.count("6")+p.count("7")+p.count("8")+p.count("9")+p.count("4")) >=1 :
            if r[0:3]=="REF" and (r[3:5]).isdigit() and r[-1]=="@" :
                print("APPROVED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")
