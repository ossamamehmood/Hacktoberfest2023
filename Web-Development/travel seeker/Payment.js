

function getnextpage(){
	location.href="OTP.html"
}


let productCont = document.getElementById("right-container1");

let cartLS = JSON.parse(localStorage.getItem("selectedHotel"));

let finalamt = localStorage.getItem("finalAmount");

	function displayProductsData() {
		 let mainContainer = document.getElementById('right-container1')
		mainContainer.innerHTML="";
		
		
			

			let imag = document.createElement("div");
			imag.setAttribute("id","imag")

			let dataAll = document.createElement("div");
			dataAll.setAttribute("id","dataAll")

			let hotelImg = document.createElement("img");
			hotelImg.src = cartLS.image;
			hotelImg.alt = 'Hotel image'
			hotelImg.classList = 'Hotel-img'

			let hotelName = document.createElement("h2");
			hotelName.innerText = cartLS.name;
			
			let hotelAddr = document.createElement("p")
			hotelAddr.innerText = cartLS.address;
			hotelAddr.classList = "Hotel-add"

			let hotelservc = document.createElement("p")
			hotelservc.innerText = "Free WiFi";
			
			let hotelservc2 = document.createElement("p")
			hotelservc2.innerText = "Free BreakFast";
			
			imag.append(hotelImg)
			dataAll.append(hotelName, hotelAddr, hotelservc,hotelservc2);

			//productCard.append(hotelImg, hotelName, hotelAddr, hotelservc);

			mainContainer.append(imag,dataAll);
		
	}
	document.getElementById("amt").textContent = finalamt;
	document.getElementById("disc").textContent = finalamt * .12
	document.getElementById("tmt").textContent= parseInt(finalamt)+ (finalamt * .12);
	displayProductsData()


	



























// let Hoteldata = []

// 		fetch('http://localhost:3000/Hoteldata').then(function(response) {
// 			return response.json()
// 		}).then(function(response) {
// 			Hoteldata = response
// 			console.log(Hoteldata)
// 			displayProductsData(Hoteldata)
// 		}).catch(function(error) {
// 			console.log(error)
// 		})

		
// 		let totalprice=0;
//         function displayProductsData(Hoteldata) {
// 			let mainContainer = document.getElementById('right-container1')
// 			mainContainer.innerHTML="";
			
// 			Hoteldata.forEach(function(product) {
// 				// totalprice.innerHTML = product.amount;
// 				// console.log("Price:",totalprice)

// 				// let productCard = document.createElement("div");
// 				// productCard.classList = 'mini-container1'

// 				let imag = document.createElement("div");
// 				imag.setAttribute("id","imag")

// 				let dataAll = document.createElement("div");
// 				dataAll.setAttribute("id","dataAll")

// 				let hotelImg = document.createElement("img");
// 				hotelImg.src = product.image;
// 				hotelImg.alt = 'Hotel image'
// 				hotelImg.classList = 'Hotel-img'

// 				let hotelName = document.createElement("h3");
// 				hotelName.innerText = product.tittle;
				
// 				let hotelAddr = document.createElement("p")
// 				hotelAddr.innerText = product.address;

// 				let hotelservc = document.createElement("p")
//                 hotelservc.innerText = product.service;
				
// 				imag.append(hotelImg)
// 				dataAll.append(hotelName, hotelAddr, hotelservc);

// 				//productCard.append(hotelImg, hotelName, hotelAddr, hotelservc);

// 				mainContainer.append(imag,dataAll);
// 			})
// 		}
// 		// console.log(totalprice)
//		 document.getElementById("amt").textContent = totalprice;
		
// 		// document.getElementById("disc").textContent = totalprice - Number(totalprice *0.1);

// function getnextpage(){
// 	location.href="OTP.html"
// }