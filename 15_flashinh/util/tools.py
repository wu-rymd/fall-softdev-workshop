from os import urandom

def generate_random_secretkey():
    return urandom(32)
