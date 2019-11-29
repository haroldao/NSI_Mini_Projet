from PIL import Image 
#https://stackoverflow.com/questions/35531932/pil-remove-background-image-from-image

def Incrustation (input_image_puth, input2_image_path, output_image_path):
    #Import de l'image + Transformation de l'image en RGBA pour travailler avec la transparence (ALPHA)
    original_image=Image.open(input_image_puth).convert("RGBA")
    background_image=Image.open(input2_image_path).convert("RGBA")
    #Lire les informations de l'image (les données des pixels)
    
    datas =original_image.getdata()
    # #Récuperation des dimensions de l'image 
    width, height = original_image.size
    # transparent = Image.new("RGBA", (width, height))
    newData=[]
    for p in datas:
        if p[0]== 0 and p[1]== 0 and p[2]== 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(p)
    
    original_image.putdata(newData)
    background_image.paste(original_image, (50,0), original_image)
    background_image.show()

if __name__ == '__main__':
    img="../Ressources/presentatrice meteo.bmp"
    img2="../Ressources/Carte meteo.bmp"
    Incrustation(img, img2, "../Rendus/Incrustation.png")

# Im 1 = P1
# im 2 = P2 (presentatrice)

# si p1 est bleu
# p=P1

# sinon
# p=p'1
