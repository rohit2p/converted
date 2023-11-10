# advance argument
# (1) arbitrary position argument
def add(*args):  # args is a tuple
    sum = 0
    for i in args:
        sum += i
    print(sum)
    print(args[2])  # index 2
    print("_________________")


add(4, 5, 7, 10)  # we can add as many values we want


# (2) arbitrary keyword argument
def calculator(**kwargs):  # kwargs is a dictionary
    return kwargs


print(calculator(add="+", multiply="*", devide="/"))
print("_____________________")


# example 2
def cal(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])


cal(add="3", mul="5", div="8")
