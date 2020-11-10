// Page 53 algo book:
// Skyline Heights
// You are given an array with heights of consecutive buildings in the city. For example, [-1,7,3] would
// represent three buildings: first is actually below street level, second is seven stories high, and third is
// three stories high (but hidden behind the seven-story onbe). You are situated at street level. Return an
// array containing heights of the buildings you can see, in order. Given [1,-1,7,3] return [1,7] .
function visibleBuildings(arr) {
    let result = [];
    let len = arr.length;
    for (let i = 1; i < len; i++ ) {
        if (arr[i] > 0 && result.length === 0){
            result.push(arr[i]);
        }
        else if (arr[i] > 0 && arr[i] > result[result.length-1]){
            result.push(arr[i]);
        }
    }
    return result;
}
console.log(visibleBuildings([1,-1,7,3,10,5,-1,11]));
console.log(visibleBuildings([-1,-2,3]));