


def get_value(self, PDF_Info, p_key, p_value):
    l_net_work_values = PDF_Info.network[tuple(p_key)]
    for value in l_net_work_values:
        if self.is_same(p_value, value[0], PDF_Info.get_indexes_with_pixel_info):
            return value
    return []


def test_get_value(self):
        key = (5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0)
        term = [5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0]

        out_put =  self.x.get_value(self.PDF_Info, key, term)
        self.assertEqual(out_put,[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)])

        key = (5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0)
        term = [5, 1, 4, 1, 1, 4, 134, 973, 286, 67, 95, 'February', 0]

        out_put =  self.x.get_value(self.PDF_Info, key, term)
        self.assertEqual(out_put,[])

# -----------------------------------------------------------------------------------------------

def do_align(self, PDF_Info, p_list1, p_list2):
    for term1 in p_list1:
        l_net_work_values = PDF_Info.network[tuple(term1)]
        terms_between = []
        # print(l_net_work_values)
        for term2 in p_list2:
            for value in l_net_work_values:
                terms_between.append(value)
                # if direction is right or down
                if PDF_Info.get_direction(value) in ['right','down']:
                    if self.is_same(term2, value[0], PDF_Info.get_indexes_with_pixel_info):
                        return self.clean_data([term1, value, terms_between], PDF_Info.get_direction)

def test_do_align(self):
        list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]

        list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, ',', 1], [5, 1, 4, 1, 2, 6, 1609, 1056, 156, 53, 95, '2020', 0]]

        list3 = [[5, 1, 4, 1, 2, 4, 1179, 1056, 285, 67, 95, 'February', 0], [5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, '20', 0], [5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, ',', 1], [5, 1, 4, 1, 2, 6, 1609, 1056, 156, 53, 95, '2020', 0]]

        out_put = self.x.do_align(self.PDF_Info, list1, list2)
        for match in out_put:
            print('----------------')
            print(match)

# -----------------------------------------------------------------------------------------------
    