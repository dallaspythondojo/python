function rBinSearch(arr, val){
  var mid = Math.floor (arr.length/2)
  var new = []
  if(arr[mid]== val){
    return True
  }
  else if(arr.length<=3){
    if(arr[0]==val|| arr[length-1] == val){
      return True
    }
    else {
      return False
    }
  }
  else if(arr[mid]>val){
    new = arr.slice(0, mid)
  }
  else {
    new = arr.slice(mid, arr.length){
    }
  }
  return rBinSearch(new, val)
}
