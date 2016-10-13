// Algorithms 10-12-16

SLL.Prototype.length = function(){
	var temp = this.head
	var counter = 0;
	while (temp.next){
		counter++
		temp = temp.next
	}
	return counter
}

SLL.Prototype.MMA = function(){
	if (!this.head){
		return null;
	}
	var temp = this.head;
	var sum = 0;
	var counter = 0;
	var max = temp.val;
	var min = temp.val;
	while (temp){
		if (temp.val > max){
			max = temp.val;
		}
		if (temp.val < min){
			min = temp.val;
		}
		sum += temp.val;
		count++;
		temp = temp.next;
	}
	return {"max": max; "min": min; "avg": (sum/counter)}
}