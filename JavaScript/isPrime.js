// This JavaScript code checks if a given number is prime.
function isPrime(number) {
    if (number <= 1) {
      return false;
    }
  
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false;
      }
    }
  
    return true;
  }
  
  const num = 17;
  if (isPrime(num)) {
    console.log(`${num} is a prime number.`);
  } else {
    console.log(`${num} is not a prime number.`);
  }

  // Asynchronous Programming with Promises:
// This code uses Promises to fetch data from a remote API and handle the results.
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { message: "Data fetched successfully" };
      resolve(data);
    }, 2000);
  });
}

fetchData()
  .then((data) => {
    console.log(data.message);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
