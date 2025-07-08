import os
from PyPDF2 import PdfMerger

os.chdir(os.path.dirname(__file__))  
print(" Current working directory:", os.getcwd())

merger = PdfMerger()
num = int(input("How many pdfs do you want to merge? "))

for i in range(num):
    pdf = input(f"Enter the name of pdf {i+1}: ")
    try:
        merger.append(pdf)
    except FileNotFoundError:
        print(f" File not found: {pdf}")
        exit(1)

output = input("Enter the name for output pdf (e.g., merged.pdf): ")
merger.write(output)
merger.close()

print(f" Merged into: {output}")
