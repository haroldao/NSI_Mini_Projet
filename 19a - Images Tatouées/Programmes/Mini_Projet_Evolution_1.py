from PIL import Image
def watermark_logo(input_image_path, output_image_path, pos_img):
    original_image=Image.open(input_image_path)
    watermark_logo=Image.open(output_image_path)

    size_watermark=(200,200)
    watermark_logo_size=watermark_logo(size_watermark)


    weight, height=original_image.size

    transparent=Image.new("RGBA",(weight, height) , (0,0,0,0))
    transparent.paste(original_image)
    transparent.paste(watermark_logo, pos_img, mask=watermark_logo_size)


    transparent.show()
    transparent.save(output_image_path)







if __name__ == '__main__':
    img='cathedrale.jpg'
    watermark_logo(img, "Arthur_Nom_Logo.png", pos_img=(0,0))
