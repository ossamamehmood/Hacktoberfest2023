'use strict';

/// constructor function
// arrow function does not work in constructor function due to this keyword
const Person = function (firstName, birthYear) {
  // instance Properties
  this.firstName = firstName;
  this.birthYear = birthYear;
  // this will automatically return the object
  /// Never made function in constructor function
  //  this.calcAge=function(){
  //     console.log(2037-this.brithYear);
  //  }
};
// difference between regular and constructor function is that we call constructor function with new keyword
const jonas = new Person('Jonas', 1991);
console.log(jonas);
//  4 steps will be followed
// 1) new  {}empty object is created
// 2. function is called , this ={}
// 3. {} is linked to prototype
// 4. function automaticaaly return the empty objects {}

const matilda = new Person('Matilda', 2017);
const jack = new Person('Jack', 1975);
console.log(matilda);
console.log(jack);

/// In js we can also make object from constructor function
console.log(jonas instanceof Person);
/// static method
Person.Hey = function () {
  console.log('hey there 🤗');
  console.log(this); // point entire constructor function
};

Person.Hey();
// jonas.Hey();  // we can't call due it can't be inherited

/////// PotoTypes
console.log(Person.prototype);

/// making function
Person.prototype.clacAge = function () {
  console.log(2037 - this.birthYear);
};
/// any object has access to its properties and method of prototype
jonas.clacAge();
matilda.clacAge();

console.log(jonas.__proto__);
console.log(jonas.__proto__ === Person.prototype);

/// Person.prototype is not the prototype of person but its properties and methods can be accessed by its object
console.log(Person.prototype.isPrototypeOf(jonas));

///.prototypeOFLinkedObjects
/// not own property
// own property Directly attach or added in that function or class
Person.prototype.species = 'HomoSapiens';
console.log(jonas);
console.log(jonas.species);

console.log(jonas.hasOwnProperty('firstName'));
console.log(jonas.hasOwnProperty('species'));

//// for linkedin  post
// const person = {
//   myName: 'Syed Moazam',
//   introduce: function()  {
//     return `Hi this is ${this.myName}`;
//   },
// };
// const introducer =person.introduce.bind(person);
// console.log(introducer());
// //output  Hi this is Syed Moazam

console.log(jonas.__proto__);
console.log(jonas.__proto__.__proto__); // top of prototypw chain
console.log(jonas.__proto__.__proto__.__proto__); // null

console.log(Person.prototype.constructor);
console.dir(Person.prototype.constructor);

const arr = [9, 8, 4, 5, 3, 2, 3, 4, 2];
console.log(arr.__proto__); // prototypal inheritance
console.log(arr.__proto__ === Array.prototype);
console.log(arr.__proto__.__proto__); // object

// prototypal inheritance is very useful to reuse code
// just like Array.prototype.filter

// extending array
// adding method in array then all the array will inherit this method
Array.prototype.unique = function () {
  return [...new Set(this)];
};
console.log(arr.unique());

const h1 = document.querySelector('h1');

console.dir(h1);
// prototype chain
//HTML Head Element
// Element
// Node
// Event Target
// Object

console.dir(x => x + 1);
//// Coding challenge 1

// const Car = function (name, speed) {
//   this.speed = speed;
//   this.name = name;
// };
// Car.prototype.accelerate = function () {
//   const upspeed = this.speed + 10;
//   console.log(`"${this.name}" going at ${upspeed} km/h`);
// };
// Car.prototype.brake = function () {
//   const lowerSpeed = this.speed - 5;
//   console.log(`"${this.name}" going at ${lowerSpeed} km/h`);
// };

// const BMW = new Car('BMW', 110);
// const Mercedes = new Car('Mercedes', 100);
// // console.log(BMW.__proto__);
// // console.log(Mercedes);

// BMW.accelerate();
// Mercedes.brake();

////////////////////ES6 Classes

// class expression
// const PersonCl=class{};

// class declaration
// class PersonCl {
//   constructor(fullName, birthYear) {
//     // this will automatic setter property
//     this.fullName = fullName;
//     this.birthYear = birthYear;
//   }
//   /// Method will be added in prototype property
//   // instance method
//   clacAge() {
//     console.log(2037 - this.birthYear);
//   }
//   greet() {
//     console.log(`Hey ${this.fullName}`);
//   }
//   ///// getter and setter in class
//   get age() {
//     return 2037 - this.birthYear;
//   }
//   /// set a property that already exist
//   set fullName(name) {
//     // console.log(name);

