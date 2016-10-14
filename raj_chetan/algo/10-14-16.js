// Algorithms 10/14/16
SLL.Prototype.prepend = function (val, before){
	var runner = this.head
	if this.head = null {return false}
	while (runner.next.val != before){
		if(!runner.next){
			return this.head;
		}
		else{
			runner = runner.next
		}
	}
	var temp = runner.next;
	runner.next = new Node(val);
	runner.next.next = temp;
	return this.head
}

SLL.Prototype.append = function (val, after){
	var runner = this.head
	if (runner == null) {return false;}
	while (runner.val != after){
		if(!runner.next){
			return this.head;
		}
		else{
			runner = runner.next
		}
	}
	var temp = runner.next;
	runner.next = new Node(val);
	runner.next.next = temp;
	return this.head;
}

SLL.Prototype.remove = function(val){
	var runner = this.head;
	if (runner == null) {return this.head;}
	while (runner.next.val != val){
		if(!runner.next){
			return this.head;
		}
		else{
			runner = runner.next
		}
	}
	var temp = runner.next.next;
	runner.next.next = null;
	runner.next = temp;
}