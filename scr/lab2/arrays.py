def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return 'ValueError'
    return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for element in mat:
        if isinstance(element, (list, tuple)):
            result.extend(element)
        else:
            return 'TypeError'
    
    return result

if __name__ == "__main__":
    print("Тестирование min_max:")

    result = min_max([3, -1, 5, 5, 0])
    print(f"[3, -1, 5, 5, 0] - {result}")
    
    result = min_max([42])
    print(f"[42] - {result}")
    
    result = min_max([-5, -2, -9])
    print(f"[-5, -2, -9] - {result}")
    
    result = min_max([])
    print(f"[] - {result}")
    
    result = min_max([1.5, 2, 2.0, -3.1])
    print(f"[1.5, 2, 2.0, -3.1] - {result}")
    

    print("\nТестирование unique_sorted:")
    
    result = unique_sorted([3, 1, 2, 1, 3])
    print(f"[3, 1, 2, 1, 3] - {result}")
    
    result = unique_sorted([])
    print(f"[] - {result}")
    
    result = unique_sorted([-1, -1, 0, 2, 2])
    print(f"[-1, -1, 0, 2, 2] - {result}")
    
    result = unique_sorted([1.0, 1, 2.5, 2.5, 0])
    print(f"[1.0, 1, 2.5, 2.5, 0] - {result}")
    

    print("\nТестирование flatten:")
    
    result = flatten([[1, 2], [3, 4]])
    print(f"[[1, 2], [3, 4]] - {result}")

    result = flatten(([1, 2], (3, 4, 5)))
    print(f"([1, 2], (3, 4, 5)) - {result}")
    
    result = flatten([[1], [], [2, 3]])
    print(f"[[1], [], [2, 3]] - {result}")
    
    result = flatten([[1, 2], "ab"])
    print(f"[[1, 2], 'ab'] - {result}")