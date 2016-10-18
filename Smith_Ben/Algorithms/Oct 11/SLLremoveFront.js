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
  
$ SLL.prototype.removeFront=(function(){
if(!this.head){
return null;
}
var temp=this.head;
var removed;
if(temp.next){
this.head=temp.next;
removed=temp.val;
temp.next=null;
}
else{
removed=temp.val;
this.head=null;
}
return removed;
}
  });
  </script>
</head>
<body>

</body>
</html>