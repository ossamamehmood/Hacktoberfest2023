var area = document.getElementById("area");
var perimeter = document.getElementById("perimeter");
var diagonal = document.getElementById("diagonal");
var side = document.getElementById("side");

function fromAreaToOther(a){
    a = parseFloat(a);
    if(a < 0){
        alert("Length cannot be negative!");
        area.value = "";
        return;
    }
    var side_of_square = Math.sqrt(a) 
    side.value = side_of_square;
    perimeter.value = 4*side_of_square;
    diagonal.value = side_of_square*Math.sqrt(2);
}
function fromPerimeterToOther(pm){
    pm = parseFloat(pm);
    if(pm < 0){
        alert("Length cannot be negative!");
        perimeter.value = "";
        return;
    }
    var side_of_square = pm/4;
    side.value = side_of_square;
    diagonal.value = side_of_square*Math.sqrt(2);
    area.value = side_of_square*side_of_square;
}
function fromDiagonalToOther(q){
    q =  parseFloat(q);
    if(q < 0){
        alert("Length cannot be negative!");
        diagonal.value = "";
        return;
    }
    var side_of_square = q/Math.sqrt(2);
    side.value = side_of_square;
    perimeter.value = 4*side_of_square;
    area.value = side_of_square*side_of_square;
}
function fromSideToOther(s){
    s = parseFloat(s);
    if(s < 0){
        alert("Length cannot be negative!");
        side.value = "";
        return;
    }
    diagonal.value = s*Math.sqrt(2);
    area.value = s*s;
    perimeter.value = 4*s;    

}