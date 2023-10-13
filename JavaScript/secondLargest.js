//javascript code to find second largest in an array

function secondLargest(arr) {
    let largest = arr[0];
    let second = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > largest) {
            second = largest;
            largest = arr[i];
        } else if (arr[i] < largest && arr[i] > second) {
            second = arr[i];
        }
    }
    return second;
}

console.log("Second Largest is :>> ", secondLargest(array));
