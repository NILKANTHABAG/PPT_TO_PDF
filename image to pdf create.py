from PIL import Image
import os
from PyPDF2 import PdfReader, PdfWriter

def convert_jpg_to_pdf(image_path, output_path):
    image = Image.open(image_path)
    pdf_path = output_path + ".pdf"
    image.save(pdf_path, "PDF", resolution=100.0)
    print(f"Converted {image_path} to {pdf_path}")

def merge_pdfs(pdf_paths, output_path):
    pdf_writer = PdfWriter()

    for pdf_path in pdf_paths:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)

    print(f"Merged PDFs into {output_path}")

# Example usage
# change the image directory where images are there
image_directory = r"E:\test\photo" 
# give the adress where you want to save the file
output_pdf = r"E:\test\output.pdf"

# Convert all JPG images to PDFs
pdf_paths = []
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_directory, filename)
        convert_jpg_to_pdf(image_path, image_path)
        pdf_paths.append(image_path + ".pdf")

# Merge all converted PDFs into a single PDF file
merge_pdfs(pdf_paths, output_pdf)
