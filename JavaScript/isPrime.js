// This JavaScript code checks if a given number is prime.

// Define a function called 'isPrime' that takes a 'number' as its parameter.
function isPrime(number) {
    // Check if the number is less than or equal to 1, which is not a prime number.
    if (number <= 1) {
      return false;
    }

    // Use a for loop to iterate from 2 to the square root of the 'number.'
    for (let i = 2; i <= Math.sqrt(number); i++) {
      // Check if the 'number' is divisible evenly by 'i.'
      if (number % i === 0) {
        // If it is divisible evenly, the 'number' is not prime.
        return false;
      }
    }

    // If none of the above conditions are met, the 'number' is prime.
    return true;
}

// Define a constant variable 'num' and set it to the value 17.
const num = 17;

// Check if 'num' is a prime number by calling the 'isPrime' function.
if (isPrime(num)) {
    // If 'isPrime' returns true, log that 'num' is a prime number.
    console.log(`${num} is a prime number.`);
} else {
    // If 'isPrime' returns false, log that 'num' is not a prime number.
    console.log(`${num} is not a prime number.`);
}
