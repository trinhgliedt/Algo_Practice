// Page 65 Algo book
// ReverseString
// Implement a function reverseString(str) that, given a string, will return the string of the same length but
// with characters reversed. Example: given "creature" , return "erutaerc" . Do not use the built-in
// reverse() function!
function reverseStr(str) {
    let newStr = "";
    for (let i = str.length-1; i>=0; i--) {
        newStr += str[i];
    }
    return newStr;
}
console.log(reverseStr("trinh"));

function reverseStr1(str) {
    return str.split("").reverse().join("");
}
console.log(reverseStr1("trinh"));

// "hello".substr(1); // "ello"
// "hello".charAt(0); // "h"
function reverseStr2(str) {
    if (str === "") // This is the terminal case that will end the recursion
        return "";
    
    else
        return reverseStr2(str.substr(1)) + str.charAt(0);
    /* 
First Part of the recursion method
You need to remember that you won’t have just one call, you’ll have several nested calls

Each call: str === "?"        	                  reverseString(str.subst(1))     + str.charAt(0)
1st call – reverseString("Hello")   will return   reverseString("ello")           + "h"
2nd call – reverseString("ello")    will return   reverseString("llo")            + "e"
3rd call – reverseString("llo")     will return   reverseString("lo")             + "l"
4th call – reverseString("lo")      will return   reverseString("o")              + "l"
5th call – reverseString("o")       will return   reverseString("")               + "o"

Second part of the recursion method
The method hits the if condition and the most highly nested call returns immediately

5th call will return reverseString("") + "o" = "o"
4th call will return reverseString("o") + "l" = "o" + "l"
3rd call will return reverseString("lo") + "l" = "o" + "l" + "l"
2nd call will return reverserString("llo") + "e" = "o" + "l" + "l" + "e"
1st call will return reverserString("ello") + "h" = "o" + "l" + "l" + "e" + "h" 
*/
}
console.log(reverseStr2("trinh"));
