/*======================================== Multiplication Table =============================================================
Program: JavaScript Program to Display the Multiplication Table 
Author: Mubashir Angathil
=============================================================================================================================*/

/**
 * Displays the multiplication table for a given number up to a specified limit.
 * @param {object} config - Configuration object with 'number' and 'limit' properties.
 */
const getMultiplicationTable = ({ number, limit }) => {
  if (number <= 0) {
    console.error(
      "Error: The multiplication factor must be a positive number greater than 0"
    );
    return;
  }

  for (let i = 1; i <= limit; i++) {
    let multiplication = i * number;
    console.log(`${i} x ${number} => ${multiplication}`);
  }
};

/**
 * Main function to demonstrate the multiplication table program.
 */
const main = () => {
  const number = 100;
  const limit = 10;

  console.log(
    `Multiplication Table for ${number} up to ${limit}\n=====================================`
  );

  getMultiplicationTable({ number, limit });
};

// Call the main function to execute the program
main();
