def hello(name):
    print(f"Hello, {name}")


def hello2(name: str):
    print(f"Hello: {name}")


if __name__ == '__main__':
    hello("Petr")
    hello2("Martin")
