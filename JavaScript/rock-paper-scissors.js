function computerPlay() {
  const choices = ["rock", "paper", "scissors"];
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function playRound(playerSelection, computerSelection) {
  playerSelection = playerSelection.toLowerCase();

  if (playerSelection === computerSelection) {
    return "It's a tie!";
  } else if (
    (playerSelection === "rock" && computerSelection === "scissors") ||
    (playerSelection === "scissors" && computerSelection === "paper") ||
    (playerSelection === "paper" && computerSelection === "rock")
  ) {
    return `You win! ${playerSelection} beats ${computerSelection}.`;
  } else {
    return `You lose! ${computerSelection} beats ${playerSelection}.`;
  }
}

function game() {
  let playerScore = 0;
  let computerScore = 0;
  let rounds = 5;

  for (let i = 0; i < rounds; i++) {
    const playerSelection = prompt("Enter your choice: rock, paper, or scissors");
    const computerSelection = computerPlay();
    console.log(playRound(playerSelection, computerSelection));

    if (playRound(playerSelection, computerSelection).includes("win")) {
      playerScore++;
    } else if (playRound(playerSelection, computerSelection).includes("lose")) {
      computerScore++;
    }
  }

  if (playerScore > computerScore) {
    console.log("Yayy! you won");
  } else if (computerScore > playerScore) {
    console.log("Oops! you lost");
  } else {
    console.log("It's a tie!");
  }
}

// Start the game
game();
