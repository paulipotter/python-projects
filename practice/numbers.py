def print_formatted(number):
    # your code goes here
    line = ""
    n = 0
    for n in range(1, number):
        line += "{0}\t{1}\t{2}\t{3}\n".format(n, '{:d}'.format(oct(n)), hex(n), bin(n))
    print(line)
    return line

number = input("pls put a number here: ")
print_formatted(number)
