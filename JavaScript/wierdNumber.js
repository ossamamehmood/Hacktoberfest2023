// Write a program that finds weird numbers between and including 10 - 100
// weirdNumber(10, 100);
// More info in the link -> https://en.wikipedia.org/wiki/Weird_number

function weirdNumber(startRange = 10, EndRange = 100) {
  if(typeof(startRange) !== 'number') {
    console.error('Start Range must be a number');
    return;
  }

  if(typeof(EndRange) !== 'number') {
    console.error('End Range must be a number');
    return;
  }

  if(EndRange > 100) {
    console.warn('End Range must not exceed 100');
    return;
  }

  const weirdNum = [];
  function combination(array){
    const results = [[]];
    for (const value of array) {
      const copy = [...results];
      for (const prefix of copy) {
        results.push(prefix.concat(value));
      }
    }
    return results;
  }
  for (let i = startRange; i <= EndRange; i++){
    const possibleDivisors = [];
    for (let j = 1; j <= i / 2; j++) {
      if (i % j === 0) {
        possibleDivisors.push(j);
      }
    }
    const sumOfDivisors = possibleDivisors.reduce((a, b) => a + b, 0);
    const combArray = combination(possibleDivisors);
    const sumOfSubset = [];
    combArray.forEach((arr) => {
      const sum = arr.reduce((a, b) => a + b, 0);
      sumOfSubset.push(sum);
    });
    if (!sumOfSubset.includes(i) && sumOfDivisors > i) {
      weirdNum.push(i);
    }
  }
  if (weirdNum.length) {
    console.log(`Here is the weird number: ${weirdNum.join(', ')}`);
  } else {
    console.log(`No weird number found within the range ${startRange} - ${EndRange}`);
  }
}