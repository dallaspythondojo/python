def insert_val_at(index, my_list, value):
	if index >= len(my_list): # index out of range
		return False
	
	my_list.append(None)
	temp = None
	
	for i in range(len(my_list)):
		if i == index:
			temp = my_list[i]
			my_list[i] = value
			break
	
	# start at index after insertion and swap temp with current index
	for j in range(index + 1, len(my_list)):
		(my_list[j], temp) = (temp, my_list[j])
		
	return my_list
	