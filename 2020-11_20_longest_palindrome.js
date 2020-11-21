// Page 68
// Longest Palindrome
// For this challenge, we will look not only at the
// entire string, but also substrings within it.
// For a string, return the longest palindromic
// substring. Given "what up, dada?" , return
// "dad" . Given "not much" , return "n" . Include
// spaces as well (i.e. be strict, as in the “Is
// Palindrome” challenge): given "My favorite
// racecar erupted!" , return "e racecar e" .

function isPalindrome(str){
    var BackwardsString = "";
    for (var i = str.length-1; i >= 0; i--){
        BackwardsString += str[i];
  
        }
        return BackwardsString === str;
  
}

function longestPalindrome(str){
    var prevPalindrome = currPalindrome = '';
    // i sets lower bound of the string
    for(var i = 0; i < str.length; i++){
        // j sets the upper bound of the string
        for(var j = str.length; j >= i; j--){
            // console.log("i: ", i, ", j:", j, ", str.slice(i,j):", str.slice(i,j));
            if(isPalindrome(str.slice(i,j))){
                if(prevPalindrome.length < str.slice(i,j).length){
                    // console.log("i: ", i, ", j:", j, ", str.slice(i,j):", str.slice(i,j));
                    prevPalindrome = str.slice(i,j);
                }
                break;
            }
        }
    }
    return prevPalindrome;
}
console.log(longestPalindrome('this')); // should log 't'
console.log(longestPalindrome('bobe')); // should log 'bob'
console.log(longestPalindrome('what up, daddy-o?')); // should log 'dad'
console.log(longestPalindrome('Yikes! my favorite racecar erupted!'));  // should log 'e racecar e'