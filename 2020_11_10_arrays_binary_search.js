// Binary Search
// Given a sorted array and a value, return whether
// that value is present in the array. Do not
// sequentially iterate the entire array. Instead,
// ‘divide and conquer’, taking advantage of the fact
// that the array is sorted.
function binarySearch(arr, x) {
    if (x < arr[0] || x > arr[arr.length-1]){
        return false;
    }
    if (x === arr[0] || x === arr[arr.length-1]){
        return true;
    }
    let begP = 0, endP = arr.length - 1;
    while (begP <= endP) {
        let midP = Math.floor((endP - begP)/2);
        if (x === arr[midP]){ 
            return true;
        }
        else if (x < arr[midP]) { //go left
            endP = midP - 1;
        }
        else if (x > arr[midP]) { //go right
            begP = midP + 1;
        }
    }
    return false;
}
console.log(binarySearch([1,5,8,9,10,15,20], 5));
console.log(binarySearch([1,5,8,9,10,15,20], 20));
console.log(binarySearch([1,5,8,9,10,15,20], 2));