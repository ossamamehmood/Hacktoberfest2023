var fahreinheitElement = document.getElementById("fahrenheit");
var celsiusElement = document.getElementById("celsius");
var kelvinElement = document.getElementById("kelvin");


function fromFahrenheitToOther(f){
    f = parseFloat(f);
    celsiusElement.value = (f-32)/1.8;
    kelvinElement.value = ((f-32)/1.8)+273.15;
}

function fromCelsiusToOthers(c){
    c = parseFloat(c);
    fahreinheitElement.value = (c*1.8)+32;
    kelvinElement.value =c+273.15;
}
function fromKelvinToOther(k){
    k = parseFloat(k);
    fahreinheitElement.value = ((k-273.15)*1.8)+32;
    celsiusElement.value = k-273.15;

}