//     if (name.includes(' ')) this._fullName = name; // to reduce conflict
//     else alert(`${name} is not a full name`);
//   }
//   get fullName() {
//     return this._fullName;
//   }
//   /// static method
//   static Hey() {
//     console.log('hey there 🤗');
//     console.log(this); // point entire class function
//   }
// }
/// when we create object with new keyword constructor is automatically called
/// calling static methods
// PersonCl.Hey();
// const jessica = new PersonCl('Jessica Davis', 1996);
// console.log(jessica);
// jessica.clacAge();

// console.log(jessica.__proto__ === PersonCl.prototype); // constructor PersonCl.prototype
// console.log(jessica.__proto__);

// // same like in class
// // PersonCl.prototype.greet=function(){
// //   console.log(`Hey ${this.firstName}`);
// // }
// jessica.greet();
// // this is a property
// console.log(jessica.age);

///1. Classes are not hoisted ( can't access before declare)
///2. Classes are first class citizen
///3. Classes are executed in strict mode

/// it depend on you to use classes or constructor functiion

//// lec 11 Setter and Getter
// const walter = new PersonCl('Walter White', 1990);

const account = {
  owner: 'jonas',
  movements: [200, 530, 120, 300],

  // get latest movement
  get latest() {
    return this.movements.slice(-1).pop();
  },
  /// this is like property
  set latest(mov) {
    this.movements.push(mov);
  },
};
console.log(account.latest);

account.latest = 50;
console.log(account.movements);

/// lec 12 static method

// Array.from()   static method in array
// Number.parseFloat()  static method

//////////////lec 13
// 3rd way of implementing prototypal inheritance
// manually implementing prototypal inheritance

// object literal
// const PersonProto = {
//   calcAge() {
//     console.log(2037 - this.birthYear);
//   },
//   init(firstName, birthYear) {
//     this.firstName = firstName;
//     this.birthYear = birthYear;
//   },
// };

// /// brand new object link to PersonProto object
// const steven = Object.create(PersonProto); // pointing to person prototype
// console.log(steven);
// steven.name = 'Steven';
// steven.birthYear = 2002;
// steven.calcAge();

// //// in constructor function with new keyword
// // constructor automatic points to the prototype
// // but in object.create method we have to manually point to prototype

// console.log(steven.__proto__);
// console.log(steven.__proto__ === PersonProto);

// const sarah = Object.create(PersonProto);
// sarah.init('Sarah', 1999);
// sarah.calcAge();
// console.log(sarah);
// console.log(sarah.firstName);

/// coding challenge 2
// class Car {
//   constructor(name, speed) {
//     this.name = name;
//     this.speed = speed;
//   }
//   accelerate() {
//     this.speed += 10;
//     console.log(`${this.name} going at ${this.speed}`);
//   }
//   brake() {
//     this.speed -= 5;
//     console.log(`${this.name} going at ${this.speed}`);
//   }
//   get speedUs() {
//     return this.speed / 1.6;
//   }
//   set speedUs(speed) {
//     this.speed = speed * 1.6;
//   }
// }
// const ford = new Car('Ford', 120);
// console.log(ford.speedUs);
// ford.accelerate();
// ford.brake();
// console.log(ford.speedUs);

// ford.speedUs = 50;
// console.log(ford);

//// lec 15 Inherirance in classes using constructor function
/*  using cosntructor function
const Person1 = function (firstName, birthYear) {
  this.firstName = firstName;
  this.birthYear = birthYear;
};
Person1.prototype.calcAge = function () {
  console.log(2037 - this.birthYear);
};

// Student Constructor
const Student = function (firstName, birthYear, course) {
  /// using parent consructor
  Person.call(this, firstName, birthYear); // this is pointing to object
  this.course = course;
};
////making student prototype of person
// at this student object is empty if we write below introduce function then it will overwrite the method
Student.prototype = Object.create(Person1.prototype);

// Student.prototype=Person1.prototype;// it should be not the same object so remove this code

Student.prototype.introduce = function () {
  console.log(`My name is ${this.firstName} and I study ${this.course}`);
};
const mike = new Student('Mike', 2003, 'ComputerScience');
console.log(mike);
mike.introduce();
mike.calcAge();
console.log(mike.__proto__);
console.log(mike.__proto__.__proto__);
console.log(mike instanceof Student);
console.log(mike instanceof Person);

Student.prototype.constructor = Student; // without this student.prototype.constructor will point to person constructor
// still directing to person to fix
console.dir(Student.prototype.constructor);
console.log(mike.__proto__);
/// mike will point to student prototype
/// we want to make student prototype of person class
// as we are doing manually so we will use object.create method

*/
//////Coding Challenge 3

