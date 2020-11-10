// Page 53 algo book
// Remove Negatives
// Implement a function removeNegatives() that
// accepts an array and removes any values that
// are less than zero.
// Second-level challenge: don’t use nested loops.
function removeNegatives(arr) {
    let temp = 0;
    if (arr[arr.length-1] < 0) {arr.pop();}
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            console.log("i: ", i)
            temp = arr[arr.length-1];
            arr[arr.length-1] = arr[i];
            arr[i] = temp; 
            arr.pop();
        }
    }
    return arr;
}
console.log(removeNegatives([-2,3,5,-9,5,2,-6]));