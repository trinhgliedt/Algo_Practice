// Fibonacci
// Implement the Fibonacci function, a famous mathematical equation that generates a numerical
// sequence such that each number is the sum of the previous two. The Fibonacci numbers at index 0
// and 1, coincidentally, have values of 0 and 1. Your function should accept an argument of which
// Fibonacci number.
// Examples: fibonacci(2) = 1, fibonacci(3) = 2, fibonacci(4) = 3, fibonacci(5) = 5, etc.
function fibonacci(x) {
    if (x <= 1) return 1;
    return fibonacci(x - 1) + fibonacci(x - 2);
}

function fibonacci1(x) {
    let a = 1, b = 0, temp = 0;
    while (x >= 0) {
        temp = a;
        a = a + b; 
        b = temp;
        x--;
    }
    return b
}

function fibonacci2(x) {
    let a = 1, b = 0, temp = 0;
    for (let i = x; i >=0; i--) {
        temp = a;
        a = a + b; 
        b = temp;
        
    }
    return b
}

// console.log(fibonacci(2));
// console.log(fibonacci(3));
// console.log(fibonacci(4));
// console.log(fibonacci(5));
// console.log(fibonacci(6));
// console.log(fibonacci(7));
// console.log(fibonacci(8));
// console.log(fibonacci(9));
// console.log(fibonacci(10));
// console.log(fibonacci(11));
// console.log(fibonacci(12));
// console.log(fibonacci1(12));
console.log(fibonacci2(12));