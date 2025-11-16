import random

def generate_unique_email():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    rand = "".join(random.choice(chars) for _ in range(10))
    return "test_user_" + rand + "@example.com"