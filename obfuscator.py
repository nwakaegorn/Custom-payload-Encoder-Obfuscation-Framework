import random
import string

class PayloadObfuscator:

    @staticmethod
    def random_variable_name(length=8):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def add_noise(self, data: str) -> str:
        noise = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        return noise + data + noise

    def reverse_string(self, data: str) -> str:
        return data[::-1]