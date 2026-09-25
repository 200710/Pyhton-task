from random import *
from string import *
def generate_password():
    letters = [choice(ascii_uppercase) for _ in range(3)]
    digits_ = [choice(digits) for _ in range(3)]
    special_chars = [choice('!@#$%^&*') for _ in range(2)]
    password_list = letters + digits_ + special_chars
    shuffle(password_list)
    password = ''.join(password_list)
    return password
for i in range(50):
    print(generate_password())
