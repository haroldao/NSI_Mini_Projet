#ARTHUR LOGO (Evolution 1)
from PIL import Image

def watermark_logo(input_image_path,input2_image_path, output_image_path, pos_img):
    #Importation des images nécessaires
    original_image=Image.open(input_image_path)
    watermark_logo=Image.open(input2_image_path)

    #Definitions de nouvelles variables pour redimensionner le logo NSI
    new_width=200
    new_height=50

    #Redimension du Logo
    watermark_logo=watermark_logo.resize((new_width, new_height))

    #Creation d'une image transparente pour le texte
    transparent=Image.new("RGBA",original_image.size, (0,0,0,0))

    #Copie de l'image originale sur l'image "transparent" vide
    transparent.paste(original_image)

    #Copie du watermark (suivi de quelques paramètres) sur l'image "transparent" vide
    transparent.paste(watermark_logo, pos_img, mask=watermark_logo)

    transparent.show()
    transparent.save(output_image_path) #Sauvegarde


if __name__ == '__main__':
    img='../Ressources/cathedrale.jpg'
    img2='../Ressources/Arthur_Logo.png'
    watermark_logo(img, img2, "../Rendus/Arthur_Nom_Logo.jpg", pos_img=(100,0))
