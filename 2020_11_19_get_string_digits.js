// Page 66 Algo:
// Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given
// "0s1a3y5w7h9a2t4?6!8?0" , the function should return the number 1,357,924,680.
function strDigits(str) {
    let len = str.length;
    let newStr = "";
    for (let i = 0; i<len; i++){
        if (isNaN(parseInt(str[i])) === false) {
            newStr += str[i];
        }
    }
    // return parseInt(newStr);
    return +newStr;
}
console.log(strDigits("0s1a3y5w7h9a2t4?6!8?0"));