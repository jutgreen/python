import random
import string

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

print("First alphaNumeric Random String is  ", get_random_alphaNumeric_string(16))
print("Second alphaNumeric Random String is ", get_random_alphaNumeric_string(16))
print("Third alphaNumeric Random String is  ", get_random_alphaNumeric_string(16))