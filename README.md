# DigiFo


## data_extraction.py
This file contains functions related to extracting and formatting data from PDF files.

### Functions:
1. pdf_reader(path)
   
   - Purpose: Extracts tables from a PDF file.
   - Parameters:
        -- path (str): The file path of the PDF.
   - Returns:
        -- all_pages (list): A list containing tables extracted from each page of the PDF.

2. pdf_data_formatter(all_pages)
   
   - Purpose: Formats extracted tables into CSV format.
   - Parameters:
         -- all_pages (list): A list of tables extracted from PDF pages.
   - Returns:
         -- text_string (str): A string containing the CSV-formatted data from all tables.




## helper.py
This file contains functions for extracting specific text elements from PDF files.

### Functions:
1. extract_bold_words(path, page_no)

Purpose: Extracts bold text from a specific page of a PDF file.

Parameters:

   path (str): The file path of the PDF.

   page_no (int): The page number from which to extract bold text.

Returns:

   clean_text (str): Extracted bold text from the specified page.

2. font_based_extraction(path)

Purpose: Extracts text with font size greater than or equal to 12 from a PDF file.
Parameters:
path (str): The file path of the PDF.
Returns:
Extract_Data (list): List of text elements with font size greater than or equal to 12.
