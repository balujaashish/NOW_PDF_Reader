

class Supporting_Data():

    def __init__(self, p_data):
        self.data = p_data

    def get(self, p_name):
        for key in self.data:
            if self.get_list_name(key) == p_name:
                return self.data[key]
    

    
    def get_term(self, e):
        return e[3]
    
    def get_list_name(self, e):
        return e[3]
