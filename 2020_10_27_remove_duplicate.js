// Remove Duplicates from Sorted Array

// Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let len = nums.length;
    let i = 0;
    if (len > 1) {
        for (let j = 1; j < len; j++) {
            if (nums[j] !== nums[i]){
                i++;
                nums[i] = nums[j];
            }
        }
    }
        return i+1; //cos i starts at 0
};
let arr1 = [1, 1, 3, 4, 4, 7];
let arr2 = [1];
let arr3 = [1, 4, 5, 5];
console.log(removeDuplicates(arr1));
console.log(removeDuplicates(arr2));
console.log(removeDuplicates(arr3));