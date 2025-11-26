def stage1():
    counter = 1
    matrix = []
    for i in range(13):
        row = []
        for j in range(13):
            row.append(counter)
            counter += 1
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def stage2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j % 2 == 1:
                matrix[i][j] += j
    return matrix


def sum_of_digit(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


def main():
    matrix = stage1()
    print_matrix(matrix)
    print()
    matrix = stage2(matrix)
    print_matrix(matrix)
    num = int(input("enter number: "))
    print(sum_of_digit(num))
main()