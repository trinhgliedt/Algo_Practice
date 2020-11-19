// Page 64 algo book
// Arrs2Map
// Given two arrays, create an associative array (map) containing keys of the first, and values of the
// second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true] , return {"abc":
// 42, 3: "wassup", "yo": true} .
function arrayToMap(arr1, arr2) {
    let newMap = {};
    for (let i = 0; i < Math.min(arr1.length, arr2.length); i++) {
        newMap[arr1[i]] = arr2[i];
    }
    return newMap;
}
console.log(arrayToMap(["abc", 3, "yo"],[42, "wassup", true]));
console.log(arrayToMap(["abc", 3, "yo"],[42, "wassup", true, 5, 6, 7]));
