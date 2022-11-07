from random import sample
import string
def get_random_password(n=8) -> str:
    chars = sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, n)

    return "".join(chars)  # TODO написать функцию генерации случайных паролей


print(get_random_password())