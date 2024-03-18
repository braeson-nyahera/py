def generate_fibonacci_sequence(n):
    fibonacci = [0, 1]
    
    while len(fibonacci) < n:
        next_term = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_term)

    return fibonacci


def main():
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    fibonacci_sequence = generate_fibonacci_sequence(n)

    print("Fibonacci sequence up to term", n, "is:")
    print(fibonacci_sequence)

if __name__ =="__main__":
    main()