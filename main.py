from base64 import b64encode

print(''' 
 _  _  _____  ___  __      __    ____  __  ___  ___  ___ 
( \( )(  _  )/ __)(  )    /__\  ( ___)/  )(__ )(__ )(__ )
 )  (  )(_)(( (__  )(__  /(__)\  )__)  )(  (_ \ (_ \ / / 
(_)\_)(_____)\___)(____)(__)(__)(__)  (__)(___/(___/(_/   
 
 
 ''')

i = True
n = True

class token:
    def __init__(self, ID):
        self.Token = b64encode(bytes(ID, 'utf-8'))
        self.Token = self.Token.decode("utf-8")

while i:
    Answer = token(input("Enter the ID : "))
    print('the first 40% of this ID token is', Answer.Token)
    while n == True:
        loop = input('another one ? (yes/no) : ')
        if loop == "yes":
            i=True
            break
        if loop == "no":
            i=False
            break
        else:
            print("please enter yes or no")
            pass