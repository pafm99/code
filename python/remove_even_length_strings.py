// Remove even length strings

my_strings = ['hello', 'push', 'test', 'scary', 'yes']

function removeEvenLengthStrings(arr){
  var new_arr = [];
  for (var i = 0; i < arr.length; i++){
    if (arr[i].length % 2 === 0){
      arr.splice(i, 2) // i = is the index 2 is how many i want to remove
    }
  }
  return arr;
}

removeEvenLengthStrings(my_strings);
