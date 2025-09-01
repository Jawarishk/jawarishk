def remove_odds(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def main():
    my_list = [3, 7, 2, 8, 5, 10, 11, 14]
    result = remove_odds(my_list)
    print("Original list:", my_list)
    print("Even numbers only:", result)

main()
