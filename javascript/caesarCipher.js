// Every letter in the string gets shifted forward by the value passed in
// Will be able to handle negative numbers

function caesarCipher(str, num){
    //turn num into an appropriate value. Like if we get a number like 300 then turn it into an appropriate value.
    num = num % 26;
    // First: make our entire string into lowercase
    var lowerCaseString = str.toLowerCase();
    // Second: We want an alphabet array with every letter in the alphabet to reference when shifting every letter in our string
    var alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    // Third: Loop through every letter in our string and shift it the correct number of times
    var newString = '';
    for (var i = 0; i < lowerCaseString.length; i++){
      var currentLetter = lowerCaseString[i];
      //if currentLetter is a space add it to the new string
      if(currentLetter === ' '){
        newString += currentLetter;
        continue;
      }
      // determine were our current letter is in our alphabet array
      var currentIndex = alphabet.indexOf(currentLetter);
      //shift our current letter by the number passed into our function to get our new letter
      var newIndex = currentIndex + num;
      // If the new index is greater than 25 start back at the beggining of the alphabet array
      if (newIndex > 25) newIndex = newIndex - 26;
      // If number passed in is a negative number wrap the index backwards
      if (newIndex < 0) newIndex = 26 + newIndex;
      if (str[i] === str[i].toUpperCase()){
        // If letter in the string is upper cased keep it upper cased
        newString += alphabet[newIndex].toUpperCase();
      }
      else newString += alphabet[newIndex];
    }
    return newString;
    
  }
  
  caesarCipher('Zoo Keeper', 2);
  caesarCipher('Big Car', -16);
  caesarCipher('JavaScript', -900);