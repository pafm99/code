function factorial(num){
    // A recursive function will continue to call itself until the base case is satisfied
    if (num === 1){
      return num;
    }
    else{
      return num * factorial(num -1);
    }
  }
  factorial(10);