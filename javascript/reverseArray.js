function reverseArr(input) {
    var ret = [];
    for(var i = input.length-1; i >= 0; i--) {
        ret.push(input[i]);
    }
    console.log(ret);
    return ret;
}

var a = [3,5,7,8]
var b = reverseArr(a);
