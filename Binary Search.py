def BinarySearch(list_of_numbers, number_to_find, left, right):
    middle = (left + right)//2
    if list_of_numbers[middle] == number_to_find:
        return middle
    elif list_of_numbers[middle] < number_to_find:
        left = middle + 1
    elif list_of_numbers[middle] > number_to_find:
        right = middle - 1
    else:
        print("number not found")

    return BinarySearch(list_of_numbers, number_to_find, left, right)

if __name__ == '__main__':
    number_list = [2,4,5,11,17,20,25,32,67,78,90]
    number_to_find = 0
    index = BinarySearch(number_list, number_to_find, 0, len(number_list) - 1)
    print(f'Number found in the index : {index}')