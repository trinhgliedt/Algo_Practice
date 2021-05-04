function findFirstNonRepeatingChar(str) {
  // edge case: no result, meaning all the characters are repeated:

  // need at least O^n
  // make a hash map out of the string to store the char, and first time it appears
  let hMap = {};
  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (!hMap.hasOwnProperty(char)) {
      hMap[char] = i;
    } else if (hMap.hasOwnProperty(char)) {
      delete hMap[char];
    }
  }
  if (Object.keys(hMap).length === 0) {
    return "_";
  } else if (Object.keys(hMap).length > 0) {
    let firstCharInHMap = Object.keys(hMap)[0];
    return firstCharInHMap;
  }
}
console.log("aabbccdeef:", findFirstNonRepeatingChar("aabbccdeef"));
console.log("abcab:", findFirstNonRepeatingChar("abcab"));
console.log("abcabc:", findFirstNonRepeatingChar("abcabc"));
