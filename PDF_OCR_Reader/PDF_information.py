
class PDF_Information():
    def __init__(self):
        self.rawData = []
        self.cleanData = []
        self.network = {}
        self.keywords = {}
        self.RawCurrency = []
        self.Currency = []
        self.integers = []
        self.decimals = []
        self.dates = []
        self.PDF_Lines = []

    

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


    
        

