from prepare_data_keywords import Prepare_Data_Keywords
from phrase_search import Phrase_Search

import re

class Extract_Dates_Frm_PDF():

    def __init__(self):
        pass


    def extract_dates_frm_pdf(self, PDF_Info, get_exact_match, p_distance):
        """
        extracts dates information from pdf data

        Args:
            PDF_Info (PDF_Information class objeact): pdf information extracted.
            p_distance (int): distance in pixel while looking for term in proximity

        Returns:
            none. updates PDF_Info with dates information.
            
        """
        PDK = Prepare_Data_Keywords()
        # scan pdf document to get dates
        self.search_dates_in_pdf(PDF_Info)
        # get unique dates
        dates_set = self.get_unique_dates(PDF_Info)
        date_tokens = {}
        # tokeniseall dates for search
        for date in dates_set:
            date_tokens[date] = PDK.tokenize_keyword(date)

        # search dates in term network so we can get the exact location of dates in document
        PS = Phrase_Search()
        for key in date_tokens:
            match = PS.search(PDF_Info, date_tokens[key], p_distance)
            if match:
                PDF_Info.keywords[(key, tuple(date_tokens[key]))] = get_exact_match(match,date_tokens[key])  


    def search_dates_in_pdf(self, PDF_Info):
        regEx = r'(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)?(?:\d{2,4})'
        regEx1 = r'(\d{1,4}([.\-/])\d{1,2}([.\-/])\d{1,4})'
        out_put = {}
        for line in PDF_Info.PDF_Lines:
            line = line[0][0]
            match = re.findall(regEx, line)  
            if match:
                out_put[line] = match
            match = re.findall(regEx1, line)  
            if match:
                if out_put.get(line):
                    out_put[line] = out_put[line] + [m[0] for m in match]
                else:
                    out_put[line] = [m[0] for m in match]
        PDF_Info.dates = out_put

    
    def get_unique_dates(self, PDF_Info):
        dates = {}
        dates = set()
        for key in PDF_Info.dates:
            for d in PDF_Info.dates[key]:
                dates.add(d)
        return dates