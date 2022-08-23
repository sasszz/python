function deDupe(arr) {
    const expected = [];
    for(let num = arr[arr.length-1]; num > 0; num--) {
        console.log(num);
        expected.push(num);
    }
    return expected;
}

function deDuple(arr) {
    let i = 0;
    while(i < arr.length - 1) {
        if(arr[i] == arr[i+1]) {
            delete arr[i];
        }
        else {
            i++;
        }
    }
    return arr
}

console.log(deDuple([1,2,2,3,4,4,4,5]))