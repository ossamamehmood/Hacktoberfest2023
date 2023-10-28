// Pigeonhole Sort Algorithm in JavaScript
// GitHub: https://github.com/uppy19d0

function pigeonholeSort(arr) {
    let min = arr[0];
    let max = arr[0];

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    const range = max - min + 1;
    const holes = new Array(range).fill().map(() => []);

    for (let i = 0; i < arr.length; i++) {
        holes[arr[i] - min].push(arr[i]);
    }

    let index = 0;
    for (let i = 0; i < range; i++) {
        for (const value of holes[i]) {
            arr[index++] = value;
        }
    }

    return arr;
}

// Example usage:
const inputArray = [8, 3, 2, 7, 4, 6, 8];
const sortedArray = pigeonholeSort(inputArray);
console.log("Sorted order is:", sortedArray);
