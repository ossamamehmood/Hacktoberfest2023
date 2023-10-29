function mergeSort<T>(array: T[]): T[] {
    if (array.length <= 1) {
      return array;
    }
  
    const middle = Math.floor(array.length / 2);
    const left = array.slice(0, middle);
    const right = array.slice(middle);
  
    return merge(mergeSort(left), mergeSort(right));
  }
  
  function merge<T>(left: T[], right: T[]): T[] {
    let result: T[] = [];
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
  
  // Example usage
  const unsortedArray: number[] = [4, 2, 7, 1, 9, 5, 3, 8, 6];
  const sortedArray: number[] = mergeSort(unsortedArray);
  console.log("Sorted Array:", sortedArray); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  