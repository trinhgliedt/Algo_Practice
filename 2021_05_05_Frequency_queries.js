// You are given  queries. Each query is of the form two integers described below:
// -  : Insert x in your data structure.
// -  : Delete one occurence of y from your data structure, if present.
// -  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

// The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

// Example

// The results of each operation are:

// Operation   Array   Output
// (1,1)       [1]
// (2,2)       [1]
// (3,2)                   0
// (1,1)       [1,1]
// (1,1)       [1,1,1]
// (2,1)       [1,1]
// (3,2)                   1
// Return an array with the output: .

// Function Description

// Complete the freqQuery function in the editor below.

// freqQuery has the following parameter(s):

// int queries[q][2]: a 2-d array of integers
// Returns
// - int[]: the results of queries of type

// Input Format

// The first line contains of an integer , the number of queries.
// Each of the next  lines contains two space-separated integers,  and .

// Constraints

// All
// Sample Input 0

// 8
// 1 5
// 1 6
// 3 2
// 1 10
// 1 10
// 1 6
// 2 5
// 3 2
// Sample Output 0

// 0
// 1
// Explanation 0

// For the first query of type , there is no integer whose frequency is  (). So answer is .
// For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .

// Sample Input 1

// 4
// 3 4
// 2 1003
// 1 16
// 3 1
// Sample Output 1

// 0
// 1
// Explanation 1

// For the first query of type , there is no integer of frequency . The answer is . For the second query of type , there is one integer,  of frequency  so the answer is .

// Sample Input 2

// 10
// 1 3
// 2 3
// 3 2
// 1 4
// 1 5
// 1 5
// 1 4
// 3 2
// 2 4
// 3 2
// Sample Output 2

// 0
// 1
// 1
// Explanation 2

// When the first output query is run, the array is empty. We insert two 's and two 's before the second output query,  so there are two instances of elements occurring twice. We delete a  and run the same query. Now only the instances of  satisfy the query.

function freqQuery1(queries) {
  let arr = [];
  let result = [];
  queries.forEach((q) => {
    console.log("q:", q);
    // console.log("arr:", arr);
    if (q[0] === 1) {
      arr.push(q[1]);
    } else if (q[0] === 2) {
      arr.indexOf(q[1]) > -1 && arr.splice([arr.indexOf(q[1])], 1);
    } else if (q[0] === 3) {
      // console.log("in 3");
      // create a hashmap for all values
      // let arrMap = new Map();
      let arrMap = {};
      for (let i = 0; i < arr.length; i++) {
        // console.log(
        //   i,
        //   "arr:",
        //   arr,
        //   "arrMap:",
        //   arrMap,
        //   "arr[i]",
        //   arr[i],
        //   "arrMap.hasOwnProperty(arr[i].toString()):",
        //   arrMap.hasOwnProperty(arr[i].toString())
        // );
        // arrMap.get(arr[i])
        //   ? arrMap.set(arr[i], arrMap.get(arr[i]) + 1)
        //   : arrMap.set(arr[i], 1);
        arrMap.hasOwnProperty(arr[i].toString())
          ? (arrMap[arr[i]] = arrMap[arr[i]] + 1)
          : (arrMap[arr[i]] = 1);
      }

      let found = [];
      Object.keys(arrMap).forEach((key) => {
        if (arrMap[key] === q[1]) {
          found.push(true);
        } else found.push(false);
        console.log(
          "arr:",
          arr,
          "arrMap:",
          arrMap,
          "key",
          key,
          "arrMap[key]:",
          arrMap[key],
          "q[1]:",
          q[1],
          "found:",
          found
        );
      });
      found.length >= 1 && found.some((check) => check === true)
        ? result.push(1)
        : result.push(0);
    }
  });
  return result;
}
// console.log(
//   freqQuery([
//     [1, 1],
//     [2, 2],
//     [3, 2],
//     [1, 1],
//     [1, 1],
//     [2, 1],
//     [3, 2],
//   ])
// );
// console.log(
//   freqQuery([
//     [1, 5],
//     [1, 6],
//     [3, 2],
//     [1, 10],
//     [1, 10],
//     [1, 6],
//     [2, 5],
//     [3, 2],
//   ])
// );

function freqQuery(queries) {
  let arr = [];
  let result = [];
  queries.forEach((q) => {
    if (q[0] === 1) {
      arr.push(q[1]);
    } else if (q[0] === 2) {
      arr.indexOf(q[1]) > -1 && arr.splice([arr.indexOf(q[1])], 1);
    } else if (q[0] === 3) {
      let arrMap = {};
      for (let i = 0; i < arr.length; i++) {
        arrMap.hasOwnProperty(arr[i].toString())
          ? (arrMap[arr[i]] = arrMap[arr[i]] + 1)
          : (arrMap[arr[i]] = 1);
      }

      let found = [];
      Object.keys(arrMap).forEach((key) => {
        if (arrMap[key] === q[1]) {
          found.push(true);
        } else found.push(false);
      });
      found.length >= 1 && found.some((check) => check === true)
        ? result.push(1)
        : result.push(0);
    }
  });
  return result;
}

const freqQuery2 = (queries) => {
  const result = [];
  const hash = {};
  const freq = [];

  for (let i = 0; i < queries.length; i += 1) {
    const [action, value] = queries[i];
    const initValue = hash[value] || 0;

    if (action === 1) {
      hash[value] = initValue + 1;
      freq[initValue] = (freq[initValue] || 0) - 1;
      freq[initValue + 1] = (freq[initValue + 1] || 0) + 1;
    }

    if (action === 2 && initValue > 0) {
      hash[value] = initValue - 1;
      freq[initValue - 1] += 1;
      freq[initValue] -= 1;
    }

    if (action === 3) result.push(freq[value] > 0 ? 1 : 0);
    console.log(
      queries[i],
      "hash:",
      hash,
      "initValue:",
      initValue,
      "freq:",
      freq,
      "result:",
      result
    );
  }

  return result;
};

console.log(
  freqQuery2([
    [1, 3],
    [2, 3],
    [3, 2],
    [1, 4],
    [1, 5],
    [1, 5],
    [1, 4],
    [3, 2],
    [2, 4],
    [3, 2],
  ])
);
