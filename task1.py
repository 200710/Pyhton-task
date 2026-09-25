def f(x):
    print(f"{x} = {round((x * round(9 / 5, 2)) + 32, 2)}")

def k(x):
    print(f"{x} = {round(x + 273.15, 2)}")
f(int(input()))
k(int(input()))
