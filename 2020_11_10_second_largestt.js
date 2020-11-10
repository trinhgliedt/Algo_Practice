// Page 55 algo book
// Second-Largest
// Return the second-largest element of an array.
function secondLargest(arr) {
    let max = Math.max.apply(null, arr);
    maxPos = arr.indexOf(max);
    arr[maxPos] = -Infinity;
    let secondMax = Math.max.apply(null, arr);
    arr[maxPos] = max;
    return secondMax;
}
console.log(secondLargest([5,3,2,9,4,5,10,2]))