function remove_dup(str){
    var newstr = "";
    var obj = {};
    for (var i = 0; i < str.length; i++){
      if (!obj[str[i]]){
        newstr += str[i];
        obj[str[i]] = true;
      }
    }
    return newstr;
  }
remove_dup("mommy");