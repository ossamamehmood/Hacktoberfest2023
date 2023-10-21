function secondLargest(arr) {
    let largest = -Infinity, result = -Infinity;
    for (const value of arr) {
        if (value > largest) {
            result = largest;
            largest = value;    
        }
        else if (value < largest && value > result) {
            result = value;
        }
    }
    return result;
}

// Test it
let arr = [120, -15, -10, -300, -110];
console.log(secondLargest(arr)); // -10