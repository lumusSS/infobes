from .encrypt import method

from rsa.rsa_encrypt import RsaEncrypt
from rsa.rsa_context_creator import RsaEncryptContextCreator

encryptions = {
    "RSA" : method(RsaEncrypt(), RsaEncryptContextCreator()),
}