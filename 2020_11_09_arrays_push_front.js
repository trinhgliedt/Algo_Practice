// PushFront
// Given an array and an additional value, insert this
// value at the beginning of the array. Do this
// without using any built-in array methods.
function pushFront(arr, x) {
    //game plan: duplicate the last value in the array, 
    // then, copy all value to the right
    // then, assign the first array value to be the inserted value
    let temp = arr[arr.length-1];
    arr.push(temp);
    let len = arr.length;
    for (let i = len - 2; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[0] = x;
    return arr;
}
console.log(pushFront([5,3,4,2,8], 9));