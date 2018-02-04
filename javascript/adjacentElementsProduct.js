function adjacentElements(arr) {
  product = -100;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] * arr[i - 1] > product) {
      product = arr[i] * arr[i - 1];
    }
  }
  return product;
}

let my_arr = [-1, 3, 4, 22, -5, 66, 23];
adjacentElements(my_arr);
