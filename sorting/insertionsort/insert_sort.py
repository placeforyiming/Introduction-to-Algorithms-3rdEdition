# <<Introduction To Algorithms (3rd)>>  p16 ~ p19
def insert_sort(input_list):
	if len(input_list)<2:
		return input_list
	for j in range(1,len(input_list)):
		key=input_list[j]
		i=j-1
		while i>-1 and input_list[i]>key:
			input_list[i+1]=input_list[i]
			i=i-1
		input_list[i+1]=key
	return input_list
