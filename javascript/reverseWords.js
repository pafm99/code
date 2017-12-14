function reverseWords(string){
    //reverse every word in the string
    var wordsArr = string.split(' ');
    var reversedWordsArr = [];
    
    wordsArr.forEach(word =>{
      var reversedWord = '';
      for (var i = word.length - 1; i >=0; i--){
        reversedWord += word[i];
      }
      reversedWordsArr.push(reversedWord);
    });
    
    return reversedWordsArr.join(' ');
  }
  
  reverseWords('paul franco');