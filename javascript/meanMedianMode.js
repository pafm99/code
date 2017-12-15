function meanMedianMode(array) {
return {
    mean: getMean(array),
    median: getMedian(array),
    mode: getMode(array)
}
}

function getMean(array) {
var sum = 0;

array.forEach(num => {
    sum += num;
});

var mean = sum / array.length;
return mean;
}

function getMedian(array) {
array.sort(function(a, b){return a-b});
var median;

if (array.length % 2 !== 0) {
    median = array[Math.floor(array.length / 2)];
}
else {
    var mid1 = array[(array.length / 2) - 1];
    var mid2 = array[array.length / 2];
    median = (mid1 + mid2) / 2;
}

return median;
}

function getMode(array) {
var modeObj = {};

// create modeObj
array.forEach(num => {
    if (!modeObj[num]) modeObj[num] = 0;
    modeObj[num]++;
});

// create array of mode/s 
var maxFrequency = 0;
var modes = [];
for (var num in modeObj) {
    if (modeObj[num] > maxFrequency) {
    modes = [num];
    maxFrequency = modeObj[num];
    }
    else if (modeObj[num] === maxFrequency) modes.push(num);
}
// if every value appears same amount of times 
if (modes.length === Object.keys(modeObj).length) modes = [];
return modes;
}


meanMedianMode([9,10,23,10,23,9]);

//option 2
// function getMean(array){
//     var sum = 0;
//     array.forEach(num =>{
//       sum += num;
//     });
//     var mean = sum / array.length;
//     return mean
//   }
  
//   function getMedian(array){
//     array.sort(function(a,b){
//       return a - b;
//     });
//     var median;
//     if (array.length % 2 !== 0){
//       median = arr[Math.floor(array.length/2)];
//     }
//     else {
//       var mid1 = array[array.length / 2 - 1]
//       var mid2 = array[array.length / 2]
//       median = (mid1 + mid2) / 2;
//     }
//     return median;
//   }
  
//   function getMode(array){
//     var modeObject = {};
//     array.forEach(num =>{
//       if (!modeObject[num]) modeObject[num] = 0;
//       modeObject[num]++;
//     });
//     var maxFrequency = 0;
//     var modes = [];
//     for (var num in modeObject){
//       if (modeObject[num] > maxFrequency){
//         modes = [num];
//         maxFrequency = modeObject[num];
//       }
//       else if (modeObject[num] === maxFrequency){
//         modes.push(num)
//       }
//     if (modes.length === Object.keys(modeObject).length){
//       modes = [];
//     }
//     return modes;
//     }
//   }
  
//   function meanMedianMode(array){
//     return {
//       mean: getMean(array),
//       median: getMedian(array),
//       mode: getMode(array)
//     };
//   }
  
//   meanMedianMode([1,2,3,4,5,4,6,1]);