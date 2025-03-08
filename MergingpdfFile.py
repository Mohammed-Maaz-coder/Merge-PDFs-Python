from PyPDF2 import PdfWriter
import os

# Create a PDF merger object
merger = PdfWriter()

# Get all PDF files in the current directory
pdf_files = sorted([file for file in os.listdir() if file.endswith(".pdf")])  # Sorting ensures order

# Check if PDF files are found
if not pdf_files:
    print("No PDF files found in the directory.")
else:
    for pdf in pdf_files:
        try:
            merger.append(pdf)  # Append each PDF
        except Exception as e:
            print(f"Error merging {pdf}: {e}")

    # Save the merged PDF
    output_file = "merged-pdf.pdf"
    merger.write(output_file)
    merger.close()

    print(f"Merged PDF saved as: {output_file}")