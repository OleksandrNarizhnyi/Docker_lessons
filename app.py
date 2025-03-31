def greeting(name: str, age: int) -> str:
    res = f"HI, I'M {name}! I'M {age} y.o"

    return res


if __name__ == "__main__":
    res = greeting("O'gway", 325)

    print(res)