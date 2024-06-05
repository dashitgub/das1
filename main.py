import time
from jwt_handler import encodeJWT, decodeJWT,refreshJWT

user = {"email": "dasmukumjanovvv@gmail.com", "username": "das", "id": 1}

jwt_token = encodeJWT(user) #{'access_token':asdasds }

time.sleep(6)

decoded = decodeJWT(jwt_token['access_token'])

new_jwt_token = refreshJWT(jwt_token['refresh_token'])
print(new_jwt_token)

