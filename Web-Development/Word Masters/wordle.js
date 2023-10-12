let guess = "",start= 0,correctLetters = 0,endGame = false
const correctWord = [];
const WordOfTheDay_URL = "https://words.dev-apis.com/word-of-the-day"
const validateWord_URl = "https://words.dev-apis.com/validate-word"
const letters = document.querySelectorAll(".letter")
function isLetter(letter) {
    return /^[a-zA-Z]$/.test(letter);
}
function addLetter(letter) {
    if(guess.length < 5) guess += letter;
    else guess = guess.slice(0,-1) + letter
}
function isEndOfWord() {
    return guess.length !== 0 && guess.length % 5 === 0
}
function startLoader(){
    document.querySelector(".spiral").style.visibility= "visible";
}
function stopLoader(){
    document.querySelector(".spiral").style.visibility = "hidden";
}
function updateBoard(){

    guess = guess.toUpperCase()
    let j = start;

    for(let i = 0; i < guess.length; i++){
        letters[j++].innerText = guess[i]
    }
    for(let i = j; i < 30;i++){
        letters[i].innerText =  " ";
    }
}
function updateLetters() {

    let correct = correctWord.slice()
    // update green letters first
    for (let i = start; i < start + 5; i++) {
        const currentLetter = letters[i].innerText
        let index = correct.indexOf(currentLetter)
        if (correct.includes(currentLetter) && index === i - start) {
            letters[i].style.backgroundColor = "darkgreen"
            correctLetters++;
        }
    }
    // add yellow and grey
    for (let i = start; i < start + 5; i++) {

        const currentLetter = letters[i].innerText
        letters[i].style.color = "white"
        let index = correct.indexOf(currentLetter)

        if (correct.includes(currentLetter)) {
            if(index !== i-start){
                letters[i].style.backgroundColor = "goldenrod"
            }
            correct[index] = ""
        } else {
            letters[i].style.backgroundColor = "#888"
        }
    }
    start += 5;
    guess = "";
}
function alertWrongWord() {
    for(let i = start;i < start+5;i++){
        letters[i].style.borderColor =  "red"
        setTimeout(function (){
            letters[i].style.borderColor = "#ccc"
        },500)
    }
}
function titleAnimation() {
    document.querySelector(".brand")
        .style.animation = "rainbow 4s infinite linear"
}
function checkWinOrLose() {
    if(correctLetters === 5){
        endGame = true
        alert("you win")
        titleAnimation();
    }
    else if(start > 25){
        endGame = true
        alert("you lose the word was, " + correctWord.join(''))
    }
    correctLetters = 0
}
function checkKey(letter) {
    if(isLetter(letter) ){
        addLetter(letter);
    }
    else if(letter === 'Backspace') {
        guess = guess.substring(0, guess.length - 1)
    }
    else if(isEndOfWord() && letter === 'Enter'){
        isValidWord().then(valid =>{
            if(valid){
                updateLetters()
                checkWinOrLose()
            }
            else {
                alertWrongWord()
            }
        })
    }
    updateBoard();
}
function init(){
    document
        .addEventListener('keydown',function (event){
           if(!endGame)
               checkKey(event.key)
        })
}
async function isValidWord(){
    startLoader()
    const promise = await fetch(validateWord_URl,{
        method :"POST", body: JSON.stringify({word : guess})
    })
    const response = await promise.json()
    stopLoader()
    return response.validWord
}

async function getWordOfTheDay(){
    startLoader()
    const promise = await fetch(WordOfTheDay_URL)
    const processedResponse = await  promise.json()
    const word = processedResponse.word.toUpperCase()
    for(let i = 0; i < word.length;i++){
        correctWord.push(word[i])
    }

    stopLoader()
}
getWordOfTheDay();
init();