import time
import os
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def run():
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")
    ts = time.time()
    print(ts)
    id = id_generator()
    print(id)

run()

