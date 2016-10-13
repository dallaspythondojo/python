<html>
<head>
  <title></title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>"
  <script type="text/javascript">
  /*
  $(docuemnt).ready(function(){
    // ... your assignment here
  });
  */
  
$ SLL.prototype.mma = (function(){
if(!this.head){
return null;
}
var temp = this.head;
var sum = 0;
var counter = 0;
var max = temp.val;
var min = temp.val;
while(temp){
if(temp.val > max){
max = temp.val;
}
if(temp.val < min){
min = temp.val;
}
sum += temp.val;
count ++;
temp = temp.next;
}
return{"max":max, "min":min, "avg":(sum/count)};
}

  });
  </script>
</head>
<body>

</body>
</html>