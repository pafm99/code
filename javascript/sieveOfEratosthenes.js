// Sieve of Eratosthenes
// returns all of the prime numbers up to the given numbers
// A Prime Number can be divided evenly only by 1, or itself. And it must be a whole number greater than 1. 
// Example: 5 can only be divided evenly by 1 or 5, so it is a prime number. But 6 can be divided evenly by 1, 2, 3 and 6 
//so it is NOT a prime number (it is a composite number).


function sieveOfEratosthenes(n){
    var primes = [];
    for (var i = 0; i <+ n; i++){
      primes[i] = true;
    }
    
    primes[0] = false;
    primes[1] = false;
    
    for (var i = 2; i <= Math.sqrt(n); i++){
      for (var j = 2; j * i <= n; j++){
        primes[i * j] = false;
      }
    }
    var result = [];
    for (var i = 0; i < primes.length; i++){
      if (primes[i]) result.push(i);
    }
    return result;
  }
  
  sieveOfEratosthenes(20);