// Given a string,return a new string with the duplicates excludedBonus: Keep only the last instance of each character.


const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";


// De-dupes the given string.
// - Time: O(?).
// - Space: O(?).


function stringDedupe(str) { 
    obj = {};
    expected = "";
    for(let i = 0; i < str.length; i++) {
        if(obj[str[i]]) {
            obj[str[i]] ++;
        }
        else {
            obj[str[i]] = 1;
            expected += str[i]
        }
    }
    return expected;
    }

const string2 = "helloo";
console.log(stringDedupe(string2));