from Intersect_list import Intersect_List
import queue
import multiprocessing
from multiprocessing import Queue, Process

class Intersect_Lists():

    def __init__(self):
        pass

    def Intersect_multi_lists(self, p_list1, p_position1, p_dict, p_position2):
        """
        intersect all items in dictionary with a sorted list.
        each time in dictionary has a key and a list
        
        Args:
            p_list1 (List 2-D): 2-D sorted list.
            p_position1 (int): position of terms in p_list1 2-D array(second dimension).
            p_list2 (dicionary): where key is the list name and values are list of keywords. 
            p_position2(queue): position of terms in p_list2 2-D array(second dimension).
   
        Returns:
            dictionary in this form:
            {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]]}
            first entry in found items is from list2
        """
        return_obj ={}
        # iterate over dictionary and intersect each list with p_list1
        for key in p_dict:
            l_result = self.Intersect_list_item(p_list1, p_position1, key, p_dict[key], p_position2)
            # add to result dictionary only if a match found
            if l_result:
                return_obj.update(l_result)
        return return_obj



    def Intersect_multi_lists_using_queue(self, p_list, p_position, p_input, p_key_position, p_result):
        """
        intersect a list with a sorted list, iterate over the list and call binary_search for each term.
        it will work fo multiprocessing where each process looks at queue for input to work with. and push the result inot p_result. each process keeps running he while loop till an exception occurs.
        Args:
            p_list (List 2-D): 2-D sorted list.
            p_position (int): position of terms in a 2-D array(second dimension).
            p_input (queue): the lists we want to intersect with p_list are in form of a queue. 
            p_result(queue): each process will push out the intersect result to p_result
   
        Returns:
            nothing adds result(dictionary) to queue
        """
        while True:
            try:
                '''
                    try to get task from the queue. get_nowait() function will 
                    raise queue.Empty exception if the queue is empty. 
                    queue(False) function would do the same task also.
                '''
                l_dict = p_input.get_nowait()
            except queue.Empty:

                break
            else:
                '''
                    if no exception has been raised, intersect the two lists by iterating over 
                    second list and search each term in list 1.
                '''
                l_key = ()
                l_list = []
                # read keyword and list 
                for key in l_dict:
                    l_key = key
                    l_list = l_dict[key]

                output_list = self.Intersect_list_item(p_list, p_position, l_key, l_list, p_key_position)
                if output_list:
                    p_result.put(output_list)

        return True

    def Intersect_multi_lists_using_MultiProcessing(self, p_list, p_position, p_dict, p_key_position):
        l_input = Queue()
        l_result = Queue()           
        no_cpu = multiprocessing.cpu_count()
        processes, out_put = [], {} 

        # put data in queue for process to read when executing the target function
        for key in p_dict:
            l_input.put({key:p_dict[key]})

        # creating processes
        for w in range(no_cpu):
            p = Process(target=self.Intersect_multi_lists_using_queue, args=(p_list, p_position, l_input, p_key_position, l_result))
            processes.append(p)
            p.start()

        # completing process
        for p in processes:
            p.join()
        
        # get result from queue updated by all processes
        while not l_result.empty():
            out_put.update(l_result.get_nowait())

        return out_put



    def Intersect_list_item(self, p_list1, p_position1, p_key, p_list2, p_position2):
        """
        intersect an item in dictionary with a sorted list.
        each time in dictionary has a key and a list
        
        Args:
            p_list1 (List 2-D): 2-D sorted list.
            p_position1 (int): position of terms in p_list1 2-D array(second dimension).
            p_key(immutable obj): key of dictionary item
            p_list2 (List 2-D): the lists we want to intersect with p_list1. 
            p_position2(queue): position of terms in p_list2 2-D array(second dimension).
   
        Returns:
            dictionary in this form:
            {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]]}
            first entry in found items is from list2
        """
        l_Intersect_list = Intersect_List()
        # intersect the two lists 
        return_obj =  l_Intersect_list.Intersect_2_lists(p_list1, p_position1, p_list2, p_position2)
        #  add key to dicionary only when a match found else return an empty dictionary
        if return_obj and p_key:
            return {p_key:return_obj}
        else: return {}
        
    