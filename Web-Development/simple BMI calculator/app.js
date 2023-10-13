const height = document.getElementById("height");
const weight = document.getElementById("weight");
const button = document.getElementById("button");
const app = document.getElementById("app");

let BmiValuedocument = document.createElement("h2"); //creates an element to store output BMI
BmiValuedocument.classList.add("output"); //add a class name of output
let clearButton = document.createElement("button"); //create a button to vlean the output
clearButton.classList.add("button"); //add a class name of button
clearButton.innerText = "Clear";

clearButton.addEventListener("click", () => {
  app.removeChild(BmiValuedocument); //removes the output
});

//when the button is clicked ......
button.addEventListener("click", () => {
  let heightValue = parseInt(height.value); //converts height string to an integer
  let weightValue = parseInt(weight.value); //converts height string to an integer
  let BMI = weightValue / (heightValue / 100) ** 2;

  app.appendChild(clearButton);
  if (isNaN(BMI) || BMI == 0) {
    BmiValuedocument.innerText =
      "Invalid: You Must add both your height and weight!";
    app.appendChild(BmiValuedocument);
  } else if (BMI <= 18.5) {
    BmiValuedocument.innerHTML =
      'Your <span style="color:black"> BMI </span> value  is : ' +
      ` <span style="color:black">${BMI.toFixed(1)}</span>` +
      ' .Your BMI value falls within the <i style="color:red">underweight range</i>.';
    app.appendChild(BmiValuedocument);
  } else if (BMI <= 22.9) {
    BmiValuedocument.innerHTML =
      'Your <span style="color:black"> BMI </span> value  is : ' +
      ` <span style="color:black">${BMI.toFixed(1)}</span>` +
      ' .Your BMI value falls within the <i style="color:green"> Healthy range</i>.';
    app.appendChild(BmiValuedocument);
  } else if (BMI <= 24.9) {
    BmiValuedocument.innerHTML =
      'Your <span style="color:black"> BMI </span> value  is : ' +
      ` <span style="color:black">${BMI.toFixed(1)}</span>` +
      ' .Your BMI value falls within the <i style="color:orange">overweight range</i>.';
    app.appendChild(BmiValuedocument);
  } else {
    BmiValuedocument.innerHTML =
      'Your <span style="color:black"> BMI </span> value  is : ' +
      ` <span style="color:black">${BMI.toFixed(1)}</span>` +
      ' .Your BMI value falls within the <i style="color:red">obese range</i>.';
    app.appendChild(BmiValuedocument);
  }
});
