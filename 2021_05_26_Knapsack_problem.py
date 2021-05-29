def knapsack_recursion(m, w, v, n):
    if m == 0 or n == 0:
        return 0
    # the given item can't fit into the knapsack
    if w[n-1] > m:
        return knapsack_recursion(m, w, v, n-1)
    else:
        # given item can fit into the knapsack so we have 2 options (include, exclude)
        n_included = v[n-1] + knapsack_recursion(m-w[n-1], w, v, n-1)
        n_excluded = knapsack_recursion(m, w, v, n-1)

        return max(n_included, n_excluded)


# print(knapsack_recursion(5, [4, 2, 3], [10, 4, 7], 3))


def knapsack(n, m, v, w):
    if m == 0 or n == 0:
        return 0
    if w[n-1] > m:
        return knapsack(n-1, m, v, w)
    else:
        n_included = v[n-1] + knapsack(n-1, m-w[n-1], v, w)
        n_excluded = knapsack(n-1, m, v, w)
    return max(n_included, n_excluded)


print(knapsack(3, 5, [10, 4, 7], [4, 2, 3]))
