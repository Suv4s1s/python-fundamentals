def Fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    try:
        n = int(input("Enter a value: "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        fib = Fibonacci(n)
        print("Fibonacci sequence up to {}:".format(n))
        print(fib)
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()