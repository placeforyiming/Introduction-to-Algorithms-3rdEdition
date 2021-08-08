# <<Introduction To Algorithms (3rd)>>  p162 ~ p164
from heap_sort import *

class Prior_min_Queue:

    def __init__(self):
        # supposed element is tuple (key,value)
        self.queue_list={}
        self.key_list_ordered=[]


    def insert(self,element):
        # element is expected a tuple with (cost,value)
        self.queue_list[element[0]]=element[1]
        self.key_list_ordered.append(float("inf"))
        self.decrease_key(len(self.key_list_ordered),element[0])
        

    def minimum(self):
        output=(self.key_list_ordered[0],self.queue_list[self.key_list_ordered[0]])
        return output

    def extract_min(self):
        if len(self.key_list_ordered)==0:
            print ("empty queue")
        else:
            output=(self.key_list_ordered[0],self.queue_list[self.key_list_ordered[0]])
            self.key_list_ordered[0]=self.key_list_ordered[len(self.key_list_ordered)-1]
            self.key_list_ordered=self.key_list_ordered[:len(self.key_list_ordered)-1]
            if len(self.key_list_ordered)>0:
                self.key_list_ordered=min_heapify(self.key_list_ordered,1)
            return output

    def decrease_key(self,index, new_key):
        # the first node has index 1 not 0
        if self.key_list_ordered[index-1]<=new_key:
            print ("New key is larger!")
        self.key_list_ordered[index-1]=new_key
        while index>1 and self.key_list_ordered[int(index/2)-1]>self.key_list_ordered[index-1]:
            temp=self.key_list_ordered[index-1]
            self.key_list_ordered[index-1]=self.key_list_ordered[int(index/2)-1]
            self.key_list_ordered[int(index/2)-1]=temp
            index=int(index/2)



