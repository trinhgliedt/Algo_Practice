// Page 69:
// Common Suffix
// When given an array of words, returns the largest
// suffix (word-end) that is common between all
// words. For example, for input ["ovation",
// "notation", "action"] , return "tion" .
// Given ["nice", "ice", "sic"] , return "" .
function commonSuffix(arr) {
    if (arr.length === 0){return"";}
    if (arr.length === 1){return arr[0];}
// find common suffix of the first 2 words and save it in a variable. Use an array variable instead of a string for the ease of cutting this variable later on.
    let currReversedSuffixArr = [];
    let len1 = arr[1].length;
    let len0 = arr[0].length;
    // console.log("arr[1].length: ", arr[1].length);

    for (let i = len0-1, j = len1-1; i>=0, j>=0; i--, j--){
        if (arr[1][j] === arr[0][i]){
            // console.log("i: ", i,"j: ", j, currReversedSuffixArr);
            currReversedSuffixArr.push(arr[1][j]);
        }
        else if (arr[1][j] !== arr[0][i]){
            break;
        }
    }
    // console.log("line 26: ", currReversedSuffixArr);

    // iterate through the rest of the array, compare the array value with the saved suffix
    for (let i = 2; i<arr.length; i++) {
        let prevReversedSuffixArr = currReversedSuffixArr;
        let len = arr[i].length;
        let sLen = prevReversedSuffixArr.length;
        currReversedSuffixArr = [];
        for (let j = len-1, k=0; j>=0, k<sLen; j--, k++) {
            if (arr[i][j] === prevReversedSuffixArr[k]){
                currReversedSuffixArr.push(arr[i][j]);
            }
            else if (arr[i][j] !== prevReversedSuffixArr[k]){
                break;
            }
        }
        // console.log("line 39: ",prevReversedSuffixArr);
    }
    // iterate thru the reversed suffix array from back to front and make a string from it
    sLen = currReversedSuffixArr.length;
    let suffix = "";
    for (let i=sLen-1; i>=0; i--) {
        suffix += currReversedSuffixArr[i];
    }
    return suffix;
}
console.log("42: ", commonSuffix(["ovation", "notation", "action"]));
console.log("50: ", commonSuffix(["nice", "ice", "sic"]));
console.log("51: ", commonSuffix(["Mike", "hike", "franchise"]));

