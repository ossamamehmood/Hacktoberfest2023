

// let setData={
//     hotelName: "Royal Palace",
//           price: 1550,
//           rating: 3,
//           address: "Kajari Road, Chomu Pulia Road, Jaipur, Rajasthan",
//           city:"jaipur"
// }



// document.getElementById("Mumbai-btn").addEventListener("click",deleteMum);
// function deleteMum(){
//     document.getElementById("Mumbai-input").value="";
//  }

// localStorage.setItem("CurrentHotel",JSON.stringify(setData));


let data=JSON.parse(localStorage.getItem("selectedHotel"))

// console.log(data.rating)
let querry="jaipur"

let gmap=document.getElementById("gmap_canvas")
let gmap1=document.getElementById("gmap_canvas1")
// gmap.src=`https://api.openweathermap.org/data/2.5/weather?q=${querry}&appid=c5f7cb74d66a1bd017f2be6cb3dde82f`
fetchData()
async function fetchData(){
    try{


        gmap.src=`https://maps.google.com/maps?q=${querry}=&output=embed`
        gmap1.src=`https://maps.google.com/maps?q=${querry}=&output=embed`
       

    }catch(err){
        console.log(err);
    }
}
let baseprice=data.price;
document.getElementById("a-price").innerText=`Rs. ${baseprice}`;

pricesfun()

function pricesfun(){
    let qty1=document.getElementById("a-addmore1").value
    let qty2=document.getElementById("a-addmore2").value
    let qty3=document.getElementById("a-addmore3").value

let beforeprice1=document.getElementById("beforeprice1")
let afterprice1=document.getElementById("afterprice1")
let beforeprice2=document.getElementById("beforeprice2")
let afterprice2=document.getElementById("afterprice2")

let beforeprice3=document.getElementById("beforeprice3")
let afterprice3=document.getElementById("afterprice3")

afterprice1.innerText=qty1*baseprice;
beforeprice1.innerText=qty1*afterprice1.innerText*1.5;
afterprice2.innerText=qty2*(baseprice/1+1000);
beforeprice2.innerText=qty2*(afterprice2.innerText*1.5);
afterprice3.innerText=qty3*(baseprice/1+2000);
beforeprice3.innerText=qty3*(afterprice3.innerText*1.5);
}



let hotelName=data.name;
document.getElementById("a-HotelName").innerText=hotelName;

let hoteladd=data.address;
document.getElementById("a-HotelAdd").innerText=hoteladd;

let hotelRating=`${data.rating} Very good`
document.getElementById("a-rating").innerText=hotelRating;

// let price=`${data.price} Very good`
// document.getElementById("a-rating").innerText=hotelRating;




function paymentpage1(){
   let price= document.getElementById("afterprice1").innerText
//    alert(price);
    localStorage.setItem("finalAmount",price)
    location.href="Payment.html"
}

function paymentpage2(){
    let price= document.getElementById("afterprice2").innerText
    // alert(price);
    localStorage.setItem("finalAmount", price);
    //  localStorge.setItem("finalAmount",price)
    location.href="Payment.html"
 }
 
function paymentpage3(){
    let price= document.getElementById("afterprice3").innerText

    // alert(price);
     localStorage.setItem("finalAmount",price)
     location.href="Payment.html"
 }

// document.querySelector("#a-booknowbtn").addEventListener







// afterprice2.textContent=qty*afterprice1/1000*1000+1000