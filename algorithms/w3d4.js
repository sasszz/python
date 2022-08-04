// R - Read and Re-State
// I - Input - what is the function taking in 
// O - Output - what is the function spitting out 
// T - Talk - don't be a deer in headlights

// Walk - walk it through

// Create a function that, given a string, returns the string's acronym (first letter of each word capitalized)

function create_acronym() {
    var acronym = [];
    let text = "object oriented programming"
    const myArray = text.split(" ");
    for(let i = 0; i < myArray.length; i++) {
        acronym.push(myArray[0][0]);
        acronym.push(myArray[i+1]);
        }
    // text.toUpperCase(acronym);
    console.log(acronym)
}

create_acronym()

function acronymize(str) {
    let newArr = str.split(" ");
    let newStr = " ";
    for(let i = 0; i < newArr.length; i++) {
        let temp = newArr[i][0];
        newStr += temp.toUpperCase();
    }
    console.log(newStr);
}

acronymize("object oriented programming")