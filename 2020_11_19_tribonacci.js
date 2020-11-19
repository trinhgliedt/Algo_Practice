// Page 57 algo book
// Tricky Tribonacci
// Why stop with fibonacci? Create a function to
// retrieve a “tribonacci” number, from the sum of
// the previous 3 . Tribonaccis are {0, 0, 1, 1, 2, 4, 7,
// 13, 24, 44, 81, ...}. Again, use a time-space
// tradeoff to make this fast.
function tribonacci(x) {
    if (x < 2) {return 0;}
    else {
        let current = 1, prev1 = 0, prev2 = 0, temp = 0, temp1 = 0;
        for (let i = x; i >=2; i--) {
            temp = current;
            temp1 = prev1;
            current = current + prev1 + prev2;
            prev1 = temp;
            prev2 = temp1;
            // console.log("i: ", i, ", current: ", current, ", prev1: ", prev1, ", prev2: ", prev2);
        }
        return prev1;
    }
}

console.log("0: ", tribonacci(0));
console.log("1: ", tribonacci(1));
console.log("2: ", tribonacci(2));
console.log("3: ", tribonacci(3));
console.log("4: ", tribonacci(4));
console.log("5: ", tribonacci(5));
console.log("6: ", tribonacci(6));
console.log("7: ", tribonacci(7));
console.log("8: ", tribonacci(8));
console.log("9: ", tribonacci(9));
console.log("10: ", tribonacci(10));