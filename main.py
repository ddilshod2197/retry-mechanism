import time
import random

class RetryMechanism:
    def __init__(self, max_attempts, delay):
        self.max_attempts = max_attempts
        self.delay = delay

    def retry(self, func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < self.max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts < self.max_attempts:
                        print(f"Attempt {attempts} failed. Retrying in {self.delay} seconds...")
                        time.sleep(self.delay)
                    else:
                        raise e
        return wrapper

# Misol
@RetryMechanism(max_attempts=3, delay=2)
def example_function():
    if random.random() < 0.5:
        raise Exception("Example error")
    else:
        return "Example success"

print(example_function())
```

Kodda RetryMechanism klassi yaratilib, uda unga max_attempts va delay parametrini berish uchun constructor yaratildi. Keyin retry metodini yaratib, uda unga func parametrlar berish uchun wrapper metod yaratildi. Wrapper metodda max_attempts dan kam bo'lgan urinishlar uchun func metodini chaqiradi, lekin agar urinishlar max_attempts ga teng bo'lsa, Exceptionni qaytaradi. Misol uchun example_function metodini yaratib, uda unga RetryMechanism klassidan instance yaratib, uda unga max_attempts va delay parametrini berish uchun @RetryMechanism dekoratoridan foydalanildi.
