const array = [2, 3, 4, 10, 40];

function binarySearch(arr, target, start, end) {
    if (start > end) return false;
    const mid = Math.floor((start + end) / 2);
    if (arr[mid] === target) {
        console.log(`value found at ${mid}`);
        return true;
    }
    if (arr[mid] > target) {
        return binarySearch(arr, target, start, mid - 1);
    }
    if (arr[mid] < target) {
        return binarySearch(arr, target, mid + 1, end);
    }
}

console.log(binarySearch(array, 10, 0, array.length - 1));
