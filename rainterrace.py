def trap_rain_water(heights):
    n = len(heights)
    if n == 0:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n
    
    # Calculate the max height to the left of each element
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # Calculate the max height to the right of each element
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    
    # Calculate the trapped water at each element
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - heights[i]
    
    return water

# Example usage
heights = [3, 4, 0, 2, 3, 1]
result = trap_rain_water(heights)
print("Amount of trapped rainwater:", result)
