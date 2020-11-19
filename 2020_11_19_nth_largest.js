// Page 55 algo book
// Nth-Largest
// Given an array, return the Nth-largest element:
// there should be (N - 1) elements that are larger.
function nthLargest(arr, n) {
    if (n > arr.length) {
        console.log("The array you provided doesn't have a/an "+ n + "th element");
        return null;
    }
    else {
        let max = arr[0];
        let maxArr = [];
        for (let i = 0; i<arr.length; i++){
            if (arr[i] > max){
                max = arr[i]
            }
        maxArr.push(max);

        for (let j = 2; j <= n; j++) {
            let prevMax = -Infinity;
            for (let i = 0; i<arr.length; i++){
                if (arr[i] > prevMax && arr[i] < maxArr[maxArr.length-1]){
                    prevMax = arr[i]
                }
            }
            maxArr.push(prevMax);
        }
        console.log("maxArr: ", maxArr);
        return maxArr[n-1];
    }
}
console.log("line 23: ", nthLargest([5,3,2,9,15,20,6], 3));
console.log("line 24: ", nthLargest([5,3,2,9,15,20,6], 5));
console.log("line 25: ", nthLargest([2],1));
console.log("line 26: ", nthLargest([],2));