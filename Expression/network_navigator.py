
class Network_Navigtor():
    # navigates the etworkto return 
    def __init__(self):
        self.alignment_list = []
        self.direction = {}
        self.distance = {}


    def align(self, PDF_Info, p_list1, p_list2):  
        """
        check if any term in list1 aligns with any term in list2.

        Args:
            PDF_Info (PDF_Information class objeact): pdf information extracted.
            p_list1 (list): list of terms that could come from lets say a phrase.
            p_list2 (list): list of terms that could come from lets say a phrase.

        Returns:
            none. updates public property of this class:
                self.alignment_list , self.direction , self.distance
            
        """
        # before checking the alignment reset public properties.
        self.reset()
        # check if any term in list1 aligns with any term in list2
        self.alignment_list = self.get_alignment_list(PDF_Info, p_list1, p_list2)
        if self.alignment_list:
            p = []
            for o in self.alignment_list:
                p.append([o[0], [term[0] for term in o[1]]])
            # get direction details, count of terms alignment direction. 
            self.direction = self.get_direction(p, PDF_Info.get_direction)
            # get distance detail, min and maximum distance of aligning terms.
            self.distance = self.get_distance(p, PDF_Info.get_distance)
           

    def get_direction(self, p_alignment_list, get_direction):
        # get direction count of aligning terms
        out_put = {}
        direction = []
        # get all directions of aligning terms in a list then we will apply list count mentod.
        for l_alignment_term in p_alignment_list:
            direction = direction + [get_direction(term) for term in l_alignment_term[1]]
        out_put['right'] = direction.count('right')
        out_put['down'] = direction.count('down')
        out_put['equal'] = direction.count('equal')
        return out_put

    def get_distance(self, p_alignment_list, get_distance):
        # get minimum and maximum distance between twrms in both lists
        out_put = {}
        distance = []
        # default value will be -1
        out_put['min'] = -1
        out_put['max'] = -1
        # get all distances between terms in a list, then we will use min amd max methods on list.
        if p_alignment_list:
            for l_alignment_term in p_alignment_list:
                distance = distance + [get_distance(term) for term in l_alignment_term[1]]
            out_put['min'] = min(distance)
            out_put['max'] = max(distance)
        return out_put

         
    def get_alignment_list(self, PDF_Info, p_list1, p_list2):
        out_put = []
        # for each term in list1 check if it aligns with list2.
        for term in p_list1:
            # check if term aligns with p_list2 terms
            # returns list of terms that align and terms that fall between them
            term_align = self.get_alignment_term(PDF_Info, term, p_list2)
            if term_align:
                # from result set remove terms from between that are in list1 or list2.
                aligning_terms = self.remove_aligning_terms(term_align, p_list1+p_list2)
                out_put.append([term, aligning_terms])
        return out_put


    def get_alignment_term(self, PDF_Info, p_term, p_list):
        # scan network to check if term aligns with any term in p_list
        out_put = []
        # from term network gets terms that align with p_term,
        # we will check if any term in p_list is in the list of terms from network.
        align_values = PDF_Info.network.get(tuple(p_term))
        for term in p_list:
            term_in_between = []
            # traverse over each term in network alignment list to see if term from p_list exixts
            for value in align_values:
                # we will look only in two directions right and left and will also include split terms(equal)
                if PDF_Info.get_direction(value) in ['right', 'down', 'equal']:
                    # add term to in between to record all terms that fall in between two aligning terms, 
                    # this will be reset if match not found
                    term_in_between.append(value)
                    if value[0] ==  term:
                        # remove matched term from in between, pop will remove last added value to term
                        term_in_between.pop()
                        l_direction = PDF_Info.get_direction(value)
                        term_in_between = self.clean_data(term_in_between, PDF_Info.get_direction, l_direction)
                        out_put.append([value, term_in_between])
                        term_in_between =[]
                        break
        return out_put



    def is_same(self, term1, term2, get_indexes_with_pixel_info):
        match = True
        # if term lists are equal as it is, also takes care of both empty list
        if term1 == term2:
            return True
        # either one term is empty
        if not term1 or not term2:
            return False
        # check for pixel information
        for i in get_indexes_with_pixel_info():
            if term1[i] != term2[i]:
                match = False
        return match

    def clean_data(self, p_list, get_direction, p_direction):
        # remove terms which dont fall in the direction, used to clean in between terms
        out_put = []
        for value in p_list:
            if get_direction(value) == p_direction:
                out_put.append(value)
        return out_put

    def remove_aligning_terms(self, p_list, p_aligning_terms):
        # remove terms from "between" that are art of lists we are checking for alignment in this class.
        out_put= []
        for term in p_list:
            between_term = term[1]
            # get a copy of between list to maintain original copy as is.
            between_term_i = between_term.copy()
            # intersect two lists and remove common terms from "between"
            for b_term in between_term_i:
                if b_term[0] in p_aligning_terms:
                    between_term.remove(b_term)
            out_put.append([term[0], between_term])
        return out_put


    def reset(self):
        self.alignment_list = []
        self.direction = {}
        self.distance = {}  

        