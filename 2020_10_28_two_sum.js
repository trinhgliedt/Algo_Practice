// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]

// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

// Constraints:

// 2 <= nums.length <= 105
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let len = nums.length, result = [];
    for (let j = 0; j < len; j++) {
        for (let i = 1; i < len; i++) {
        let anchor = nums[j];
        if ((anchor + nums[i]) == target && i != j) {
            result.push(j);
            result.push(i);
            return result;
            }
        }
    }
    return [];
};

function twoSum(nums, targetSum) {
    let sum=0;
    let i=0, result = []; 
    while (sum <= targetSum && i < nums.length){
        if (nums[i] < targetSum && (sum + nums[i]) <= targetSum) {
            sum += nums[i];
            result.push(i);
          }
        i++;
    }
    if (sum > targetSum){
        result.pop();
    }
    if (sum == targetSum){
        return result;
      }
    return result;
  
  };

let nums = [2,7,11,15], target = 9;
let nums1 = [3,2,4], target1 = 6;
let nums2 = [3,3], target2 = 6;
let nums3 = [2,5,5,11], target3 = 10;
console.log(twoSum(nums, target));
console.log(twoSum(nums1, target1));
console.log(twoSum(nums2, target2));
console.log(twoSum(nums3, target3));