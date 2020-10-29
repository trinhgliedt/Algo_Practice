// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Follow up: Could you solve it without converting the integer to a string?

 

// Example 1:

// Input: x = 121
// Output: true
// Example 2:

// Input: x = -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: x = 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Example 4:

// Input: x = -101
// Output: false
 

// Constraints:

// -2^31 <= x <= 2^31 - 1

/**
 * @param {number} x
 * @return {boolean}
 */

var isPalindrome = function(x) {
    if (x < 0 || Math.abs(x) >= 2**31) {return false;}
    if (x < 10) {return true;}
    let xStr = x.toString();
    let len = xStr.length, check = false;
    if (len == 2) {return xStr[0]===xStr[1];}
    for (let i = 0, j = len-1; i <= Math.floor(len/2), j>= Math.floor(len/2); i++, j--) {
        if (xStr[i] === xStr[j]) {
            check = true;
        }
        else {return false;}
        // console.log("len: ", len, ", i: ", i, ", j: ", j, "check: ", check);
    }
    return check;
};

var isPalindrome = function(num) {
    var top = Math.pow(10, Math.log10(num) | 0), bot = 1;
    while (top >= bot) {
        if ((num / top % 10 | 0) !== (num / bot % 10 | 0)) { return false }
        top /= 10;
        bot *= 10;
    }
    return true;
};

let x1 =121;
let x2 = -121;
let x3 = 10;
let x4 = 11;
let x5 = 0;
let x6 = 100;
let x7 = 4444;
let x8 = 4444444444444;
let x9 = 123123;
let x10 = 1000030001;
console.log(x1, isPalindrome(x1));
console.log(x2, isPalindrome(x2));
console.log(x3, isPalindrome(x3));
console.log(x4, isPalindrome(x4));
console.log(x5, isPalindrome(x5));
console.log(x6, isPalindrome(x6));
console.log(x7, isPalindrome(x7));
console.log(x8, isPalindrome(x8));
console.log(x9, isPalindrome(x9));
console.log(x10, isPalindrome(x10));