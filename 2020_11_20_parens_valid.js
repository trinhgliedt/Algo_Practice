// Page 67 Algo:
// Parens Valid
// Create a function that, given an input string,
// returns a boolean whether parentheses in that
// string are valid. Given input "y(3(p)p(3)r)s" ,
// return true. Given "n(0(p)3" , return false .
// Given "n)0(t(0)k" , return false .
function parensValid(str) {
    let count = 0;
    for (let i = 0; i <str.length; i++) {
        if (str[i] === "("){
            if (count < 0){return false;}
            count += 1;
            // console.log(str[i], ", count: ", count);
        //         }
        }
        else if (str[i] === ")") {
            count -= 1;
            // console.log(str[i], ", count: ", count);
        
        }
    }
    return (count != 0 ? false : true);
}
console.log(parensValid("y(3(p)p(3)r)s")); //true
console.log(parensValid("n(0(p)3")); // false
console.log(parensValid("n)0(t(0)k")); //false
console.log(parensValid("()(()(())))")); //false