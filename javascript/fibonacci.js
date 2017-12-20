// Hints: 
// 1: Does not require a lot of code 
// 2: Base case deals with the fact that the first two numbers are always 1 and 1
// The Fibonacci Sequence is the sum of the previous 2 numbers
// Fibonacci Sequence; 1, 1, 2, 3, 4, 5, 8, 13, 21, 34, ...
// O(2^n) Time Complexity which is really bad

function fibonacci(position){
    // Base case
    if (position < 3) return 1;
    // recursive function
    else return fibonacci(position - 1) + fibonacci(position - 2);
  }
  
  fibonacci(12);