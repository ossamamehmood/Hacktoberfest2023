function generateRandomNumber() {
    // gen a random number
    const randomNumber = Math.floor(Math.random() * 100000) + 1;

    // display the random num
    const resultElement = document.getElementById("result");
    resultElement.innerHTML = "Your random number is: " + randomNumber + "!";
}