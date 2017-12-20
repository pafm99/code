// Memoized Fibonacci Function 

// Check to see if number already exists in chache
// if number is in cache, use that number
// if number is not in cache, calculate it and put it in the cache so it can be used multiple times in the future

// Runtime: O(n) - Linear


function fibMemo(index, cache){
    //index: index of number in fibonacci sequence
    // cache: an array used as memory
    cache = cache || [];
    //Base case
    if (cache[index]) return cache[index];
    else{
      if (index < 3) return 1;
      else{
        // recursive function 
        cache[index] = fibMemo(index - 1, cache) + fibMemo(index -2, cache);
      }
    }
    return cache[index];
    
  }
  fibMemo(50)