import pdfplumber
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar,LTLine,LAParams
import os

#! Function is used to extract word with bold text
def extract_bold_words(path, page_no):
    with pdfplumber.open(path) as pdf: 
        text = pdf.pages[0]
        clean_text = text.filter(lambda obj: (obj["object_type"] == "char" and "Bold" in obj["fontname"]))
        return clean_text.extract_text()

#! Function is used to extract words with font more than 12
def font_based_extraction(path):

    Extract_Data=[]

    for page_layout in extract_pages(path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    for character in text_line:
                        if isinstance(character, LTChar):
                            Font_size=character.size

                if Font_size >= 12:
                    Extract_Data.append([(element.get_text())]) # Font_size,

    def get_element(x):
        return x[0].replace("","")

    return list(
                            map(get_element,Extract_Data)
                    )
             

if __name__ == "__main__":

    path = "./log_books/CPP-1 SCE Log Book.pdf"
    page_no = 0

    font_based_extraction(path)
    extract_bold_words(path, page_no)

