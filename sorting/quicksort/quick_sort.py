# <<Introduction To Algorithms (3rd)>>  p170 ~ p173

def quick_sort(input_list):
	def partition(input_list,p,r):
		# p start from 1 instead of 0, r end with len(list) instead of len(list)-1
		x=input_list[r-1]
		i=p-2
		for j in range(p-1,r):
			if input_list[j]<=x:
				#print (input_list[j])
				i=i+1
				temp=input_list[i]
				input_list[i]=input_list[j]
				input_list[j]=temp
		temp=input_list[r-1]
		input_list[r-1]=input_list[i+1]
		input_list[i+1]=temp
		return i+2

	def quick_sort_recursion(input_list,p,r):
		if p<r:
			q=partition(input_list,p,r)
			quick_sort_recursion(input_list,p,q-2)
			quick_sort_recursion(input_list,q,r)
	quick_sort_recursion(input_list,1,len(input_list))
	return input_list