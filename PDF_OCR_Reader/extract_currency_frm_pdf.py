from price_parser import Price
from PDF_OCR_Reader.token_network import Token_Network


class Extract_Currency_Frm_PDF():

    def __init__(self):
        pass

    def extract_currency_frm_pdf(self, PDF_Info, p_distance):
        """
        extracts currency information from pdf data

        Args:
            PDF_Info (PDF_Information class objeact): pdf information extracted.
            p_distance (int): distance in pixel while looking for term in proximity

        Returns:
            none. updates PDF_Info with currency information.
            
        """
        TN =Token_Network()
        out_put = []
        # get all terms that have currency information
        self.search_currency_in_pdf(PDF_Info)  
        # verify currency found
        for currency in PDF_Info.RawCurrency:
            term = currency[0]
            currency_info = currency[1]
            key = TN.get_matching_key(PDF_Info.network, PDF_Info.get_indexes_with_pixel_info, term)
            # if term has both currency type and amount then term qualifies as currency
            if currency_info[0] and currency_info[1]:
                out_put.append([currency])
            # if term has amount and currency type is missing then look for currency type in right direction
            elif currency_info[1]:
                # only check for terms that qualfy as pure digits.(.and , are allowed)
                if self.is_ammount(PDF_Info.get_term(term)):
                    currency_found = self.get_currency_in_proximity(PDF_Info, key, p_distance)
                    if currency_found:
                        out_put.append([currency, currency_found])
            # if term has currency type and amount is missing then look for amount in right direction
            elif currency_info[0]:
                amount_found = self.get_amount_in_proximity(PDF_Info, key, p_distance)
                if amount_found:
                    out_put.append([currency, amount_found])
        PDF_Info.Currency = out_put


    def search_currency_in_pdf(self, PDF_Info):
        out_put = []
        for term in PDF_Info.cleanData:            
            p = Price.fromstring(PDF_Info.get_term(term))
            if p.amount or p.currency:
                out_put.append([term, [p.currency,p.amount, p.amount_text]])
        PDF_Info.RawCurrency = out_put
    
    def search_currency_in_string(self, p_str):           
        p = Price.fromstring(p_str)
        if p.amount or p.currency:
            return [p.currency,p.amount, p.amount_text]
    


    def get_currency_in_proximity(self, PDF_Info, p_key, p_distance):
        out_put = []
        terms_proximity = self.get_term_in_proximity(PDF_Info, p_key, p_distance)
        for term in terms_proximity:
            for currency in PDF_Info.RawCurrency:
                if currency[1][0]:
                    if not currency[1][1]:
                        if self.is_same(currency[0],term[0], PDF_Info.get_indexes_with_pixel_info):
                            out_put = currency
            break
        return out_put

    
    def get_amount_in_proximity(self, PDF_Info, p_key, p_distance):
        out_put = []
        terms_proximity = self.get_term_in_proximity(PDF_Info, p_key, p_distance)
        for term in terms_proximity:
            for currency in PDF_Info.RawCurrency:
                if currency[1][1]:
                    if not currency[1][0]:
                        if self.is_same(currency[0],term[0], PDF_Info.get_indexes_with_pixel_info):
                            out_put = currency
            break
        return out_put



    def get_term_in_proximity(self, PDF_Info, p_key, p_distance):
        out_put = []
        # for all terms that align with the p_key get all terms on right within 200 pixel distance
        terms = PDF_Info.network.get(p_key)
        if terms:
            for term in PDF_Info.network[p_key]:
                if PDF_Info.get_direction(term) == 'right' and PDF_Info.get_distance(term) < p_distance:
                    out_put.append(term)
                # all terms are sorted by distance, so if distance 
                if PDF_Info.get_distance(term) >= p_distance:
                    return out_put
        return out_put




    def is_ammount(self, term):
        # remove decimal
        term = term.replace('.','')
        # remove comma
        term = term.replace(',','')
        # all that should be left is a digit so we can use isdigit
        return term.isdigit()
    


    def is_same(self, term1, term2, get_indexes_with_pixel_info):
        match = True
        # if term lists are equal as it is, also akes care of both empty list
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

            
