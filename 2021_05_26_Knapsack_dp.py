class KnapsackProblem:

    def __init__(self, n, M, w, v):
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 for _ in range(M+1)] for _ in range(n+1)]

    def solve(self):
        # construct the S dynamic programming table
        for i in range(self.n+1):
            for w in range(self.M+1):
                not_taking_item = self.S[i-1][w]
                taking_item = 0

                if self.w[i] <= w:
                    taking_item = self.v[i] + self.S[i-1][w-self.w[i]]
                # memorization - we store the sub-results to avoid calculating the same values over and over
                self.S[i][w] = max(not_taking_item, taking_item)

    def show_result(self):
        print(f"Total benefit: {self.S[self.n][self.M]}")

        w = self.M
        for n in range(self.n, 0, -1):
            if self.S[n][w] != 0 and self.S[n][w] != self.S[n-1][w]:
                print(f"We take item #{n}")
                w = w - self.w[n]


if __name__ == '__main__':
    knapsack = KnapsackProblem(4, 7, [0, 1, 3, 4, 5], [0, 1, 4, 5, 7])
    knapsack.solve()
    knapsack.show_result()
