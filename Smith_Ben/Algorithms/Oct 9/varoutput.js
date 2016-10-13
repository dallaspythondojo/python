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
  
  var output = [0, 1];
$ (function fancy(num){
if(num < output.length){
return output[num];
}
else{
while(num >= output.length){
output[output.length]=output[output.length-2] + output[output.length-1];
}
return output[num];
}
}
  });
  </script>
</head>
<body>

</body>
</html>