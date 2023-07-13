import random

def main() -> None:
    test_list = [120, 60, -30, 0, -14, 15, 100]

    # built-in immutable sort
    sorted_list = sorted(test_list)
    print(f"\nOriginal list: {test_list}")
    print(f"Sorted list: {sorted_list}")

    # built-in mutable sort (It's just a method for 'list' objects.)
    test_list.sort()
    print(f"\nOriginal list: It Is MODIFIED")
    print(f"Sorted list: {test_list}")

    
    test_numbers = [1, 2, 3, 4, 5, 6, 7]

    # built-in immutable shuffle
    shuffled_numbers = random.choices(test_numbers, k=len(test_numbers))
    print(f"\nOriginal list: {test_numbers}")
    print(f"Shuffled list: {shuffled_numbers}")

    # built-in mutable shuffle
    random.shuffle(test_numbers)
    print(f"\nOriginal list: It is MODIFIED")
    print(f"Shuffled list: {test_numbers}")



if __name__ == "__main__":
    main()
