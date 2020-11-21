// Page 67:
// Braces Valid
// Given a string, returns whether the sequence of
// various parentheses, braces and brackets within
// it are valid. For example, given the input string
// "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!" , return
// true . Given "d(i{a}l[t]o)n{e" , return
// false . Given "a(1)s[O(n]0{t)0}k" , return
// false .
function bracesValid(str) {
    var open_braces = [];
    for(var i = 0; i < str.length; i++){
        if(str[i] === '(' || str[i] === '{' || str[i] === '['){
            open_braces.push(str[i]);
        }
        else if(str[i] === ')' || str[i] === '}' || str[i] === ']'){
            if((str[i] === ')' && open_braces[open_braces.length-1] === '(')
            || (str[i] === ']' && open_braces[open_braces.length-1] === '[')
            || (str[i] === '}' && open_braces[open_braces.length-1] === '{')){
                open_braces.pop();
            }
            else{
                return false;
            }
        }
    }
    return open_braces.length == 0;
}
console.log(bracesValid("w(a{t}s[o(n{c}o)m]e)h[e{r}e]!")); //true
console.log(bracesValid('{[a()b]c}')); //true
console.log(bracesValid('{[()}]')); //false
console.log(bracesValid('{}[]()[(])')); //false