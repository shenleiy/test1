import rsa
import base64
from urllib import request


def create_new_keys(lens):
    (public_key, private_key) = rsa.newkeys(lens)
    with open('public1.pem', 'wb') as f:
        f.write(public_key.save_pkcs1())
    with open('private1.pem', 'wb') as f:
        f.write(private_key.save_pkcs1())


def rsa_encrypt(msg):
    with open('public.pem', 'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())
    code = rsa.encrypt(msg.encode('utf-8'), public_key)
    code = base64.b64encode(code).decode('utf-8')
    print(code)
    code = request.quote(code)
    print(code)
    return code


def rsa_decrypt(code):
    code = request.unquote(code)
    with open('private1.pem', 'rb') as private_file:
        private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
    code = base64.b64decode(code.encode('utf-8'))
    msg = rsa.decrypt(code, private_key).decode('utf-8')
    return msg


rsa_encrypt('Aa123456')
