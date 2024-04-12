def add(*args):
    # args is a tuple
    _sum = 0
    for n in args:
        _sum += n
    return _sum


print(add(5, 7, 6))


def calculate(n , **kwargs):
    # kwargs is a dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f'key: {key}, value: {value}')
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
