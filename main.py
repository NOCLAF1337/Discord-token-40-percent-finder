import base64

ID = input("ID : ")

Token = base64.b64encode(bytes(ID, 'utf-8'))

Token = Token.decode("utf-8")

print('the first part of the ID' ,ID, 'token is', Token)