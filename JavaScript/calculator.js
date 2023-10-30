//Making Simple-Calculator Using Js
function basicCalculator() {
    while (true) {
      // Display a menu of options
      const choice = prompt("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit");
  
      // Convert the choice to a number
      const option = parseInt(choice);
  
      if (isNaN(option)) {
        alert("Invalid choice. Please enter a number.");
        continue;
      }
  
      if (option === 5) {
        alert("Calculator closed.");
        break;
      }
  
      if (option < 1 || option > 4) {
        alert("Invalid choice. Please select a valid option (1-4).");
        continue;
      }
  
      // Get user input for two numbers
      const num1 = parseFloat(prompt("Enter the first number:"));
      const num2 = parseFloat(prompt("Enter the second number:"));
  
      if (isNaN(num1) || isNaN(num2)) {
        alert("Invalid input. Please enter valid numbers.");
        continue;
      }
  
      // Perform the selected operation
      let result;
      switch (option) {
        case 1:
          result = num1 + num2;
          break;
        case 2:
          result = num1 - num2;
          break;
        case 3:
          result = num1 * num2;
          break;
        case 4:
          if (num2 === 0) {
            alert("Division by zero is not allowed.");
            continue;
          }
          result = num1 / num2;
          break;
      }
  
      // Display the result
      alert("Result: " + result);
    }
  }
  
  basicCalculator();
  
