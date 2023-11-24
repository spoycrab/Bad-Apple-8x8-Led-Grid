import PIL.Image,glob
# ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
ASCII_BIN = ["1","0"]

def resizeImage(image, new_width):
    old_width, old_height = image.size
    new_height = new_width * old_height / old_width
    return image.resize((new_width, int(new_height)))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels: # pixel // (255/num de chars na lista)
        # ascii_str += ASCII_CHARS[pixel//25]
        ascii_str += ASCII_BIN[pixel//128] 
    return ascii_str

if __name__ == "__main__":

    ascii_list = []
    with open("output.txt","w") as o:
        for path in glob.glob('images/*.png'):
            try:
                image = PIL.Image.open(path)
            except:
                print(path, "Unable to find image ")


            image = image.resize((8,8))
            greyscale_image = to_greyscale(image)
            ascii_str = pixel_to_ascii(greyscale_image)
            ascii_str_len = len(ascii_str)
            ascii_img = ""
            hex_string = ""

            for i in range(0, ascii_str_len, image.width):
                hex_string += "%X" % int(ascii_str[i:i+image.width],2) #ffbdbd5c19999899

            hex_string = ("0x"+hex_string).lower() #0xffbdbd5c19999899
            o.write(f"{hex_string},\n")
            ascii_list.append(("0x"+hex_string).lower())
    print(ascii_list)
        

    

    # for i in range(0, ascii_str_len, image.width):
    #     ascii_img += ascii_str[i:i+image.width] + "\n"

    # with open("ascii_image.txt", "w", encoding="utf-8") as f:
    #     f.write(ascii_img)
