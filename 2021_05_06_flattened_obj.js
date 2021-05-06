let obj = {
  a: 2,
  b: {
    c: 3,
    d: { e: 4 },
  },
};

const flattenedObj = (obj) => {
  let target = {};
  Object.keys(obj).forEach((key) => {
    if (typeof obj[key] === "object" && obj[key] !== null) {
      Object.assign(target, flattenedObj(obj[key]));
    } else {
      target[key] = obj[key];
    }
  });
  return target;
};
console.log(flattenedObj(obj));
