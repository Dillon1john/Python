import re #imports regular expressions
password = input("Please enter a Password")
user_password = True

while True:
    if (len(password)<6 or len(password)>16):
        print("Not Valid! It should contain the proper length")
        break
    elif not re.search ("[A-Z]" ,password): #re.search checks regular expression database
        print("Not Valid! It should contain uppercase")
        break
    elif not re.search ("[a-z]" ,password):
        print("Not Valid! It should contain lowercase")
        break
    elif not re.search ("[0-9]" ,password):
        print("Not Valid! It should contain numbers")
        break
    elif not re.search ("[!,@,$,%,^,&,*,+,=]" ,password):
        print("Not Valid! It should contain special characters")
        break
    else: 
        print("Valid Password",password)
        user_password = False
        break
    if user_password:
        print("Not a valid password")


        # we need to make sure, if entered incorrectly (restarts) That means entering a restart
        #option right after each invalid break


        
        
