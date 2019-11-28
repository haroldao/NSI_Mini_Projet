from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#https://stackoverflow.com/questions/47123649/pil-draw-trans<parent-text-on-top-of-an-image
# https://pillow.readthedocs.io/en/4.2.x/reference/ImageDraw.html#example-draw-partial-opacity-text


def watermark_text(input_image_path, output_image_path, text, pos_text):
    #Importation de l'image de fond
    original_image=Image.open(input_image_path).convert("RGBA")

    #Nouvelle variation avec une image vide transparente
    txt = Image.new('RGBA', original_image.size, (255,255,255,0))

    #Avoir un contexte pour dessiner
    drawing = ImageDraw.Draw(txt)

    #Definition de la couleur
    color=(0,0,0, 80)

    #Importation d'une police (en local)
    font= ImageFont.truetype(".../Montserrat-Bold.ttf", 40)

    #Dessin du texte avec plusieurs paramètres (Position, texte, police, alignement )
    drawing.text(pos_text, text, fill=color, font=font, align= "right")

    final_image = Image.alpha_composite(original_image, txt) 
    final_image.show()
    final_image.save(output_image_path)


if __name__ == '__main__':
    img= '../Ressources/Nelson_IMG.jpg'
    watermark_text(img, "../Rendus/tatouage-lycee.jpg", text="Lycée Nelson Mandela", pos_text=(50,350) )


