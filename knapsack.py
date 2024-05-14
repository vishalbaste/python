# Given data
n = 4
w = [2,3,1,4]
p = [3,4,6,5]
M = 8

# Initialize the dynamic programming table with zeros
dp = [[0] * (M + 1) for _ in range(n + 1)]

# Fill the table using dynamic programming
for i in range(1, n + 1):
    for j in range(1, M + 1):
        if w[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + p[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

# Determine the optimal profit
optimal_profit = dp[n][M]

# Backtrack to find the solution vector
solution_vector = [0] * n
j = M
for i in range(n, 0, -1):
    if dp[i][j] != dp[i - 1][j]:
        solution_vector[i - 1] = 1
        j -= w[i - 1]

# Print the results
print("Optimal profit:", optimal_profit)
print("Solution vector:", solution_vector)
