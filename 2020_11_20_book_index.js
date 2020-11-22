// page 69:
// Book Index
// Write a function that given a sorted array of page
// numbers, return a string representing a book
// index. Combine consecutive pages to create
// ranges. Given [1, 3, 4, 5, 7, 8, 10] ,
// return the string "1, 3-5, 7-8, 10" .
function bookIndex(arr) {
    var myStr = "";
    var firstnum = arr[0];
    var lastnum;
    for(var i = 0; i < arr.length; i++){
        // if it is not consecutive, (top end of range becomes current index)
        if (!(arr[i] + 1 == arr[i+1])){
            lastnum = arr[i];
            // This if statement is for checking for last element (don't add ", " at the end)
            if(i == arr.length -1){
                // Checks for cases where "-" is not needed. i.e. [5,10,12] -> logs "5, 10, 12"
                if(firstnum == lastnum){
                    myStr += firstnum;
                }
                // Else, "-" added to consecutive set of numbers
                else{
                    myStr += firstnum + "-" + lastnum;
                    firstnum = arr[i + 1];
                }
            }
            // separates the strings, rather than first index/last index.
            else{
                // Checks if the index is single, non-consecutive.
                if(firstnum == lastnum){
                    myStr += firstnum + ", "
                    firstnum = arr[i + 1];
                }
                // Else, "-" added to consecutive set of numbers
                else{
                    myStr += firstnum + "-" + lastnum + ", ";
                    firstnum = arr[i + 1];
                }
            }

        }
    }
    return myStr
  }

  console.log(bookIndex([1, 2, 3, 5, 6, 7, 10, 11]));
  console.log(bookIndex([5, 10, 11, 12]));