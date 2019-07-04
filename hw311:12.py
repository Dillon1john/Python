capitalABC= ["A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"]
lowercaseabc=["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]
specialchracter=["!,@,$,%,^,&,*,+,="]
number=[1,2,3,4,5,6,7,8,9,0]
user_passwords=[ ]
while True:
    password= input("enter the password: ")
    user_passwords.append(password)
    if capitalABC not in user_passwords:
        print("Not Valid! It should contain atleast one capital letter")
        if lowercaseabc not in user_passwords:
            print("Not Valid! It should contain atleast one lowercase letter")
            if number not in user_passwords:
                print("Not Valid! It should contain atleast one number")
                continue
                if specialchracter not in user_passwords:
                  print("Not Valid! It must contain atleast one special character.")
                  continue
                  if len(password)<6:
                     print ("Not Valid! Passowrd must be more than 6")
                     continue
                     if len(password)>16:
                        print("Not Valid! Password must be less than 16")
    else:   
        print("Valid Password",user_passwords)
        
        
