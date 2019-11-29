#ICN Logo (Evolution 2)
from PIL import Image

def watermark_logo(input_image_path, input2_image_path, output_image_path, pos_img):
    #Import des images
    original_image=Image.open(input_image_path).convert("RGBA")
    watermark_logo=Image.open(input2_image_path)

    #Definitions de nouvelles variables pour redimensionner le logo NSI
    new_width=50
    new_height=50

    #Redimension du Logo
    watermark_logo=watermark_logo.resize((new_width, new_height))

    #Nouvelle variation qui convient une image vide transparente
    transparent=Image.new("RGBA", original_image.size , (0,0,0,0))

    #Collage de l'image en fond
    transparent.paste(original_image)

    #Collage du Watermak_Logo(NSI) et attribution du paramètre pos_img(Position)
    transparent.paste(watermark_logo, pos_img)

    #transparent = Image.alpha_composite(original_image, watermark_logo) 

    transparent.show()
    transparent.save(output_image_path)

if __name__ == '__main__':
    img='../Ressources/cathedrale.jpg'
    img_2='../Ressources/NSI_Logo.png'
    watermark_logo(img, img_2, "../Rendus/NSI_Logo.jpg", pos_img=(100,0))
