// fibonacci2
// Implement the fibonacci2 function, a famous mathematical equation that generates a numerical
// sequence such that each number is the sum of the previous two. The fibonacci2 numbers at index 0
// and 1, coincidentally, have values of 0 and 1. Your function should accept an argument of which
// fibonacci2 number.
// Examples: fibonacci2(2) = 1, fibonacci2(3) = 2, fibonacci2(4) = 3, fibonacci2(5) = 5, etc.
function fibonacci2(x) {
    if (x <= 1) return 1;
    return fibonacci2(x - 1) + fibonacci2(x - 2);
}

function fibonacci21(x) {
    let a = 1, b = 0, temp = 0;
    while (x >= 0) {
        temp = a;
        a = a + b; 
        b = temp;
        x--;
    }
    return b
}

function fibonacci22(x) {
    let a = 1, b = 0, temp = 0;
    for (let i = x; i >=0; i--) {
        temp = a;
        a = a + b; 
        b = temp;
        
    }
    return b
}

console.log(fibonacci2(0));
console.log(fibonacci2(1));
console.log(fibonacci2(2));
console.log(fibonacci2(3));
console.log(fibonacci2(4));
console.log(fibonacci2(5));
console.log(fibonacci2(6));
console.log(fibonacci2(7));
console.log(fibonacci2(8));
console.log(fibonacci2(9));
console.log(fibonacci2(10));
console.log(fibonacci2(11));
console.log(fibonacci2(12));