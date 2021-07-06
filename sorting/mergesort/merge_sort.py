# <<Introduction To Algorithms (3rd)>>  p30 ~ p34
def merge_sort(input_list):
	def merge_and_sort(A,p,r):
		if p+1<r:
			q=int((p+r)/2.0)
			temp_A_1=A[:q]
			temp_A_2=A[q:]
			sorted_A_1=merge_and_sort(temp_A_1,0 , len(temp_A_1))
			sorted_A_2=merge_and_sort(temp_A_2,0 ,len(temp_A_2))
			final_sorted_list=[]
			count_1=0
			count_2=0
			while (len(sorted_A_1)>count_1 and len(sorted_A_2)>count_2):
				if sorted_A_1[count_1]<sorted_A_2[count_2]:
					final_sorted_list.append(sorted_A_1[count_1])
					count_1+=1
				else:
					final_sorted_list.append(sorted_A_2[count_2])
					count_2+=1
			if len(sorted_A_1)>count_1:
				final_sorted_list=final_sorted_list+sorted_A_1[count_1:]
			if len(sorted_A_2)>count_2:
				final_sorted_list=final_sorted_list+sorted_A_2[count_2:]
			return final_sorted_list

		else:
			return [A[r-1]]
	return_list=merge_and_sort(input_list,0,len(input_list))
	return return_list
