def head(li):
    return li[0]


def tail(li):
    return li[1:]


def is_empty(li):
    return li == []


def add_to_front(x, li):
    return [x] + li


def r(li):
    if is_empty(li):
        return []
    else:
        return r(tail(li)) + [head(li)]


def prod(m, n):
    if m == 0:
        return 0
    else:
        return prod(m - 1, n) + n


def fast_pow(b, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return fast_pow(b ** 2, k/2)
    else:
        p = k - 1
        return fast_pow(b ** 2, p/2) * b


def prod_accum(m, n, a):
    if m == 0:
        return a
    else:
        return prod_accum(m - 1, n, a + n)


def failure_plus(a, b):
    if a == -1 or b == -1:
        return -1
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a + b


def min(a, b):
    if a == -1:
        return b
    elif b == -1:
        return a
    elif a < b:
        return a
    else:
        return b


def min_change(a, d):
    if a == 0:
        return 0
    elif is_empty(d):
        return -1
    else:
        if head(d) > a:
            return min_change(a, tail(d))
        else:
            return min(failure_plus(1, min_change(a-head(d), d)), min_change(a, tail(d)))


def greedy_min_change(a, d):
    if a == 0:
        return 0
    elif is_empty(d):
        return -1
    else:
        if head(d) > a:
            return greedy_min_change(a, tail(d))
        else:
            return failure_plus((a / head(d)), greedy_min_change((a % d), tail(d)))


def pow_it(b, n):
    a = 1
    while n > 0:
        a *= b
        n = n-1
    return a


def test():
    list = [3, 2, 6, 1]
    empty_list = []

    assert head(list) == 3, "Head test failed"
    assert tail(list) == [2, 6, 1], "Tail test failed"

    assert tail(empty_list) == [], "Empty tail test failed"

    assert not is_empty(list), "Populated list should not be empty"
    assert is_empty(empty_list), "Empty list should be empty"
    assert add_to_front(4, list) == [4, 3, 2, 6, 1], "Added to front incorrectly"

    assert r(list) == [1, 6, 2, 3], "List reversed incorrectly"

    assert prod(3, 2) == 6, "Product of 3*2 incorrect"
    assert prod(9, 1928) == 17352, "Product of 9*1928 incorrect"

    assert fast_pow(9, 4) == 6561, "9^4 incorrect (even number test)"
    assert fast_pow(9, 5) == 59049, "9^5 incorrect (odd number test)"

    assert prod_accum(3, 2, 0) == 6, "Product of 3*2 incorrect"

    change_list = [100, 50, 20, 10, 5, 1]
    assert min_change(6, change_list) == 2, "Min change of $6 should be 2 bills"
    assert min_change(286, change_list) == 7, "Min change of $286 should be 7 bills"

    assert pow_it(10, 3) == 1000, "10^3 should be equal to 1000"
    assert pow_it(3, 3) == 27, "3^3 should be equal to 27"



if __name__ == "__main__":
    test()
