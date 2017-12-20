function bubbleSort(array){
    for (var i = array.length; i > 0; i--){
      for (var j = 0; j < i; j++){
        if (array[j] > array[j + 1]){
          temp = array[j];
          array[j] = array[j + 1];
          array[j + 1] = temp;
        }
      }
    }
    return array;
  }
  
  bubbleSort([5, 3, 8, 1, 4, 13, 6, 7, 7]);