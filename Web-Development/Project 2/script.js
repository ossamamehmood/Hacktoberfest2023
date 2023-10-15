var button = document.getElementById("button")
var button1 = document.getElementById("button1")

var input = document.getElementById("input");

const palindrome = (value)=>{
    return value.split('').reverse().join('');
}


button.addEventListener("click",()=>{
    var value = input.value;
    var result = palindrome(value);
    if(result === value){
        // console.log(true);
        document.getElementById("result").innerHTML="Palindrome"
    }
    else{
        // console.log(false);
        document.getElementById("result").innerHTML="Not Palindrome"
    }

})
button1.addEventListener("click",()=>{
    input.value = "";
    document.getElementById("result").innerHTML="";
})


