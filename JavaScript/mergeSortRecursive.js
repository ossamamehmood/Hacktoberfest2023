// Merge sort function
function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);

  const leftSorted = mergeSort(left);
  const rightSorted = mergeSort(right);

  return merge(leftSorted, rightSorted);
}

// Helper function to merge sorted arrays
function merge(left, right) {
  let result = [];

  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  return result.concat(left.slice(leftIndex), right.slice(rightIndex));
}

// Usage
const arr = [12, 11, 13, 5, 6, 7];
const sortedArr = mergeSort(arr);

console.log(sortedArr);