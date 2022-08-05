// /* 
//     Zip Arrays into Map
//     Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
//     Associative arrays are sometimes called maps because a key (string) maps to a value 
//  */

// const keys1 = ["abc", 3, "yo"];
// const vals1 = [42, "wassup", true];
// const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
// };

// const keys2 = [];
// const vals2 = [];
// const expected2 = {};

// /**
//  * Converts the given arrays of keys and values into an object.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<string>} keys
//  * @param {Array<any>} values
//  * @returns {Object} The object with the given keys and values.
//  */
// function zipArraysIntoMap(keys, values) { }

// var firstArray = ['John', 'David', 'Bob'];
// var secondArray = ['Mike', 'Sam', 'Carol'];
// var arrayOfObject = firstArray.map(function (value, index) {
//     return [value, secondArray[index]]
// });
// console.log("The First Array=");
// console.log(firstArray);
// console.log("The Second Array=");
// console.log(secondArray);
// console.log("The mix Of array object=");
// console.log(arrayOfObject);

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];

function newobj (arr1, arr2) {
    var expected = {};
    for(let i = 0; i < arr1.length; i++) {
        expected[arr1[i]] = arr2[i];
    }
    return expected;
}

console.log(newobj(keys1, vals1));