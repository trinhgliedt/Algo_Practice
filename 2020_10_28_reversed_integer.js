Note:
// Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21
// Example 4:

// Input: x = 0
// Output: 0
 

// Constraints:

// -2^31 <= x <= 2^31 - 1

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let xStr = Math.abs(x).toString();
    let len = xStr.length;
    let resultStr = "";
    for (i = len-1; i >= 0; i--) {
        resultStr += xStr[i];
    }
    if (parseInt(resultStr) < 2**31) {
        return Math.abs(x) === x ? parseInt(resultStr) : -parseInt(resultStr);
    }
    return 0;
};
let x1 = 123;
let x2 = -123;
let x3 = 120;
let x4 = 1234567893;
console.log(reverse(x1));
console.log(reverse(x2));
console.log(reverse(x3));
console.log(reverse(x4));