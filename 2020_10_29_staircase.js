// Staircase

// This is a staircase of size :

//    #
//   ##
//  ###
// ####
// Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

// Write a program that prints a staircase of size .

// Function Description

// Complete the staircase function in the editor below.

// staircase has the following parameter(s):

// int n: an integer
// Print

// Print a staircase as described above.

// Input Format

// A single integer, , denoting the size of the staircase.

// Constraints

//  .

// Output Format

// Print a staircase of size  using # symbols and spaces.

// Note: The last line must have  spaces in it.

// Sample Input

// 6 
// Sample Output

//      #
//     ##
//    ###
//   ####
//  #####
// ######
// Explanation

// The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
function staircase(n) {
    let noOfSpaces = 0, noOfHashes = 0;
    let result = "";
    for (let i = 1; i <= n; i++) {
        result = "";
        noOfSpaces = n-i;
        noOfHashes = i;
        for (let j = 1; j <= noOfSpaces; j++) {
            result += " ";
        }
        for (let k = 1; k <= noOfHashes; k++) {
            result += "#";
        }
        console.log(result);
    }

}
staircase(20);