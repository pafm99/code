//Remove Negatives
function remove_negatives(arr){
    var idx = 0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]>0){
            arr[idx] = arr[i];
            idx++;
        }
    }
    arr.length = idx
}

