from base64 import b64encode

print(''' 
 _  _  _____  ___  __      __    ____  __  ___  ___  ___ 
( \( )(  _  )/ __)(  )    /__\  ( ___)/  )(__ )(__ )(__ )
 )  (  )(_)(( (__  )(__  /(__)\  )__)  )(  (_ \ (_ \ / / 
(_)\_)(_____)\___)(____)(__)(__)(__)  (__)(___/(___/(_/   
 
 
 ''')

ID = input("Enter the ID : ")

Token = b64encode(bytes(ID, 'utf-8'))

Token = Token.decode("utf-8")

print('the first 40% of the ID' ,ID, 'token is', Token)