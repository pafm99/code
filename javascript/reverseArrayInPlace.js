function reverseArrayInPlace(arr){
    //You only want to loop through half of the array
    for (var i = 0; i < arr.length/2; i++){
      var temp = arr[i];
      arr[i] = arr[arr.length-1 -i];
      arr[arr.length - 1 - i] = temp;
    }
    return arr;
  }
  
  reverseArrayInPlace([1,2,3,4,5,6,7]);