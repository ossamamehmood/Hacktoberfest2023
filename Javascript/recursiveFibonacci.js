function fib(n) {
    if (n === 0 || n === 1) {
      return n;
    } else {
      return fib(n - 1) + fib(n - 2);
    }
  }
  
  const readline = require('readline');
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  rl.question('Por favor, insira a posição: ', (position) => {
    const pos = parseInt(position);
    if (pos === 1) {
      console.log(`O ${pos}º número de Fibonacci é: ${fib(pos)}`);
    } else if (pos === 2) {
      console.log(`O ${pos}º número de Fibonacci é: ${fib(pos)}`);
    } else if (pos === 3) {
      console.log(`O ${pos}º número de Fibonacci é: ${fib(pos)}`);
    } else {
      console.log(`O ${pos}º número de Fibonacci é: ${fib(pos)}`);
    }
    rl.close();
  });