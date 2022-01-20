import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = ",.'/?*_&%$#@!"

all = lower + upper + numbers + symbols
password = "".join(random.sample(all, 8))
print(password)