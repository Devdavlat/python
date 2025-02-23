"""
only_even_parameters nomli dekorator yarating, bunda quyidagi funksiyallarda ishlating va tegishli natija qaytaring.
"""


def only_even_parameters(func):
    def only_even(*args):
        for i in args:
            if i % 2 == 0:
                return func(*args)
            else:
                return f"Please add only even numbers!"

    return only_even


@only_even_parameters
def add(a, b):
    return a + b


@only_even_parameters
def multiply(a, b, c, d):
    return a * b * c * d


print(add(2, 8))
print(multiply(6, 3, 2, 2))
