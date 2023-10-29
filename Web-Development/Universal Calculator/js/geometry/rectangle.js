var area = document.getElementById("area");
var perimeter = document.getElementById("perimeter");
var diagonal = document.getElementById("diagonal");
var sideA = document.getElementById("sideA");
var sideB = document.getElementById("sideB");
function AreaAndSideA(area,sideA){
    /*b = A / a
    P = 2a + 2b
    p = q = √(a2 + b2) */
    area.value = area;
    sideA.value = sideA;
    var sideB_value = area/sideA;
    sideB.value = sideB_value;
    var per = 2*sideA + 2*sideB_value;
    perimeter.value = per;
    var q = (sideA*sideA)+(sideB_value*sideB_value);
    diagonal.value = Math.sqrt(q);
    
}

function AreaAndSideB(area,sideB){
    /**
     a = A / b
    P = 2a + 2b
    p = q = √(a2 + b2)
     */
    
    var sideA__ = area/sideB;
    sideA.value = sideA__;
    perimeter.value = 2*sideA__ + 2*sideB;
    diagonal.value = Math.sqrt((Math.pow(sideA__,2)) + ( Math.pow(sideB,2) ));
}

function sideAAndSideB(sideA,sideB){
    /**
     A = ab
    P = 2a + 2b
    p = q = √(a2 + b2)
     */
    var area__ = sideA*sideB; 
    area.value = area__;
    perimeter.value = (2*sideA) + (2*sideB);
    diagonal.value = Math.sqrt((Math.pow(sideA,2)) + (Math.pow(sideB,2)));

}

function PerimeterAndSideA(perimeter,sideA){
    /* 
    b = (P - 2a) / 2
    A = ab
    p = q = √(a2 + b2)
    */
   if(perimeter < (2*sideA)){
       alert("Perimeter must be > 2 x Side");
       return;
   }
   var sideB__ = (perimeter-(2*sideA))/2; 
   sideB.value = sideB__;
   area.value = sideA*sideB__;
   diagonal.value = Math.sqrt((Math.pow(sideA,2)) + (Math.pow(sideB__,2)));

}
function perimeterAndsideB(perimeter,sideB){
    /**
     a = (P - 2b) / 2
    A = ab
    p = q = √(a2 + b2)
     */
    if(perimeter < (2*sideB)){
        alert("Perimeter must be > 2 x side");
        return;
    }
    var sideA__ = (perimeter-(2*sideB)) / 2; 
    sideA.value = sideA__;
    area.value = sideA__*sideB;
    diagonal.value = Math.sqrt((Math.pow(sideA__,2)) + (Math.pow(sideB,2)));

}
function diagonalAndSideA(diagonal,sideA){
    /**
     b = √(p2 - a2)
    A = ab
    P = 2a + 2b
     */
    if(diagonal < sideA){
        alert("Invalid Input: q < a");
   }
    var sideB__ = Math.sqrt( (Math.pow(diagonal,2)) - (Math.pow(sideA,2)) );
    sideB.value  = sideB__;
    area.value = sideA*sideB__;
    perimeter.value = (2*sideA) + (2*sideB__);
}
function diagonalAndSideB(diagonal,sideB){
    /*
    a = √(p2 - b2)
    A = ab
    P = 2a + 2b
    */
   if(diagonal < sideB){
        alert("Invalid Input: q < b");
   }
    var sideA__ = Math.sqrt((Math.pow(diagonal,2)) - (Math.pow(sideB,2)));
    sideA.value = sideA__;
    area.value = sideA__*sideB;
    perimeter.value = (2*sideA__) + (2*sideB);
}

function isNotEmpty(element_val,element_val_2){
    var test = (element_val != "" & element_val_2 != "") & (element_val > 0 & element_val_2 > 0);
    if(test == 1){
        return true;
    }
    else{
        return false;
    }
}

function calculate(){
   if(isNotEmpty(area.value,sideA.value)){
    alert(`A = ${area.value} a = ${sideA.value}`);
    AreaAndSideA(area.value,sideA.value);
    
   }
   else if(isNotEmpty(area.value,sideB.value)){
    alert(`A = ${area.value} b = ${sideB.value}`);
    AreaAndSideB(area.value,sideB.value);
   }
   else if(isNotEmpty(sideA.value,sideB.value)){
    alert(`A = ${sideA.value} b = ${sideB.value}`);
    sideAAndSideB(sideA.value,sideB.value);
   }
   else if(isNotEmpty(perimeter.value,sideA.value)){
    alert(`P = ${perimeter.value} a = ${sideA.value}`);
    PerimeterAndSideA(perimeter.value,sideA.value);
   }
   else if(isNotEmpty(perimeter.value,sideB.value)){
    alert(`A = ${perimeter.value} a = ${sideB.value}`);
    perimeterAndsideB(perimeter.value,sideB.value);
   }
   else if(isNotEmpty(diagonal.value,sideA.value)){
    alert(`q = ${diagonal.value} a = ${sideA.value}`);
    diagonalAndSideA(diagonal.value,sideA.value);
   }
   else if(isNotEmpty(diagonal.value,sideB.value)){
    alert(`q = ${diagonal.value} b = ${sideB.value}`);
    diagonalAndSideB(diagonal.value,sideB.value);
   }
   else{
       alert("Calculation not allowed!");
       clear();
   }

}
function clear(){
    area.value =  "";
    perimeter.value = "";
    diagonal.value =  "";
    sideA.value =   "";
    sideB.value =  "";
}
document.getElementById("submit-button").addEventListener("click",calculate);
document.getElementById("clear-button").addEventListener("click",clear);