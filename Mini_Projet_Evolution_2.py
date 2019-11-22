from PIL import Image
def watermark_logo(input_image_path, output_image_path, pos_img):
    original_image=Image.open(input_image_path)
    watermark_logo=Image.open(output_image_path)

    


    weight, height=original_image.size

    transparent=Image.new("RGBA",(weight, height) , (0,0,0,0))
    transparent.paste(original_image)
    transparent.paste(watermark_logo, pos_img, mask=watermark_logo)


    transparent.show()
    transparent.save(output_image_path)







if __name__ == '__main__':
    img='cathedrale.jpg'
    watermark_logo(img, "NSI_Logo.png", pos_img=(0,0))
