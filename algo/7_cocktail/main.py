from typing import List


# def cocktail_sort(numbers:List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     swapped = True
#     start = 0
#     end = len_numbers - 1
#     while swapped:
#         swapped = False

#         for i in range(start, end):
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#                 swapped = True

#         if not swapped:
#             break

#         swapped = False
#         end = end - 1

#         for i in range(end-1, start-1,-1):
#             print(i)
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#                 swapped = True

#         start = start + 1

#     return numbers

def cocktail_sort(numbers: List[int]) -> List[int]:
    swap = False
    len_numbers = len(numbers)
    start = 0
    end = len_numbers-1

    while swap:
        swap = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swap = True
        if not swap:
            break
        swap = False
        end = end -1
        for i in reversed(range(start-1, end-1)):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swap = True
        start = start + 1
    
    return numbers



if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(cocktail_sort(nums))
