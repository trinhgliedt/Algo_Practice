// Page 66 algo book:
// Remove Blanks
// Create a function that, given a string, returns the string, without blanks. Given " play that
// Funky Music " , returns a string containing "playthatFunkyMusic" .
function removeBlanks(str) {
    return str.trim().split(" ").join("");
}
console.log(removeBlanks("  Play that    Funky Music  "));


