function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
  
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
  
      if (arr[mid] === target) {
        return mid; // Element found, return its index
      }
  
      if (arr[mid] < target) {
        left = mid + 1; // Adjust the left boundary
      } else {
        right = mid - 1; // Adjust the right boundary
      }
    }
  
    return -1; // Element not found
  }
  
  // Example usage:
  const sortedArray = [2, 4, 6, 8, 10, 12, 14, 16, 18];
  const target = 10;
  const result = binarySearch(sortedArray, target);
  
  if (result !== -1) {
    console.log(`Element ${target} found at index ${result}`);
  } else {
    console.log(`Element ${target} not found in the array`);
  }
  