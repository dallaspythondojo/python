// Algorithms 10-13-16

SLL.Prototype.Back = function(){
	var temp = this.head;
	while (temp.next){
		temp = temp.next;
	}
	return temp.val;
}

SLL.Prototype.AddBack = function(){
	var temp = this.head;
	while (temp.next){
		temp = temp.next;
	}
	temp.next = new Node(val);
}

SLL.Prototype.reBack = function(){
	var temp = this.head;
	while (temp.next.next){
		temp = temp.next;
	}
	temp.next = null;
	return this.head;
}

