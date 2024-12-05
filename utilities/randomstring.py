import random
import string
def randomStringGenerator(size=5,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
