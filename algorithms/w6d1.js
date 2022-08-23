function whatChange(int) {
    newint = int;
    dict = {};
    if (newint >= 25) {
        x = Math.floor(newint / 25);
        dict['quaters'] = x;
        newint = newint % 25;
    }
    if (10 <= newint < 25) {
        y = Math.floor(newint / 10);
        dict['dime'] = y;
        newint = newint % 10;
    } 
    if (5 <= newint < 10) {
        z = Math.floor(newint / 5);
        dict['nickle'] = z;
        newint = newint % 5;
    } 
    if (1 <= newint < 5) {
        a = Math.floor(newint / 1);
        dict['pennies'] = a;
        newint = newint % 5;
        return dict
    }
}
console.log(whatChange(65));