


class Term_Proximity():
    
    def __init__(self):
        pass

    def get_all_terms_in_proximity(self, p_align_terms, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term, p_distance):
        """
        returns the terms in proximity of a term.

        Args:
            p_aligned_terms (List): all terms aligned to a term. (from token network)
                    -> needs to be sorted by distance.
            p_get_direction (function): returns the direction of a term from another term.
            p_get_order_key (function): returns the order of a term in network key(1-D List).
            p_get_order_value (function): returns the order in network value(2-D List, has direction and distance).
            p_term (string): term around which we are looking for other terms.

        Returns:
            direction and distance of term2 from term1
        """
        # we will only be looking for terms in right and bottom
        l_match = []
        # get all terms with direction = equal(the terms were grouped together)
        first_equal = self.get_first_term_in_direction(p_align_terms, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term, 'equal', p_distance)
        # get all terms with direction = right
        first_right = self.get_first_term_in_direction(p_align_terms, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term,'right', p_distance)
        # get all terms with direction = down
        first_down = self.get_first_term_in_direction(p_align_terms, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term,'down', p_distance)  
        if first_equal:
            l_match = l_match + [first_equal]
        if first_right: 
            l_match = l_match + first_right
        if first_down: 
            l_match = l_match + first_down
        return l_match



    def get_first_term_in_direction(self, p_aligned_terms, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term, p_direction, p_distance):
        """
        returns the first term in proximity of a term in a direction.

        Args:
            p_aligned_terms (List): all terms aligned to a term. (from token network)
                    -> needs to be sorted by distance.
            p_get_direction (function): returns the direction of a term from another term.
            p_get_order_key (function): returns the order of a term in network key(1-D List).
            p_get_order_value (function): returns the order in network value(2-D List, has direction and distance).
            p_term (string): term around which we are looking for other terms.
            p_direction (string): direction we want to look for a term.

        Returns:
            direction and distance of term2 from term1
        """
        out_put = []
        distance = 0
        if p_direction == 'equal':
            return self.get_first_term_equal(p_aligned_terms, p_get_order_key, p_get_order_value, p_get_direction, p_term)
        else:
            for term in p_aligned_terms:
                if p_get_direction(term) == p_direction:
                    if distance == 0:
                        distance = p_get_distance(term)
                    if p_get_distance(term) < distance + 5 and distance <= p_distance:
                        out_put.append(term)
                    else: break
            return out_put

    def get_first_term_equal(self, p_term_network, p_get_order_key, p_get_order_value, p_get_direction, p_term):
        """
        returns the first term that was grouped together with p_term.

        Args:
            p_term_network (List): all terms aligned to a term. (from token network)
                    -> needs to be sorted by distance.
            p_get_order_key (function): returns the order of a term in network key(1-D List).
            p_get_order_value (function): returns the order in network value(2-D List, has direction and distance).
            p_get_direction (function): returns the direction of a term from another term.
            p_term (string): term around which we are looking for other terms.

        Returns:
            term in proximity that is eqal and has order greater than p_term
        """
        order = p_get_order_key(p_term)
        for term in p_term_network:
            # check for direction to be equal which should have distance 0 and should appear first, 
            # if direction is not equal we know it did not have an equl term and we can return.
            if  p_get_direction(term) == 'equal':
                if p_get_order_value(term) == order+1:
                    return term
            else:
                return []


    def get_next_term_in_direction(self, p_data, p_current, p_get_direction):
        """
        returns the next term in proximity of a term in direction of currect term.

        Args:
            p_data (List): all terms aligned to a term. (from token network)
                    -> needs to be sorted by distance.
            p_get_direction (function): returns the direction of a term from another term.
            p_current (List): term with location data and direction and distance information 

        Returns:
            next term to current term.
        """
        found = False
        direction = p_get_direction(p_current)
        # iterate over each term and if directions and current
        #  term match get the next term and return
        for term in p_data:
            if p_get_direction(term) == direction:
                if found == True:
                    return term
                if term == p_current:
                    found = True
        return []