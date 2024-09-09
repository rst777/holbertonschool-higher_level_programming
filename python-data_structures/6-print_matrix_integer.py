#!/user/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, num in enumerate(line):
            if i < len(line) -1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print("$")


