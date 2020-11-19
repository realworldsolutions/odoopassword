from passlib.context import CryptContext
import sys
import warnings
warnings.filterwarnings("ignore")

if len(sys.argv) != 2:
    raise ValueError('Please provide password')

setpw = CryptContext(schemes=['pbkdf2_sha512'])
print(setpw.encrypt(sys.argv[1]))