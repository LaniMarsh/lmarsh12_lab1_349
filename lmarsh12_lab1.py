import sys

def singleton (filename) -> int:
    with open(filename, 'r') as f:
        numbers = []
        for line in f:
            number = int(line.strip())
            numbers.append(number)

    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid % 2 == 0:
            if numbers[mid] == numbers[mid + 1]:
                # singleton on the right of mid
                left = mid + 2
            else:
                # singleton on the left of mid
                right = mid - 1
        else:
            if numbers[mid] == numbers[mid - 1]:
                # singleton on the right of mid
                left = mid + 1
            else:
                # singleton on the left of mid
                right = mid - 2

    return numbers[left]

if __name__ == "__main__":
    filename = sys.argv[1]
    single = singleton(filename)
    print(single)