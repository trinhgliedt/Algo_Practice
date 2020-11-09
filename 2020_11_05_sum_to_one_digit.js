// Page 41 algo books
// Sum To One Digit
// Implement a function sumToOne(num) that,
// given a number, sums that number’s digits
// repeatedly until the sum is only one digit. Return
// that final one digit result.
function sumToOneDigit(num){
    let numStr = num.toString(), len = numStr.length, tempNum = 0;
    
    while (len > 1) {
        tempNum = 0;
        for (let i = 0; i < len; i++) {
            tempNum += parseInt(numStr[i]);
        }
        numStr = tempNum.toString();
        len = numStr.length;
    }
    return tempNum;
}
console.log(sumToOneDigit(12345));

// method 2: This is pretty cool
function sumToOneDigit2(num){
    switch(num%9) {
        case 0: return 9;
        case 1: return 1; 
        case 2: return 2 
        case 3: return 3; 
        case 4: return 4; 
        case 5: return 5; 
        case 6: return 6; 
        case 7: return 7; 
        case 8: return 8; 
        default: return -1;
    }
}
console.log(sumToOneDigit2(945));