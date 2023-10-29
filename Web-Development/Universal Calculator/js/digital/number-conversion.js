var binary_element = document.getElementById("binary");
var octal_element = document.getElementById("octal");
var decimal_element = document.getElementById("decimal");
var hexadecimal_element = document.getElementById("hexadecimal");



function fromBinaryToOther(num){
    num = parseInt(num,2);
    
    
    octal_element.value = num.toString(8);
    decimal_element.value = num.toString(10);
    hexadecimal_element.value = num.toString(16);
}
function fromOctalToOthers(num){
    num = parseInt(num,8);
    
    binary_element.value = num.toString(2);
    decimal_element.value = num.toString(10);
    hexadecimal_element.value = num.toString(16);
    
}
function fromDecimalToOther(num){
    num = parseInt(num,10);
    
    binary_element.value = num.toString(2);
    octal_element.value = num.toString(8);
    hexadecimal_element.value = num.toString(16);

}
function fromHexadecimalToOther(num){
    num = parseInt(num,16);
    
    binary_element.value = num.toString(2);
    octal_element.value = num.toString(8);
    decimal_element.value = num.toString(10);
}