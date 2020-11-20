// Page 66 algo:
// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given
// "there's no free lunch - gotta pay yer way" , return "TNFL-GPYW" . Given "Live
// from New York, it's Saturday Night!" , return "LFNYISN" .
function acronyms(str) {
    let arr = str.split(" ");
    let newStr = "";
    for (let i = 0; i<arr.length; i++){
        newStr += arr[i][0].toUpperCase();
    }
    return newStr;
}
console.log(acronyms("Live from New York, it's Saturday Night!"));

