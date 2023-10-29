var square_meter_element = document.getElementById("square-meter");
var square_km_element = document.getElementById("square-kilometer");
var square_cm_element = document.getElementById("square-centimeter");
var square_mm_element = document.getElementById("square-milimeter");
var square_micro_element = document.getElementById("square-micrometer");
var hectare_element = document.getElementById("hectare");
var square_mile_element = document.getElementById("square-mile");
var square_yard_element = document.getElementById("square-yard");
var square_foot_element = document.getElementById("square-foot");
var square_inch_element = document.getElementById("square-inch");
var acre_element = document.getElementById("acre");

function is_valid(element,value){
    if(value < 0){
        alert("Cannot accept negative numbers!");
        element.value = "";
        return false;

    }
    else{
        return true;
    }
}

function fromSquareMeterToOther(num){
    num = parseFloat(num);
    if(is_valid(square_meter_element,num)){
    square_km_element.value = num * 0.000001;
    square_cm_element.value =  num * 10000;
    square_mm_element.value = num * 1000000;
    square_micro_element.value = num * 1000000000000;
    hectare_element.value = num * 0.0001;
    square_mile_element.value = num * 3.861018768E-7;
    square_yard_element.value = num * 1.1959900463;
    square_foot_element.value = num * 10.763910417;
    square_inch_element.value = num * 1550.0031;
    acre_element.value = num * 0.0002471054;
    }
}
function fromSquareKilometerToOthers(num){
    num = parseFloat(num);
    if(is_valid(square_km_element,num)){
    square_meter_element.value = num * 1000000;
    square_cm_element.value =  num * 10000000000;
    square_mm_element.value = num * 1000000000000;
    square_micro_element.value = num * 1000000000000000000;
    hectare_element.value = num * 100;
    square_mile_element.value = num * 0.3861018768;
    square_yard_element.value = num * 1195990.0463;
    square_foot_element.value = num * 10763910.417;
    square_inch_element.value = num * 1550003100;
    acre_element.value = num * 247.10538147;
    }
}
function fromSquareCentimeterToOther(num){
    num = parseFloat(num);
    if(is_valid(square_cm_element,num)){
    square_meter_element.value = num * 0.0001;
    square_km_element.value =  num * 1.E-10;
    square_mm_element.value = num * 100;
    square_micro_element.value = num * 100000000;
    hectare_element.value = num * 1.E-8;
    square_mile_element.value = num * 3.861018768E-11;
    square_yard_element.value = num * 0.000119599;
    square_foot_element.value = num * 0.001076391;
    square_inch_element.value = num * 0.15500031;
    acre_element.value = num * 2.471053814E-8;
}
}
function fromSquareMilimeterToOther(num){
    num = parseFloat(num);
    if(is_valid(square_mm_element,num)){
    square_meter_element.value = num * 0.000001;
    square_km_element.value =  num * 1.E-12;
    square_cm_element.value = num * 0.01;
    square_micro_element.value = num * 1000000;
    hectare_element.value = num * 9.999999999E-11;
    square_mile_element.value = num * 3.861018768E-13;
    square_yard_element.value = num * 0.000001196;
    square_foot_element.value = num * 0.0000107639;
    square_inch_element.value = num * 0.0015500031;
    acre_element.value = num * 2.471053814E-10;
}
}
function fromSquareMicrometerToOthers(num){
    num = parseFloat(num);
    if(is_valid(square_micro_element,num)){
    square_meter_element.value = num * 1.E-12;
    square_km_element.value =  num * 1.E-18;
    square_cm_element.value = num * 9.999999999E-9;
    square_mm_element.value = num * 0.000001;
    hectare_element.value = num * 1.E-16;
    square_mile_element.value = num * 3.861018768E-19;
    square_yard_element.value = num * 1.195990046E-12;
    square_foot_element.value = num * 1.076391041E-11;
    square_inch_element.value = num * 1.5500031E-9;
    acre_element.value = num * 2.471053814E-16;
}
}
function fromHectarToOthers(num){
    num = parseFloat(num);
    if(is_valid(hectare_element,num)){
    square_meter_element.value = num * 10000;
    square_km_element.value =  num * 0.01;
    square_cm_element.value = num * 100000000;
    square_mm_element.value = num * 10000000000;
    square_micro_element.value = num * 10000000000000000;
    square_mile_element.value = num * 0.0038610188;
    square_yard_element.value = num * 11959.900463;
    square_foot_element.value = num * 107639.10417;
    square_inch_element.value = num * 15500031;
    acre_element.value = num * 2.4710538147;
}
}
function fromSquareMileToOthers(num){
    num = parseFloat(num);
    if(is_valid(square_mile_element,num)){
    square_meter_element.value = num * 2589990;
    square_km_element.value =  num * 2.58999;
    square_cm_element.value = num * 25899900000;
    square_mm_element.value = num * 2589990000000;
    square_micro_element.value = num * 2589990000000000000;
    hectare_element.value = num *258.999;
    square_yard_element.value = num * 3097602.26;
    square_foot_element.value = num * 27878420.34;
    square_inch_element.value = num * 4014492529;
    acre_element.value = num * 640.00046695;
}
}
function fromSquareYardToOthers(num){
    num = parseFloat(num);
    if(is_valid(square_yard_element,num)){
    square_meter_element.value = num * 0.83612736;
    square_km_element.value =  num * 8.3612736E-7;
    square_cm_element.value = num * 8361.2736;
    square_mm_element.value = num * 836127.36;
    square_micro_element.value = num * 836127360000;
    hectare_element.value = num * 0.0000836127;
    square_mile_element.value = num * 3.228303429E-7;
    square_foot_element.value = num * 9;
    square_inch_element.value = num * 1296;
    acre_element.value = num * 0.0002066116;
}
}
function fromSquareFootToOthers(num){
    num = parseFloat(num);
    if(is_valid(square_foot_element,num)){
    square_meter_element.value = num * 0.09290304;
    square_km_element.value =  num * 9.290304E-8;
    square_cm_element.value = num * 929.0304;
    square_mm_element.value = num * 92903.04;
    square_micro_element.value = num * 92903040000;
    hectare_element.value = num * 0.0000092903;
    square_mile_element.value = num * 3.58700381E-8;
    square_yard_element.value = num * 0.1111111111;
    square_inch_element.value = num * 144;
    acre_element.value = num * 0.0000229568;
}
}
function fromSquareInchToOthers(num){
    num = parseFloat(num);
    if(is_valid(square_inch_element,num)){
    square_meter_element.value = num * 0.00064516;
    square_km_element.value =  num * 6.4516E-10;
    square_cm_element.value = num * 6.4516;
    square_mm_element.value = num * 645.16;
    square_micro_element.value = num * 645160000;
    hectare_element.value = num * 6.4516E-8;
    square_mile_element.value = num * 2.490974868E-10;
    square_yard_element.value = num * 0.0007716049;
    square_foot_element.value = num * 0.0069444444;
    acre_element.value = num * 1.594225079E-7;
}
}
function fromAcreToOthers(num){
    num = parseFloat(num);
    if(is_valid(acre_element,num)){
    square_meter_element.value = num * 4046.8564224;
    square_km_element.value =  num * 0.0040468564;
    square_cm_element.value = num * 40468564.224;
    square_mm_element.value = num * 4046856422.4;
    square_micro_element.value = num * 4046856422400000;
    hectare_element.value = num * 0.4046856422;
    square_mile_element.value = num * 0.0015624989;
    square_yard_element.value = num * 4840;
    square_foot_element.value = num * 43560;
    square_inch_element.value = num * 6272640;
}
}
/*Author: Shaikh Sajid
*/