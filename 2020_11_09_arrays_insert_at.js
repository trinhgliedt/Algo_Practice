// InsertAt
// Given an array, index, and additional value, insert
// the value into the array at the given index. Do this
// without using built-in array methods. You can
// think of PushFront(arr,val) as equivalent to
// InsertAt(arr,0,val) .
function insertAt(arr, index, x) {
    //game plan: duplicate the last value in the array, 
    // then, iterate from index to the end, copy all value to the right
    // then, assign the array value at index to be the inserted value
    if (index <= arr.length) {
        let temp = arr[arr.length-1];
        arr.push(temp);
        let len = arr.length;
        for (let i = len - 1; i >= index; i--) {
            arr[i] = arr[i-1];
        }
    }
    arr[index-1] = x;
        return arr;
}
console.log(insertAt([5,3,4,2,8], 3, 9));
console.log(insertAt([5,3,4,2,8], 1, 9));
console.log(insertAt([5,3,4,2,8], 5, 9));
console.log(insertAt([5,3,4,2,8], 10, 9));