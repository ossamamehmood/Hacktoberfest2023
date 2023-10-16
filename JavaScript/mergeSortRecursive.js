function mergeSort(arr) {
    // If our array is tiny or already sorted, there's nothing to do.
    if (arr.length <= 1) {
      return arr;
    }
  
    // Let's split our array into two halves.
    const middle = Math.floor(arr.length / 2);
    const left = arr.slice(0, middle);
    const right = arr.slice(middle);
  
    // Now, we'll sort both of these halves by calling mergeSort on them.
    const leftSorted = mergeSort(left);
    const rightSorted = mergeSort(right);
  
    // Finally, we merge the sorted halves back together and return the result.
    return merge(leftSorted, rightSorted);
  }
  
  function merge(left, right) {
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    // We're going to compare elements from both arrays and put them in the correct order.
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        result.push(left[leftIndex]);
        leftIndex++;
      } else {
        result.push(right[rightIndex]);
        rightIndex++;
      }
    }
  
    // After we've compared and added as many elements as we can, there might be some leftovers.
    // Let's make sure to add any remaining elements from both arrays (if there are any).
    return result.concat(left.slice(leftIndex), right.slice(rightIndex));
  }
  
  // Example usage:
  const arr = [12, 11, 13, 5, 6, 7];
  const sortedArr = mergeSort(arr);
  console.log("Here's the sorted array:", sortedArr);
  