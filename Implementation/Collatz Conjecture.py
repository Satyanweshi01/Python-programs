num1 = int(input("Enter any positive number :"))


def collatz_sequence(num):
    if num < 0:
        raise ValueError("Number must be positive")
    num_list = []
    counter = 0
    while num != 1:
        num_list.append(num)
        if num % 2 == 0:
            num = num//2
            counter+=1
        else:
            num = 3*num + 1
            counter+=1
    num_list.append(1)
    print(num_list)
    print(f"The number of steps it took:{counter}")

collatz_sequence(num1)
