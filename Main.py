#this determines what fibonaccit position you wish to find.
def main():
    position = int(input("Please enter the fibonacci position you wish to find: "))
    fibonacci_list = []
    while len(fibonacci_list) < position:
        fibonacci_list = fibonacci_sequence(fibonacci_list)
    print(fibonacci_list[-1])


#solution to fibonacci sequence
def fibonacci_sequence(fibonacci_list):
    if len(fibonacci_list) == 0:
        fibonacci_list.append(0)
        return fibonacci_list
    elif len(fibonacci_list) < 2:
        fibonacci_list.append(1)
        return fibonacci_list
    else:
        fibonacci_list.append((fibonacci_list[-1] + fibonacci_list[-2]))
        return fibonacci_list

main()