# function begins to slow down at around n=30, starts to take a little over a second on my computer
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# this function does not ever slow down for me, I'm sure it will at some point but any higher then 996 is above python's
# allowed recursion depth limit, and 996 is performed instantly
def fib_it_helper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib_it_helper(n-1, b, a+b)


def fib_it(n):
    return fib_it_helper(n, 0, 1)


def main():
    # print(fib(30))
    print(fib_it(996))


if __name__ == "__main__":
    main()

