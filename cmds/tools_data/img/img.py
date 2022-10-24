from PIL import Image
import pytesseract
import requests
import function
import os

IMG_PATH = './cmds/tools_data/img/temp.png'

def ocr(img_url, lang):
    
    with open(IMG_PATH, 'wb') as file:
        file.write(requests.get(img_url, headers={'user-agent': 'Mozilla/5.0'}).content)
    function.print_time('Saved temp.png successfully')
    text = pytesseract.image_to_string(Image.open(IMG_PATH), lang=lang)
    print(text)
    if text != '':
        text_list = []
        while True:
            text_list.append(text[:2000])
            text = text[2001:]
            if text == '':
                break
        print(text_list)
        function.print_time('Ocr successfully')
        return text_list

    else:
        function.print_time('Character not found')
        return ['***Character not found***']

def rotate(img_url, angle):
    with open(IMG_PATH, 'wb') as file:
        file.write(requests.get(img_url, headers={'user-agent': 'Mozilla/5.0'}).content)

    Image.open(IMG_PATH).rotate(angle, expand=1).save(IMG_PATH, quality=100)
    function.print_time('Saved temp.png successfully')
    for i in range(95, 0, -5):
        if os.path.getsize(IMG_PATH) >= 8388608:
            function.print_time(f'Picture size is larger than 8MB, resave it with quality {i}')
            Image.open(IMG_PATH).rotate(angle, expand=1).save(IMG_PATH, quality=i)
            function.print_time('Saved temp.png successfully')
        else:
            break