const Car = function (name, speed) {
  this.speed = speed;
  this.name = name;
};
Car.prototype.accelerate = function () {
  const upspeed = this.speed + 10;
  console.log(`"${this.name}" going at ${upspeed} km/h`);
};
Car.prototype.brake = function () {
  const lowerSpeed = this.speed - 5;
  console.log(`"${this.name}" going at ${lowerSpeed} km/h`);
};

const EV = function (name, speed, charge) {
  Car.call(this, name, speed); // to point to parent constructor
  this.charge = charge;
};
EV.prototype = Object.create(Car.prototype);
EV.prototype.chargeBattery = function (chargeTo) {
  this.charge = chargeTo;
};
// overwrite the accelerate method (polymorphism)
EV.prototype.accelerate = function () {
  this.speed += 20;
  this.charge -= 1;
  console.log(
    `'${this.name}' going at ${this.speed}km/h,with a charge of ${this.charge}%`
  );
};
const tesla = new EV('Tesla', 120, 23);
tesla.accelerate();
tesla.brake();
tesla.chargeBattery(90);
console.log(tesla);
// check
console.log(tesla.__proto__);
EV.prototype.constructor = EV;
console.log(EV.prototype.constructor);

// lec 17 Inheritanmce using ES6 Classes

class PersonCl {
  constructor(fullName, birthYear) {
    // this will automatic setter property
    this.fullName = fullName;
    this.birthYear = birthYear;
  }
  /// Method will be added in prototype property
  // instance method
  clacAge() {
    console.log(2037 - this.birthYear);
  }
  greet() {
    console.log(`Hey ${this.fullName}`);
  }
  ///// getter and setter in class
  get age() {
    return 2037 - this.birthYear;
  }
  /// set a property that already exist
  set fullName(name) {
    // console.log(name);

    if (name.includes(' ')) this._fullName = name; // to reduce conflict
    else alert(`${name} is not a full name`);
  }
  get fullName() {
    return this._fullName;// because get element name is alos same to reduce ambiguity
  }
  /// static method
  static Hey() {
    console.log('hey there 🤗');
    console.log(this); // point entire class function
  }
}

class StudentCl extends PersonCl {
  constructor(fullName, birthYear, course) {
    // Always need to happen first
    super(fullName, birthYear); // it automatically call the constructor without any argument but we are now defining
    this.course = course;
  }
  introduce(){
    console.log(`My name is ${this.fullName} and I study ${this.course}`);
  }
  // thius will overwrite the method due to early in prototype chain
  clacAge(){
    console.log(`I am ${2037-this.birthYear} years old, but as a student I feel more like ${2037-this.birthYear+10}`);
  }

}
const martha=new StudentCl("Martha Jones",2003,"Computer Science")
martha.introduce();
martha.clacAge();

// lec 18 Inheritance between classes using object.create
// Parent Prototype
const PersonProto = {
  calcAge() {
    console.log(2037 - this.birthYear);
  },
  init(firstName, birthYear) {
    this.firstName = firstName;
    this.birthYear = birthYear;
  },
};


const steven =Object.create(PersonProto);

// PersonProto is prototype of StudentProto  Student inherits from PersonProto
const StudentProto=Object.create(PersonProto);
// As this is object Literal
StudentProto.init=function(firstName,birthYear,course){
PersonProto.init.call(this,firstName,birthYear);
this.course=course;
}
StudentProto.introduce=function(){
  console.log(`My name is ${this.firstName} and I study ${this.course}`);  
}
// Object is linking  to other object
// StudentProto is prototype of jay Jay inherit from studentProto
const jay=Object.create(StudentProto);
jay.init("jay",2003,"CS");
jay.introduce();
jay.calcAge();// up in prototypechain

