/* 
  Given an honorific (name title) and array of full name strings,
  in "LastName, FirstName" format
  
  Return a new array of strings in this format: "Honorific FirstName LastName"

  Bonus: re-write it with built in functional programming methods
*/

// const honorific1 = "Mr.";
// const names1 = [];
// const expected1 = [];

// const honorific2 = "Sir";
// const names2 = ["Sanchez, Rick", "Smith, Jerry"];
// const expected2 = ["Sir Rick Sanchez", "Sir Jerry Smith"];

// const honorific3 = "Mrs.";
// const names3 = ["HorseDoctor, Beth"];
// const expected3 = ["Mrs. Beth HorseDoctor"];

/**
 *
 * @param   {string} honorific
 *          The honorific to be added to the @fullNames
 *          e.g., "Sir" or "Mrs."
 * @param   {Array<string>} fullNames
 *          Format "LastName, FirstName"
 * @return  {Array<string>}
 *          The full names formatted:
 *          @honorific FirstName LastName
 * Time:    O(n * m)
 *          n = @fullNames length
 *          m = max length of a full name from the split loop
 * Space:   O(n) linear
 */
function addHonorificTrinh(honorific, fullNames) {
    // const namesWithHonorific = [];
    let len = fullNames.length;
    for (let i=0; i < len; i++) {
        let rawName = fullNames[i];
        //find start position of first name
        let startF = rawName.search(",")+2
        let lastName = "", firstName = "";
        for (let j = 0; j < startF-2; j++) {
            lastName += rawName[j];
        }
        for (let k = startF; k < rawName.length; k++) {
            firstName += rawName[k];
        }
        let name = honorific + " " + firstName + " " + lastName;
        fullNames[i] = name;
    }
    return fullNames;
}
function addHonorific(honorific, fullNames) {
    const namesWithHonorific = [];
  
    for (const fullName of fullNames) {
      let firstName = "",
        lastName = "",
        commaFound = false;
  
      for (let i = 0; i < fullName.length; i++) {
        const char = fullName[i];
  
        if (char === ",") {
          commaFound = true;
        }
        if (char !== " " && char !== ",") {
          if (commaFound === false) {
            lastName += char;
          } else {
            firstName += char;
          }
        }
      }
      namesWithHonorific.push(`${honorific} ${firstName} ${lastName}`);
    }
    return namesWithHonorific;
  }

// function addHonorificFunctional(honorific, fullNames) {
//     return fullNames.map((fullName) => {
//       const [lastName, firstName] = fullName.split(", ");
//       return `${honorific} ${firstName} ${lastName}`;
//     });
//   }

function addHonorificFunctionalReduce(honorific, fullNames) {
    return fullNames.map((fullName) =>
      fullName
        .split(", ")
        .reduce((lastName, firstName) => `${honorific} ${firstName} ${lastName}`)
    );
}
function addHonorificSplit(honorific, fullNames) {
    const namesWithHonorific = [];
  
    for (const fullName of fullNames) {
      const [lastName, firstName] = fullName.split(", ");
      namesWithHonorific.push(`${honorific} ${firstName} ${lastName}`);
    }
    return namesWithHonorific;
  }



const honorific2 = "Sir";
const names2 = ["Sanchez, Rick", "Smith, Jerry"];
const expected2 = ["Sir Rick Sanchez", "Sir Jerry Smith"];
console.log(addHonorificSplit(honorific2, names2));
console.log(addHonorificTrinh(honorific2, names2));
console.log(addHonorific(honorific2, names2));
console.log(addHonorificFunctionalReduce(honorific2, names2));
// console.log(addHonorificFunctional(honorific2, names2));
