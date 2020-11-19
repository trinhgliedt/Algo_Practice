// Page 56 algo book
// Shuffle
// Recreate the shuffle() built into JavaScript, to
// efficiently shuffle a given array’s values. Do you
// need to return anything from your function?

// Option 1: create a new result array 
function shuffle(arr) {
    // generate an array with indexes of the given array
    let indexArr = [];
    for (let i = 0; i<arr.length; i++){
        indexArr.push(i);
    }
    // loop: i = length of the index array to i=1, i--
    for (let i = indexArr.length; i>= 1; i--){
        // generate a random number between 1 to i
        let randomIndex = Math.floor(Math.random()*i);
        //in the index array, swap the newly generated number with the last index.
        let temp = indexArr[randomIndex];
        indexArr[randomIndex] = indexArr[indexArr.length-1];
        indexArr[indexArr.length-1] = temp;
    }
    // now we have a new index array
    // iterate through this new index array, push value of the given array based on this index
    let newArr = [];
    for (let i = 0; i < indexArr.length; i++) {
        newArr.push(arr[indexArr[i]]);
    }
    return newArr;
}
// console.log(shuffle([1,2,3,4,5]));
// console.log(shuffle([6,10,2,3,4]));
// console.log(shuffle(["apple", "banana", "strawberry", "plum"]));

// Option 2: alter the given array in place 
function shuffle1(arr) {
    // loop: i = length of the given array to i=1, i--
    for (let i = arr.length; i>= 1; i--){
        // generate a random number between 1 to i
        let randomIndex = Math.floor(Math.random()*i);
        //in the given array, swap the array value (at the random index that we just had) with the last value.
        let temp = arr[randomIndex];
        arr[randomIndex] = arr[arr.length-1];
        arr[arr.length-1] = temp;
    }
    return arr;
}
// console.log(shuffle1([1,2,3,4,5]));
// console.log(shuffle1([6,10,2,3,4]));
console.log(shuffle1(["apple", "banana", "strawberry", "plum"]));