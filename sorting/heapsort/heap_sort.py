# <<Introduction To Algorithms (3rd)>>  p151 ~ p159

def min_heapify(input_list,node_index):
	l=node_index*2
	r=node_index*2+1
	heap_size=len(input_list)
	heap_list=input_list
	if l<heap_size and heap_list[l-1]<heap_list[node_index-1]:
		smallest=l
	else:
		smallest=node_index
	if r<heap_size and heap_list[r-1]<heap_list[smallest-1]:
		smallest=r
	if not smallest==node_index:
		temp=heap_list[node_index-1]
		heap_list[node_index-1]=heap_list[smallest-1]
		heap_list[smallest-1]=temp
		min_heapify(heap_list,smallest)
	return heap_list

def build_min_heap(input_list):
	heap_height=int((len(input_list)-1)/2)
	for i in range(heap_height):
		node_index=heap_height-i
		input_list=min_heapify(input_list,node_index)
	return input_list

def heap_sort(input_list):
	output_list=[]
	input_list=build_min_heap(input_list)
	node_index=len(input_list)
	while node_index>1:
		output_list.append(input_list[0])
		input_list[0]=input_list[node_index-1]
		input_list=input_list[:node_index-1]
		input_list=min_heapify(input_list,1)
		node_index-=1
	output_list=output_list+input_list
	return output_list

