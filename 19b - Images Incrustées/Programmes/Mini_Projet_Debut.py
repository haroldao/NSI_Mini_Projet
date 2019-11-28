from PIL import Image 
#https://stackoverflow.com/questions/35531932/pil-remove-background-image-from-image

def RemoveBG (input_image_puth, output_image_path):
    #Import de l'image + Transformation de l'image en RGBA pour travailler avec la transparence (ALPHA)
    original_image=Image.open(input_image_puth).convert("RGBA")

    #Lire les informations de l'image
    pixdata = original_image.load()

    #Recuperation des dimensions de l'image 
    width, height = original_image.size
    
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (0, 0, 255, 255):
                pixdata[x, y] = (0, 0, 0, 255)


    
    original_image.show()
    original_image.save(output_image_path, "PNG")

if __name__ == '__main__':
    img="../Ressources/presentatrice meteo.bmp"
    RemoveBG(img, "../Rendus/RemoveBG.png")

def Incrustation(bg_image):
    bg_image=Image.open(bg_image)
