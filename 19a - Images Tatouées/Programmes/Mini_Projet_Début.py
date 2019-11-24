from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



def watermark_text(input_image_path, output_image_path, text, pos_text):
    original_image=Image.open(input_image_path)
    original_image.putalpha(10)
    drawing = ImageDraw.Draw(original_image)
    

    white_color=(255,255,255, 15)
    font= ImageFont.truetype("Montserrat-Bold.ttf", 40)
    drawing.text(pos_text, text, fill=white_color, font=font, align= "right")
    original_image.show()
    original_image.save(output_image_path)


if __name__ == '__main__':
    img= 'Nelson_IMG.jpg'
    watermark_text(img, "tatouage-lycee.jpg", text="Lycée Nelson Mandela", pos_text=(50,350) )


