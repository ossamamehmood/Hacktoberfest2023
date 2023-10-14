# Program to display the Fibonacci sequence up to n-th term
while True:
    try:
        nterms = int(input("How many terms? "))
        # Check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        else:
            # First two terms
            n1, n2 = 0, 1
            count = 0

            if nterms == 1:
                print("Fibonacci sequence up to", nterms, ":")
                print(n1)
            else:
                print("Fibonacci sequence:")
                while count < nterms:
                    print(n1)
                    nth = n1 + n2
                    # Update values
                    n1 = n2
                    n2 = nth
                    count += 1
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

