from PIL import Image 
#https://stackoverflow.com/questions/35531932/pil-remove-background-image-from-image

def Incrustation (input_image_puth, input2_image_path, output_image_path):
    #Import des images + Transformation de l'image en RGBA pour travailler avec la transparence (ALPHA)
    original_image=Image.open(input_image_puth).convert("RGBA")
    background_image=Image.open(input2_image_path).convert("RGBA")
    
    #Lire les informations de l'image (les données des pixels)
    datas =original_image.getdata()

    # #Récuperation des dimensions de l'image 
    width, height = original_image.size

    #Définition d'une liste vide pour les datas
    newData=[]

    for item in datas:
        if item[0]== 0 and item[1]== 0 and item[2]== 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    #Changement des datas de l'image (présentatrice)
    original_image.putdata(newData)

    #Copie de la présentatrice sur la carte météo
    background_image.paste(original_image, (50,0), original_image)
    background_image.show()

    #Enregistrement de l'image
    background_image.save(output_image_path)

if __name__ == '__main__':
    img="../Ressources/presentatrice meteo.bmp"
    img2="../Ressources/Carte meteo.bmp"
    Incrustation(img, img2, "../Rendus/Incrustation.bmp")
