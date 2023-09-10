import fitz # PyMuPDF
import io
from PIL import Image

def extract_text_and_images_from_pdf(pdf_path):
    text = ""
    images = []

    pdf_document = fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        
        # Extract text
        text += page.get_text()

        # Extract images
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_data = base_image["image"]

            # Convert image data to a PIL Image
            image = Image.open(io.BytesIO(image_data))
            images.append(image)
            
    pdf_document.close()
    
    return text, images

pdf_path = './1706.03762.pdf'
text, images = extract_text_and_images_from_pdf(pdf_path)
text.strip()
with open('abc.txt', 'w', encoding='utf-8') as f:
    f.write(text)

for i in range(len(images)):
    images[i].save('./' + str(i) + '.png')