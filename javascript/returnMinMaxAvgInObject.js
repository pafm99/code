my_arr = [3, 2, 22, 4, 34, 56, 28, -22]

function minMax(arr){
  var obj = {'max': 0, 'min': 0, 'avg': 0};
  var sum = 0;
  for (var x = 0; x < arr.length; x++){
    sum += arr[x];
    obj.avg = sum / arr.length;
    if (arr[x] > obj.max){
      obj.max = arr[x];
    }
    if (arr[x] < obj.min){
      obj.min = arr[x];
    }
  }
  return obj;
}

minMax(my_arr);
