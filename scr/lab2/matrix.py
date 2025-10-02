def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [[mat[i][j] for i in range(len(mat))] for j in range(num_cols)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
           return 'ValueError'
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(num_cols)]

if __name__ == "__main__":
    print("Тестирование transpose:")
    result = transpose([[1, 2, 3]])
    print(f"[[1, 2, 3]] - {result}")

    result = transpose([[1], [2], [3]])
    print(f"[[1], [2], [3]] - {result}")

    result = transpose([[1, 2], [3, 4]])
    print(f"[[1, 2], [3, 4]] - {result}")
    
    result = transpose([])
    print(f"[] - {result}")

    result = transpose([[1, 2], [3]])
    print(f"[[1, 2], [3]] - {result}")
    

    print("\nТестирование row_sums:")

    result = row_sums([[1, 2, 3], [4, 5, 6]])
    print(f"[[1, 2, 3], [4, 5, 6]] - {result}")
    
    result = row_sums([[-1, 1], [10, -10]])
    print(f"[[-1, 1], [10, -10]] - {result}")
    
    result = row_sums([[0, 0], [0, 0]])
    print(f"[[0, 0], [0, 0]] - {result}")
    
    result = row_sums([[1, 2], [3]])
    print(f"[[1, 2], [3]] - {result}")
    

    print("\nТестирование col_sums:")

    result = col_sums([[1, 2, 3], [4, 5, 6]])
    print(f"[[1, 2, 3], [4, 5, 6]] - {result}")

    result = col_sums([[-1, 1], [10, -10]])
    print(f"[[-1, 1], [10, -10]] - {result}")

    result = col_sums([[0, 0], [0, 0]])
    print(f"[[0, 0], [0, 0]] - {result}")

    result = col_sums([[1, 2], [3]])
    print(f"[[1, 2], [3]] - {result}")