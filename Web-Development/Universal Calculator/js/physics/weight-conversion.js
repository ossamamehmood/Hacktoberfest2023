/*Elements*/

var pounds_element = document.getElementById("pounds");
var gram_element = document.getElementById("grams");
var kilogram_element = document.getElementById("kilogram");
var ounce_element = document.getElementById("ounce");
var stone_element = document.getElementById("stone");
var carat_element = document.getElementById("carat");
var miligram_element = document.getElementById("miligram");
var metricTonElement = document.getElementById("metric-ton");
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
/*from pounds to other conversions*/
function fromPoundsToOther(pounds){
  pounds = parseFloat(pounds);
  if(is_valid(pounds_element,pounds)){
  gram_element.value = pounds / 0.0022046;   //pounds to gram
  kilogram_element.value = pounds/2.2046;    //pounds to kilogram
  ounce_element.value = pounds*16;         //to ounces
  stone_element.value = pounds*0.071429;     //to stone
  carat_element.value = pounds*2267.96;
  miligram_element.value = pounds*453592;
  metricTonElement.value = pounds*0.000453592;
}
}

/*from Grams to other conversions*/
function fromGramToOthers(gram){
  gram = parseFloat(gram);
  if(is_valid(gram_element,gram)){
  pounds_element.value = gram*0.0022046;  //to pounds
  kilogram_element.value = gram/1000;  //to kg
  ounce_element.value = gram*0.035274;     //to ounce
  stone_element.value = gram*0.00015747;     //to stone
  carat_element.value = gram*5;
  miligram_element.value = gram*1;
  metricTonElement.value = gram*0.000001;
  }
}

/*from kg to other conversions*/
function fromKilogramToOther(kg){
  kg = parseFloat(kg);
  if(is_valid(kilogram_element,kg)){
  pounds_element.value = kg*2.2046; //to pounds
  gram_element.value = kg*1000;       //to grams
  ounce_element.value = kg*35.274;    //to ounces
  stone_element.value = kg*0.1574;    //to stone
  carat_element.value =  kg*0.0283495;
  miligram_element.value = kg*1000000;
  metricTonElement.value = kg*0.001;
}
}
/*from Ounces To others*/
function fromOuncesToOther(oz){
  oz = parseFloat(oz);
  if(is_valid(ounce_element,oz)){
  pounds_element.value = oz*0.0625;     //to pounds
  gram_element.value = oz/0.035274;       //to grams
  kilogram_element.value = oz/35.274;     //to kg
  stone_element.value = oz*0.0044643;       //to stone
  carat_element.value = oz*141.7475;          //to carat
  miligram_element.value = oz*28349.5;          //to miligram
  metricTonElement.value = oz*35.273990723;
}
}
/*from stone to others*/
function fromStoneToOthers(st){
  st = parseFloat(st);
  if(is_valid(stone_element,st)){
  pounds_element.value = st*14;           //to pounds
  gram_element.value = st/0.00015747;       //to grams
  kilogram_element.value = st/0.15747;        //to kg
  ounce_element.value = st*224;           //ounce
  carat_element.value = st*31751.47;        //to carat
  miligram_element.value = st/0.00000015747;      //to miligram
  metricTonElement.value = st/157.4730;
}
}
/*From carat to others */
function fromCaratToOthers(ct){
    ct = parseFloat(ct);
    if(is_valid(carat_element,ct)){
    pounds_element.value = ct*0.0004409249;       //to pounds
    gram_element.value = ct*0.2;              //to grams
    kilogram_element.value = ct*0.0002;       //to kg
    ounce_element.value = ct*0.0070547981;  //to ounce
    stone_element.value = ct / 31751.47;        //to stone
    miligram_element.value = ct*200;      //to mg
    metricTonElement.value = ct*2.E-7;
  }
}
/*from miligram to other conversions*/
function fromMiligramToOthers(mg){
  mg = parseFloat(mg);
  if(is_valid(miligram_element,mg)){
  pounds_element.value = mg*0.0000022046;     //to pounds
  gram_element.value = mg*0.001;          //to grams
  kilogram_element.value = mg*0.000001;       //to kg
  ounce_element.value = mg*0.000035274;     //to ounce
  stone_element.value = mg * 0.00000015747;     //to stone
  carat_element.value = mg*0.005;           //to carat
  metricTonElement.value = mg*9.999999999E-10;
}
}
function fromMetricTonToOthers(mt){
  mt = parseFloat(mt);
  if(is_valid(metricTonElement,mt)){
  pounds_element.value = mt*2204.6244202;     //to pounds
  gram_element.value = mt*1000000;          //to grams
  kilogram_element.value = mt*1000;       //to kg
  ounce_element.value = mt*35273.990723;     //to ounce
  stone_element.value = mt*157.473;     //to stone
  carat_element.value = mt*5000000;           //to carat
  miligram_element.value = mt*1000000000;
}
}