// page 68
// Is Palindrome
// Strings like "Able was I, ere I saw
// Elba" or "Madam, I'm Adam" could be
// considered palindromes , because (if we ignore
// spaces, punctuation and capitalization) the letters
// are the same from front and back.
// Create a function that returns a boolean whether
// the string is a strict palindrome. For "a x a" or
// "racecar" , return true . Do not ignore spaces,
// punctuation and capitalization: if given "Dud" or
// "oho!" , return false .
function isPalindrome(str){
    var backwardsString = "";
    for (var i = str.length-1; i >= 0; i--){
        backwardsString += str[i];
  
        }
        return backwardsString === str;
}
console.log(isPalindrome("racecar"));
console.log(isPalindrome("Dad"));
console.log(isPalindrome("oho!"));
console.log(isPalindrome("b"));
console.log(isPalindrome(" up, daddy-o?"));
