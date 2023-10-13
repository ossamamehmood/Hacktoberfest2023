const isPrime = (number) => {
    if(number <= 1) return false;
    for (let i = 2; i <= Math.sqrt(number); i++){
      return (number % i === 0) ? false : true;
    }
  }
  const testIsPrime = (arrNumbers) => arrNumbers.map((num) => isPrime(num));
  console.log(testIsPrime([5,10,17, 23])) // [true, false, true, true]