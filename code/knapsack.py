def knapsack(weights, values, W):
    N = len(weights)
    memo = [[None] * N for _ in range(W + 1)]
    return knapsack_recursive(weights, values, W, len(weights), memo)


def knapsack_recursive(weights, values, W, N, memo):
    if N == 0 or W == 0:
        return 0

    if weights[N - 1] > W:
        return knapsack_recursive(weights, values, W, N - 1, memo)

    if memo[W][N - 1] is None:
        memo[W][N - 1] = max(values[N - 1] + knapsack_recursive(weights, values, W - weights[N - 1], N - 1, memo),
                             knapsack_recursive(weights, values, W, N - 1, memo))

    return memo[W][N - 1]


weights = [56, 59, 80, 64, 75, 17]
values = [50, 50, 64, 46, 50, 5]

W = 190

print(knapsack(weights, values, W))
