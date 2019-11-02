def binary_search(data: list, target: int, low, high) -> bool:
    if low > high:
        return False
    else:
        mid = (low+high) // 2  # python是弱类型，需要使用整除
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


if __name__ == "__main__":
    data = [2, 4, 5, 7, 8, 912, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    low = 0
    high = len(data)-1
    target = 22
    print(binary_search(data, target, low, high))

