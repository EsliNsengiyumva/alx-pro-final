def pascal_triangle(n):
    if n <= 0:
        return []

    result = []

    for i in range(n):
        row = [1] * (i + 1)

        if i > 1:
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(row)

    return result

# Example usage:
n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
