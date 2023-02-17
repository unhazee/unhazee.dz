def fib_gen(n: int):
    fib1 = 1
    fib2 = 0
    i = 0
    while i < n -2 :
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        yield fib2
for x in fib_gen(10):
    print(x)


def word_gen(s: str):
    for w in s.split():
        yield w
for y in word_gen(input()):
    print(y)