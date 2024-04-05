import pdfplumber
from io import StringIO
import pandas as pd
from helper import *

#! to parse the pdf
def pdf_reader(path):                                                   
    all_pages = []
    all_page_text = []

    with pdfplumber.open(path) as pdf:
   
        for page in pdf.pages:
            one_page = page.extract_tables()
            #one_page_text = page.extract_text()
            #all_page_text.append(one_page_text)

            all_pages.append(one_page)
    return all_pages

#! to convert dataframes into csv formated string and prepare the data to feed into LLM
def pdf_data_formatter(all_pages):                                      
    text_string = """"""
    for page in all_pages:
        for table in page:

            df = pd.DataFrame(table)
            
            csv_string = StringIO()                                     # to convert dataframe into csv formated string 
            df.to_csv(csv_string, index=False)
            csv_string.seek(0)
            single_table_csv = csv_string.read()
            
            text_string = text_string.replace("\x00","")                # to remove null character
            text_string = text_string + single_table_csv + "\n\n\n\n"   # to combine text string of all the tables in a page

    return text_string

if __name__ == "__main__":
    # path = './log_books/CPP_1_CRE_Log_Book.pdf'
    # path = './log_books/CPP-1 FCE Log Book.pdf'          
    path = './log_books/CPP-1 SCE Log Book.pdf'
    # path = './log_books/CRE reading book.pdf'

    all_pages = pdf_reader(path)               
    pdf_data = pdf_data_formatter(all_pages)            #.split("\r\n")

    page_no = 0
    bold_labels = extract_bold_words(path, page_no)
    large_font_text = font_based_extraction(path)

    print("pdf_data : \n",pdf_data,"\n\n")
    print("bold_labels : \n",bold_labels,"\n\n")
    print("large_font_text : \n",large_font_text,"\n\n")







