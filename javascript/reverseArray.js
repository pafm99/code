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

var x = [4,-10, 7, 9, 34, 52];

function reverse (a) {
  var b = []; 
  counter = 0;
  for (var i = a.length-1; i >= 0; i--) {
    b[counter] = a[i];
    counter += 1;
  }
  return b;
}

console.log(reverse(x));
