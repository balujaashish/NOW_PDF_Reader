# 00:'level'
# 01:'page_num'
# 02:'block_num'
# 03:'par_num'
# 04:'line_num'
# 05:'word_num'
# 06:'left'
# 07:'top'
# 08:'width'
# 09:'height'
# 10:'conf'
# 11:'text'
class PDF_Information():
    def __init__(self):
        self.rawData = []
        self.page_count = 0

        self.cleanData = []
        self.network = {}
        self.keywords = {}
        self.RawCurrency = []
        self.Currency = []
        self.integers = []
        self.decimals = []
        self.dates = []
        self.PDF_Lines = []

        self.Boxes = {}
        self.cells =[]
        self.box_terms = {}
        self.box_map = {}
        self.box_currency = []
        self.box_dates = []
        self.box_numbers = []
        self.box_decimals = []
        self.box_keywords = []


    def get_num_elements(self):
        return 12

    def get_order_term(self, e):
        return e[12]


    def get_order_value(self, e):
        return e[0][12]

    def get_term_dict_value(self,e):
        return e[0][11]



    def get_direction(self, e):
        return e[1][0]

    def get_distance(self, e):
        return e[1][1]



    def get_term_index(self):
        return 11
    
    def get_top_index(self):
        return 7

    def get_indexes_with_pixel_info(self):
        return [0,1,2,3,4,5,6,7,8,9,10]


    
    def get_term(self,e):
        return e[11]

    def get_top(self, e):
        return e[7]

    def get_left(self, e):
        return e[6]

    def get_height(self, e):
        return e[9]

    def get_width(self, e):
        return e[8]

    def get_page_height(self):
        return 100000


    
    def get_matching_key(self, term):
        out_put = []
        for key in self.network:
            match = True
            for i in self.get_indexes_with_pixel_info():
                if term[i] != key[i]:
                    match = False
            if match == True:
                out_put.append(list(key))
        return out_put