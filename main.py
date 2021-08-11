# Binary Search: requirement is list has to be sorted and returns the index of search element

def binary_search(lst_ele, search):
    left = 0
    right = len(lst_ele)
    mid = (left + right) // 2

    while left < right and left < mid:

        if search == lst_ele[mid]:
            return mid

        elif search < lst_ele[mid]:
            right = mid

        else:
            left = mid

        # print(left, mid, right)

        mid = (left + right) // 2

    return -1


if __name__ == '__main__':
    lst = [5, 4, 3, 6, 9, 12, 15]
    lst.sort()
    print(binary_search(lst, 6))
    print(binary_search(lst, 12))
    print(binary_search(lst, 1000))
