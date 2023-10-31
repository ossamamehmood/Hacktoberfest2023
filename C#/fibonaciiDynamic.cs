using System;

public class Fibonacci {
    public static long CalculateFibonacci(int n) {
        if (n <= 0)
            return 0;
        if (n == 1)
            return 1;

        long[] fib = new long[n + 1];
        fib[0] = 0;
        fib[1] = 1;

        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }

        return fib[n];
    }

    public static void Main() {
        int n = 10; // Change this to the desired Fibonacci number you want to calculate.
        long result = CalculateFibonacci(n);
        Console.WriteLine("Fibonacci number at position " + n + " is: " + result);
    }
}
