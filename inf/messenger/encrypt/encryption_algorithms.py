from .encrypt import method

from .rsa.rsa_encrypt import RsaEncrypt

encryptions = {
    "RSA" : method(RsaEncrypt()),
}