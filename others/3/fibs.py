def fibonacci_sequence(n):
    fib_sequence = [1, 2]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

first_10_fibonacci = fibonacci_sequence(10)
print(first_10_fibonacci)

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[1,2,4,6,9,12,16,20,25]
