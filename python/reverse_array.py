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
