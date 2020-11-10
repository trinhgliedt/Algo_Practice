// Reverse Array
// Given a numerical array, reverse the order of the
// values. The reversed array should have the same
// length, with existing elements moved to other
// indices so that the order of elements is reversed.
function reverseArr(arr) {
    let len = arr.length, temp = 0;
    for (let i = 0; i <= Math.floor((len-1)/2); i++) {
        temp = arr[i];
        arr[i] = arr[len-1-i];
        arr[len-1-i] = temp;
    }
    return arr;
}
console.log(reverseArr([1, 2, 3, 4, 5, 6]))
console.log(reverseArr([1, 2, 3, 4, 5]))