def extra_space(S, M, i, j):
    return M - j + i - word_sum(S[i:j], 0)


def word_sum(S, i):
    if S[i] == None:
        return 0
    else:
        return len(S[i]) + word_sum(S, i+1)


def badness_line(S, M, i, j):
    e = extra_space(S, M, i, j)
    if e >= 0:
        return e
    else:
        return float('inf')


def min_bad(S, M, i):
    return min_bad_helper(S, M, i, i)


def min_bad_helper(S, M, i, j):
    badness = badness_line(S, M, i, j)
    if j == len(S):
        return 0
    elif badness == float('inf'):
        return badness_line(S, M, i, j-1) + min_bad_helper(S, M, j-1, j-1)
    else:
        return min_bad_helper(S, M, i, j+1)


def min_bad_dynamic(S, M):
    total_words = len(S)
    dynamic = [0 for i in range(total_words)]
    i = 0
    for j in range(total_words):
        if j == total_words:
            dynamic[j] = 0
        elif badness_line(S, M, i, j) == float('inf'):
            dynamic[j] = dynamic[j-1]
            i = j
        else:
            dynamic[j] = badness_line(S, M, i, j)
    return dynamic[total_words]