/* 
  https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/

  Stable sort
  
  Time Complexity
    - Best:     O(n) linear when array is already sorted
    - Average:  O(n^2) quadratic
    - Worst:    O(n^2) quadratic when the array is reverse sorted

  Space: O(1) constant

  For review, create a function that uses BubbleSort to sort an unsorted array in-place.

  For every pair of adjacent indicies, swap them if the item on the left is larger than the item on the right until array is fully sorted
*/


const numsOrdered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numsRandomOrder = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8];
const numsReversed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function bubbleSort(nums) {
    let len = nums.length;
    for (let j = 0; j < len-1; j++) {
        for (let i = 0; i < len-1; i++) {
            if (nums[i] > nums[i+1]) {
                let temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
            }
        }
    }
    return nums;
}

function bubbleSort(nums) {
    let len = nums.length;
    let isSorted = false;
    while (isSorted === false) { //only perform action on elements not sorted
        isSorted = true;
        for (let i = 0; i < len-1; i++) {
            if (nums[i] > nums[i+1]) {
                isSorted = false;
                let temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
            }
        }
    }
    return nums;
}

module.exports = { bubbleSort };

console.log(bubbleSort(numsOrdered));
console.log(bubbleSort(numsRandomOrder));
console.log(bubbleSort(numsReversed));
