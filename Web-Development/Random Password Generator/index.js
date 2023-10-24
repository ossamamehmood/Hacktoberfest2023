const passwordbox = document.getElementById("password");
const btn = document.getElementById("gen");
const length = document.getElementById("length");
const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lowercase = "abcdefghijklmnopqrstuvwxyz";
const number = "0123456789";
const symbol = "!@#$%^&*(){}[]_-+=**/<>,.?/";
const alChars = uppercase + lowercase + number + symbol;
const upperinput = document.getElementById("upperCase");
const lowerinput = document.getElementById("lowerCase");
const numberinput = document.getElementById("numBer");
const symbolinput = document.getElementById("Symbols");

function genpass() {
  let charSet = "";

  if (upperinput.checked) {
    charSet += uppercase;
  }

  if (lowerinput.checked) {
    charSet += lowercase;
  }

  if (numberinput.checked) {
    charSet += number;
  }

  if (symbolinput.checked) {
    charSet += symbol;
  }

  if (charSet.length === 0) {
    passwordbox.value = "Select at least one character set.";
    return;
  }

  let password = "";

  while (password.length < length.value) {
    password += charSet[Math.floor(Math.random() * charSet.length)];
  }

  passwordbox.value = password;
}

btn.addEventListener("click", () => {
  genpass();
});

function copy() {
  passwordbox.select();
  document.execCommand("copy");
}
