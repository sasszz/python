// Given a string containing space separated words
// Reverse each word in the string.
// If you need to, use .split to start, then try to do it without.

// const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

// Reverses the letters in each words in the given space separated string of words. Does NOT reverse the order of the words themselves.
// - Time: O(?).
// - Space: O(?).
// @param {string} str Contains space separated words.
// @returns {string} The given string with each word's letters reversed.

function reverseWords(str) { 
    let strArr = str.split(" ");
    let newArr = [];
    for(let i = 0; i < strArr.length; i++) {
        var temp = "";
        for(let j = strArr[i].length-1; j >= 0; j--){
            temp += strArr[i][j];
        }
        newArr.push(temp);
    }
    console.log(newArr.join(' '));
}

const str1 = "hello world";
reverseWords(str1);