setTimeout(function () {
  var carAnimition = document.getElementById("animition1");
  carAnimition.style.display = "none";
  var hiddenItem = document.getElementById("hiddenItem");
  hiddenItem.style.display = "inline-block";
}, 4000);

function buycars() {
  var services = document.getElementById("services").style;
  services.display = "block";
}

var cars = {
  hyundai: {
    Sonata: {
      image: "img/cars/hyundai/Sonata.jpg",
      name: "Sonata",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Tucson: {
      image: "img/cars/hyundai/tucson.webp",
      name: "Tucson",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Accent: {
      image: "img/cars/hyundai/Accent.avif",
      name: "Accent",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    SantaFe: {
      image: "img/cars/hyundai/SantaFe.png",
      name: "SantaFe",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
  },
  toyota: {
    Camry: {
      image: "img/cars/toyota/Camry.jpg",
      name: "Camry",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Corolla: {
      image: "img/cars/toyota/Corolla.png",
      name: "Corolla",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },

    Prius: {
      image: "img/cars/toyota/Prius.webp",
      name: "Prius",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Fortuner: {
      image: "img/cars/toyota/Fortuner.png",
      name: "Fortuner",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
  },
  honda: {
    Civic: {
      image: "img/cars/honda/Civic.jpg",
      name: "Civic",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    City: {
      image: "img/cars/honda/city.jpg",
      name: "City",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    BRV: {
      image: "img/cars/honda/br-v.webp",
      name: "BR-V",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Hybrid: {
      image: "img/cars/honda/Hybrid.webp",
      name: "CR-V Hybrid",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
  },
  suzuki: {
    Swift: {
      image: "img/cars/suzuki/swift.webp",
      name: "Swift",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Alto: {
      image: "img/cars/suzuki/Alto.jpg",
      name: "Alto",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Mehran: {
      image: "img/cars/suzuki/Mehran.jpg",
      name: "Mehran",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Carry: {
      image: "img/cars/suzuki/Carry.jpg",
      name: "Carry",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
  },
  kia: {
    Sportage: {
      image: "img/cars/kia/Sportage.png",
      name: "Sportage",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Sorento: {
      image: "img/cars/kia/Sorento.jpg",
      name: "Sorento",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Rio: {
      image: "img/cars/kia/Rio.jpg",
      name: "Rio",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
    Stinger: {
      image: "img/cars/kia/Stinger.webp",
      name: "Stinger",
      engine: "Smart Stream 2.5 MPi",
      door: "4 doors",
      FuelTank: "60 (Ltr.)",
      MaxPower: "132 (180)/6200",
      color: ["Black", "White", "Red"],
      price: "112 Lakh",
    },
  },
};

var company = document.getElementById("company");
var brand = document.getElementById("brand");
var allCars = document.getElementById("allCars");

brand.innerHTML = `<option value="">Choose a Car</option>`;

for (var key in cars) {
  company.innerHTML += `
  <option value="${key}">${key.toUpperCase()}</option>`;

  for (var key1 in cars[key]) {
    var carData = cars[key][key1];
    var colorDiv = "";
    for (var i = 0; i < carData.color.length; i++) {
      colorDiv += `
      <div id="divColor" style="background-color: ${carData.color[i]}"></div>
      `;
    }
    allCars.innerHTML += `
      <div class="card" style="width: 25rem">
      <img
        src="${carData.image}"
        class="card-img-top"
      />
      <div class="card-body">
      <span>${key.toUpperCase()}</span><h1 class="card-title">${
      carData.name
    }</h1>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">
          <img src="img/icons/engine.png" alt="" /> ${carData.engine}
        </li>
        <li class="list-group-item">
          <img src="img/icons/speed-meter.png" alt="" />${carData.MaxPower}
        </li>
        <li class="list-group-item">
          <img src="img/icons/car-door.png" alt="" />${carData.door}
        </li>
        <li class="list-group-item">
          <img src="img/icons/full-tank.png" alt="" />${carData.FuelTank}
        </li>
        <li class="list-group-item">
          <img src="img/icons/color.png" alt="" /><div id="flex">${colorDiv}</div>
        </li>
        <li class="list-group-item">
          <img src="img/icons/price.png" alt="" /> ${carData.price}
        </li>
      </ul>
    </div>
      `;
  }
}

function companyToBrand() {
  brand.innerHTML = `<option value="">Choose a Car</option>
  `;
  for (var key in cars[company.value]) {
    brand.innerHTML += `
    <option value="${key}" >${key.toUpperCase()}</option>
  `;
  }
}

var showAll = document.querySelector(".showAll");

function filterCars() {
  var featured = document.getElementById("featured").style;
  featured.display = "block";
  showAll.innerText = "SHOW ALL";

  var selectedCompany = company.value;
  var selectedBrand = brand.value;

  if (!selectedCompany && !selectedBrand) {
    allCars.innerHTML = "";
    for (var key in cars) {
      for (var key1 in cars[key]) {
        var carData = cars[key][key1];
        var colorDiv = "";
        for (var i = 0; i < carData.color.length; i++) {
          colorDiv += `
            <div id="divColor" style="background-color: ${carData.color[i]}"></div>
          `;
        }
        allCars.innerHTML += `
          <div class="card" style="width: 25rem">
            <img src="${carData.image}" class="card-img-top" />
            <div class="card-body">
              <span>${key.toUpperCase()}</span>
              <h1 class="card-title">${carData.name}</h1>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <img src="img/icons/engine.png" alt="" /> ${carData.engine}
              </li>
              <li class="list-group-item">
                <img src="img/icons/speed-meter.png" alt="" /> ${
                  carData.MaxPower
                }
              </li>
              <li class="list-group-item">
                <img src="img/icons/car-door.png" alt="" /> ${carData.door}
              </li>
              <li class="list-group-item">
                <img src="img/icons/full-tank.png" alt="" /> ${carData.FuelTank}
              </li>
              <li class="list-group-item">
                <img src="img/icons/color.png" alt="" />
                <div id="flex">${colorDiv}</div>
              </li>
              <li class="list-group-item">
                <img src="img/icons/price.png" alt="" /> ${carData.price}
              </li>
            </ul>
          </div>
        `;
      }
    }
  } else {
    if (selectedCompany && selectedBrand) {
      var carDetails = cars[selectedCompany][selectedBrand];
      var colorDiv = "";
      for (var i = 0; i < carDetails.color.length; i++) {
        colorDiv += `
          <div id="divColor" style="background-color: ${carDetails.color[i]}"></div>
        `;
      }
      allCars.innerHTML = `
        <div class="card" style="width: 25rem">
          <img src="${carDetails.image}" class="card-img-top" />
          <div class="card-body">
            <h1 class="card-title">${carDetails.name}</h1>
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">
              <img src="img/icons/engine.png" alt="" /> ${carDetails.engine}
            </li>
            <li class="list-group-item">
              <img src="img/icons/speed-meter.png" alt="" /> ${carDetails.MaxPower}
            </li>
            <li class="list-group-item">
              <img src="img/icons/car-door.png" alt="" /> ${carDetails.door}
            </li>
            <li class="list-group-item">
              <img src="img/icons/full-tank.png" alt="" /> ${carDetails.FuelTank}
            </li>
            <li class="list-group-item">
              <img src="img/icons/color.png" alt="" />
              <div id="flex">${colorDiv}</div>
            </li>
            <li class="list-group-item">
              <img src="img/icons/price.png" alt="" /> ${carDetails.price}
            </li>
          </ul>
        </div>
      `;
    } else {
      allCars.innerHTML = "Please select a company and a car model.";
    }
  }
}
