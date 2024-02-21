import PyPDF2
import string

# Open the PDF file
with open('XI GIST 4 2023-2024.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize an empty string to store the extracted text
    extracted_text = ''

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Extract the text from the current page
        page = pdf_reader.pages[page_num]
        extracted_text += page.extract_text()

# Initialize a dictionary to store the count of each alphabet and number
alphabet_count = {char: 0 for char in string.ascii_lowercase}
number_count = {str(num): 0 for num in range(10)}

# Iterate over the extracted text
for char in extracted_text.lower():
    # If the character is an alphabet, increment its count
    if char in alphabet_count:
        alphabet_count[char] += 1
    # If the character is a number, increment its count
    elif char in number_count:
        number_count[char] += 1

# Open the text file in write mode
with open('output.txt', 'w') as txt_file:
    # Write the count of each alphabet to the text file
    for alphabet, count in alphabet_count.items():
        txt_file.write(f'{alphabet}: {count}\n')
    
    # Write the count of each number to the text file
    for number, count in number_count.items():
        txt_file.write(f'{number}: {count}\n')
