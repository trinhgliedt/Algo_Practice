class KnapsackProblem:

    def __init__(self, n, M, w, v):
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 for _ in range(M+1)] for _ in range(n+1)]

    def solve(self):
        # construct the S dynamic programming table
        for n in range(self.n+1):
            for m in range(self.M+1):
                # if not taking item, value equals to the cell on the left
                not_taking_item = self.S[n-1][m]
                taking_item = 0

                if self.w[n] <= m:
                    # taking item: value equals to old value + item value.
                    # available weight = old avail weight - weight of the new item
                    taking_item = self.v[n] + self.S[n-1][m-self.w[n]]
                # memorization - we store the sub-results to avoid calculating the same values over and over
                self.S[n][m] = max(not_taking_item, taking_item)

    def show_result(self):
        print(f"Total benefit: {self.S[self.n][self.M]}")

        m = self.M
        for n in range(self.n, 0, -1):
            if self.S[n][m] != 0 and self.S[n][m] != self.S[n-1][m]:
                # print(n, m, self.S[n][m])
                print(f"We take item #{n}")
                m = m - self.w[n]


if __name__ == '__main__':
    # knapsack = KnapsackProblem(4, 7, [0, 1, 3, 4, 5], [0, 1, 4, 5, 7])
    knapsack = KnapsackProblem(3, 5, [0, 4, 2, 3], [0, 10, 4, 7])
    knapsack.solve()
    knapsack.show_result()
