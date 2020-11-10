// RemoveAt
// Given an array and an index into the array,
// remove and return the array value at that index.
// Do this without using any built-in array methods
// except pop() . Think of PopFront(arr) as
// equivalent to RemoveAt(arr,0) .
function removeAt(arr, index) {
    //iterating from index to the end, copy all the array value by one to the left
    //then, pop the last one
    let temp = arr[0];
    let len = arr.length;
    for (let i = index-1; i < len-1; i++) {
        arr[i] = arr[i+1];
    }
    arr.pop();
    console.log(arr);
    return temp;
}
console.log(removeAt([5,3,4,2,8], 3));