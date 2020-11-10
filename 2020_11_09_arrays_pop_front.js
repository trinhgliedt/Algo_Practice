// PopFront
// Given an array, remove and return the value at
// the beginning of the array. Do this without using
// any built-in array methods except pop() .
function popFront(arr) {
    //copy all the array value by one to the left
    //then, pop the last one
    let temp = arr[0];
    let len = arr.length;
    for (let i = 0; i < len-1; i++) {
        arr[i] = arr[i+1];
    }
    arr.pop();
    console.log(arr);
    return temp;
}
console.log(popFront([5,3,4,2,8]));

//built-in method:
let myArr = [5,3,4,2,8];
myArr.shift();
console.log(myArr);