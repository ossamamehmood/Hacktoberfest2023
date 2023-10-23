// Check if number is prime
function isPrime(number) {

  // Numbers less than 2 are not prime
  if (number < 2) return false;

  // Check divisibility from 2 to square root of number
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i == 0) return false;
  }

  return true;

}

// Usage
const num = 17;

if (isPrime(num)) {
  console.log(`${num} is prime`);
} else {
  console.log(`${num} is not prime`);
}