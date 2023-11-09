<script>
// Radix sort Javascript implementation

// A utility function to get maximum value in arr[]
function getMax(arr,n)
{
    let mx = arr[0];
        for (let i = 1; i < n; i++)
            if (arr[i] > mx)
                mx = arr[i];
        return mx;
}

// A function to do counting sort of arr[] according to
    // the digit represented by exp.
function countSort(arr,n,exp)
{
    let output = new Array(n); // output array
        let i;
        let count = new Array(10);
        for(let i=0;i<10;i++)
            count[i]=0;
 
        // Store count of occurrences in count[]
        for (i = 0; i < n; i++)
            let x = Math.floor(arr[i] / exp) % 10;
            count[x]++;
 
        // Change count[i] so that count[i] now contains
        // actual position of this digit in output[]
        for (i = 1; i < 10; i++)
            count[i] += count[i - 1];
 
        // Build the output array
        for (i = n - 1; i >= 0; i--) {
            output[count[x] - 1] = arr[i];
            count[x]--;
        }
 
        // Copy the output array to arr[], so that arr[] now
        // contains sorted numbers according to current digit
        for (i = 0; i < n; i++)
            arr[i] = output[i];
}

// The main function to that sorts arr[] of size n using
    // Radix Sort
function radixsort(arr,n)
{
    // Find the maximum number to know number of digits
        let m = getMax(arr, n);
 
        // Do counting sort for every digit. Note that
        // instead of passing digit number, exp is passed.
        // exp is 10^i where i is current digit number
        for (let exp = 1; Math.floor(m / exp) > 0; exp *= 10)
            countSort(arr, n, exp);
}

// A utility function to print an array
function print(arr,n)
{
    for (let i = 0; i < n; i++)
            document.write(arr[i] + " ");
}

/*Driver Code*/
let arr=[170, 45, 75, 90, 802, 24, 2, 66];
let n = arr.length;

// Function Call
radixsort(arr, n);
print(arr, n);


// This code is contributed by awateSumit
</script>
