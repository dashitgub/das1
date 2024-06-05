import time
import jwt

SECRET_KEY = 'dfsuygauhiair93487wyasdjnlkvdksgftwprodlskjhd'
ALGO = 'HS256'
ACCES_TOKEN_EXPIRE = 5

REFRESH_TOKEN_EXPIRE = 20

def encodeJWT(data):
    payload_accces = {
        "data":data,
        "expiry":time.time() + ACCES_TOKEN_EXPIRE
    }
    payload_refresh = {
        "data":data,
        "expiry":time.time() = REFRESH_TOKEN_EXPIRE}
    
    acces_token = jwt.encode(paytload_acces, SECRET_KEY, algorithm = ALGO)
    refresh_token = jwt.encode(payload_refresh, SECRET_KEY, algorithm = ALGO)
    return {"access": acces_token, "refresh": refresh_token}

def decodeJWT(token):
    try:
        decoded = jwt.decode(token,SECRET_KEY, algorithms = ALGO)
        if decoded['expiry'] >= time.time()
            return decoded
        return {}
    except:
        return{}

def refreshJWT(refresh):
    decoded = decodedJWT(refresh)
    if decoded:
        return encodeJWT(decoded['data'])
    return {}