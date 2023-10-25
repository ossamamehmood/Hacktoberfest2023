'use strict';
// 4  feilds
// Public fields
// Private fields
// Public methods
// Private methods
// there is also static version total 8

// lec 19 onwards another example of classes
class Account {
  //1) Public instance field
  //on the instance
  locale = navigator.language;

  // 2) Private fields on the instance
  #movements = []; //not on the prototype
  #pin;
  constructor(owner, currency, pin) {
    this.owner = owner;
    this.currency = currency;
    // private
    this.#pin = pin;
    // private
    this.#movements = [];
    this.locale = navigator.language;

    console.log(`Thanks for opening an account,${owner}`);
  }
  // Public Interface of our object
  getMovements() {
    return this.#movements;
  }

  deposit(val) {
    this.#movements.push(val);
    return this; // current object  for chainig possible
  }
  // abstract the fact
  withdrawal(val) {
    // withdrawal with negative value
    this.deposit(-val); // we are calling another method that's fine also to reduce redundancy
    return this;
  }
  // not part of public API
  requestLoan(val) {
    if (this.#approveLoan(val)) {
      this.deposit(val);
      console.log('loan approved');
      return this;
    }
  }
  // 4) private method
  #approveLoan(val) {
    return true;
  }
  // static public method
  static helper() {
    console.log('Helper');
  }
}
const acc1 = new Account('Jonas', 'EUR', 1111);
console.log(acc1);

// acc1.#movements.push(120);
// acc1.#movements.push(-234);
// better to use method that also abstract the negative value in withdrawal method
acc1.deposit(240);
acc1.withdrawal(120);
acc1.requestLoan(1000);

console.log(acc1.getMovements());
// console.log(acc1.#appoveLoan()); // give error due to private
console.log(acc1);
Account.helper();

///lec20 Encapsulation some methods and properties are set private inside the class so that they are not accessible by class
//  lec21 actually private methods and fields

/// lec22  Chaining  Method
acc1
  .deposit(300)
  .deposit(200)
  .withdrawal(35)
  .requestLoan(25000)
  .withdrawal(4000);
console.log(acc1.getMovements());

/// Coding Challenge #4
class CarCl {
  constructor(name, speed) {
    this.speed = speed;
    this.name = name;
  }
  accelerate() {
    this.speed += 10;
    console.log(`"${this.name}" going at ${this.speed} km/h`);
  }
  brake() {
    const lowerSpeed = this.speed - 5;
    console.log(`"${this.name}" going at ${lowerSpeed} km/h`);
    return this;
  }
  get speedUs() {
    return this.speed / 1.6;
  }
  set speedUs(speed) {
    this.speed = speed * 1.6;
  }
}
class EVCl extends CarCl {
  #charge;
  constructor(name, speed, charge) {
    super(name, speed);
    this.#charge = charge;
  }
  chargeBattery(chargeTo) {
    this.#charge = chargeTo;
    return this;
  }
  accelerate() {
    this.speed += 20;
    this.#charge -= 1;
    console.log(
      `'${this.name}' going at ${this.speed}km/h,with a charge of ${
        this.#charge
      }%`
    );
    return this;
  }
}
const rav = new EVCl('Ravian', 120, 23);
console.log(rav);
rav.accelerate().accelerate().brake().chargeBattery(50).accelerate();

console.log(rav.speedUs);