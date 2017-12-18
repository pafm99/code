// Search for a given value (key) inside of a list (numArray)
// Runs in O (log on) run time -very performant
// Can be written as a recursive function

function binarySearch(numArray, key){
    var middleIdx = Math.floor(numArray.length /2);
    var middleElem = numArray[middleIdx];
    
    if (middleElem === key){
      return true;
    } else if (middleElem < key && numArray.length > 1){
      console.log(middleElem);
      return binarySearch(numArray.splice(middleIdx, numArray.length), key);
    } else if (middleElem > key && numArray.length > 1){
      console.log(middleElem);
      return binarySearch(numArray.splice(0, middleIdx), key);
    }
    else return false;
  }
  
  binarySearch([5, 7, 12, 16, 36, 39, 42, 56, 71], 66);