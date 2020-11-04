// Justify the given Text based on the given width of each line
// Given a string str and width of each line as L, the task is to justify the string such that each line of justified text is of length L with help of space (‘ ‘) and the last line should be left-justified.

// Input: str = “The quick brown fox jumps over the lazy dog.”, L = 11
// Output:
// The___quick
// brown___fox
// jumped_over
// the____lazy
// dogs.______
// The symbol _ denotes a space.

function justifiedSentence(str, l){
    // Step 1: break the given string into shorter string at the given length without breaking the word, then trim white space at the end of each line if any
    let result = [];
    let noOfIteration = 1;
    while (str.length > 0) {
        if (str.length-1 < l || str === ""){
            result.push(str);
            str = ""
            break;
        }
        let cutStr =  str.slice(0, l);
        let remainingStr = str.slice(l).trim();
        if (str[l] === " ") {
            result.push(cutStr.trim());
            str = remainingStr;
        }
        else {
            let pOfLastSpace = 0;
            if (cutStr.lastIndexOf(" ") > 0) {
                pOfLastSpace = cutStr.lastIndexOf(" ");
                result.push(cutStr.slice(0, pOfLastSpace).trim());
                remainingStr = str.slice(pOfLastSpace).trim();
                str = remainingStr;

            }
            else {
                result.push(str.trim());
                str = "";
            }
        }
        noOfIteration++;
    }
    // Step 1: insert spaces into each line (array values) to meet the requited length in each line
    let noOfLines = result.length;
    for (let i = 0; i < noOfLines-1; i++){ // minus last line in the string
        if (result[i].length < l) { //this means more space is needed for this line
            let noOfSpaceToAdd = l - result[i].length;
            let oneLineArr = result[i].split(" ");
            let noOfExistingSpaces = oneLineArr.length - 1;
            let oneLineStr = oneLineArr[0];
            let m = Math.min(noOfSpaceToAdd, noOfExistingSpaces);
            
            if (noOfSpaceToAdd < noOfExistingSpaces){
                    for (let j = 1; j < noOfSpaceToAdd + 1; j++) {
                        oneLineStr += " " + " " + oneLineArr[j];
                    }
                    for (let k = noOfSpaceToAdd + 1; k < oneLineArr.length; k++) {
                        oneLineStr +=  " " + oneLineArr[k];
                    }
            }
            if (noOfSpaceToAdd >= noOfExistingSpaces){
                    let n = Math.floor(noOfSpaceToAdd/noOfExistingSpaces);
                    let spaceStr = "";
                    for (let i=1; i<= n; i++){
                        spaceStr += " ";
                    }
                for (let j = 1; j <= noOfExistingSpaces; j++) {
                    oneLineStr += spaceStr + " " + oneLineArr[j];
                }
            }
            result[i] = oneLineStr;
        }
    }
    return result;
}
let str1 = "The quick brown fox jumped over the lazy dog";
let str2 = "The quick brown fox jumped over the lazy dog. The quick brown fox jumped over the lazy dog. The quick brown fox jumped over the lazy dog. The quick brown fox jumped over the lazy dog. The quick brown fox jumped over the lazy dog. The quick brown fox jumped over the lazy dog.";
// console.log(justifiedSentence(str2, 100));
// console.log(justifiedSentence(str1, 11));
console.log(justifiedSentence(str2, 20));