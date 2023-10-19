function computerChoice() {
  const choices = ["stone", "paper", "scissors"];
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function determineWinner(user, computer) {
  if (user === computer) {
    return "It's a draw!";
  } else if (
    (user === "stone" && computer === "scissors") ||
    (user === "paper" && computer === "stone") ||
    (user === "scissors" && computer === "paper")
  ) {
    return "You win!";
  } else {
    return "Computer wins!";
  }
}

function playGame(userChoice) {
  const computer = computerChoice();
  const result = determineWinner(userChoice, computer);
  return `You chose ${userChoice}, computer chose ${computer}. ${result}`;
}

// Example usage:
const userChoice = "stone"; // Replace with "stone", "paper", or "scissors"
console.log(playGame(userChoice));
