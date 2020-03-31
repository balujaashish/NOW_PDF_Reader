import unittest
from Search_list import Search_List

class testSearchList(unittest.TestCase):

    def setUp(self):
        self.g_list = [[1,3,'awf'], [2,3,'bhd'], [3,3,'ciosd'], [2,3,'dkFf']]
        self.g_list1 = [[1,3,'awf'],[2,3,'awf'], [3,3,'bhd'], [4,3,'bhd'], [5,3,'bhd'], [6,3,'ciosd'], [7,3,'dkFf'], [8,3,'dkFf']]
        self.g_position = 3
        self.x = Search_List()

    

    def test_search_term_before_index(self):
        self.assertEqual(self.x.search_term_before_index(self.g_list1, self.g_position,'bhd',3),[[3, 3, 'bhd']])
        self.assertEqual(self.x.search_term_before_index(self.g_list1, self.g_position,'ciosd',5),[])
        self.assertEqual(self.x.search_term_before_index(self.g_list1, self.g_position,'awf',0),[])
        self.assertEqual(self.x.search_term_before_index(self.g_list1, self.g_position,'awf',1),[[1,3,'awf']])
        self.assertEqual(self.x.search_term_before_index(self.g_list1, self.g_position,'dkFf',6),[])
        self.assertEqual(self.x.search_term_before_index(self.g_list1, self.g_position,'dkFf',7),[[7,3,'dkFf']])
    

    def test_search_term_after_index(self):
        self.assertEqual(self.x.search_term_after_index(self.g_list1, self.g_position,'bhd',2),[[4,3,'bhd'], [5,3,'bhd']])
        self.assertEqual(self.x.search_term_after_index(self.g_list1, self.g_position,'ciosd',5),[])
        self.assertEqual(self.x.search_term_after_index(self.g_list1, self.g_position,'awf',0),[[2, 3, 'awf']])
        self.assertEqual(self.x.search_term_after_index(self.g_list1, self.g_position,'awf',1),[])
        self.assertEqual(self.x.search_term_after_index(self.g_list1, self.g_position,'dkFf',6),[[8, 3, 'dkFf']])
        self.assertEqual(self.x.search_term_after_index(self.g_list1, self.g_position,'dkFf',7),[])   


    def test_search_term_around_index(self):
        dnd = None
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'bhd',3),[[3, 3, 'bhd'], [4, 3, 'bhd'], [5, 3, 'bhd']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'bhd',2),[[3, 3, 'bhd'], [4, 3, 'bhd'], [5, 3, 'bhd']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'bhd',4),[[3, 3, 'bhd'], [4, 3, 'bhd'], [5, 3, 'bhd']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'ciosd',5),[[6, 3, 'ciosd']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'awf',0),[[1, 3, 'awf'], [2, 3, 'awf']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'awf',1),[[1, 3, 'awf'], [2, 3, 'awf']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'dkFf',6),[[7, 3, 'dkFf'], [8, 3, 'dkFf']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,'dkFf',7),[[7, 3, 'dkFf'], [8, 3, 'dkFf']])
        self.assertEqual(self.x.search_term_around_index(self.g_list1, self.g_position,dnd,dnd),[])
        

    def test_binary_search(self): 
        dnd = None   
        self.assertEqual(self.x.binary_search( self.g_list1, self.g_position,'bhd'),[[3, 3, 'bhd'], [4, 3, 'bhd'], [5, 3, 'bhd']])
        self.assertEqual(self.x.binary_search( self.g_list1, self.g_position,'awf'),[[1, 3, 'awf'], [2, 3, 'awf']])
        self.assertEqual(self.x.binary_search( self.g_list1, self.g_position,'ciosd'),[[6, 3, 'ciosd']])
        self.assertEqual(self.x.binary_search( self.g_list1, self.g_position,'dkFf'),[[7, 3, 'dkFf'], [8, 3, 'dkFf']])
        self.assertEqual(self.x.binary_search( self.g_list1, self.g_position,'kjsajkbasj'),[])
        self.assertEqual(self.x.binary_search( self.g_list1, self.g_position,dnd),[])


if __name__ == '__main__':
    unittest.main()