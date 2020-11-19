// page 65 algo book
// InvertHash
// Create invertHash(assocArr) that converts a hash’s keys to values and values to corresponding keys.
// Example: given {"name": "Zaphod"; "numHeads": 2} , return {"Zaphod":
function invertHash(obj) {
    let newObj = {};
    for (let key in obj) {
        newObj[obj[key]] = key;
    }
    return newObj;
}
// console.log(invertHash({"name": "Zaphod", "numHeads": 2}));

function objectFlip(obj) {
    return Object.keys(obj).reduce((ret, key) => {
        ret[obj[key]] = key;
        return ret;
    }, {});
}

// console.log(objectFlip({"name": "Zaphod", "numHeads": 2}));

function objectFlip2(obj) {
    return Object.entries(obj).reduce((ret, entry) => {
      const [ key, value ] = entry;
      ret[ value ] = key;
      return ret;
    }, {});
  }
console.log(objectFlip2({"name": "Zaphod", "numHeads": 2}));
