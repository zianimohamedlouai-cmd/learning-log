x = 5
y = x
x = 10
print(y)

for n in ["ali", "sara"]:
    print(n.upper())

def add(x, acc=None):
    if acc is None:
        acc = []
    acc.append(x)
    return acc

print(add(1))
print(add(2))
print(add(3, []))
print(add(4))
print(add(5, [10, 20]))
def 