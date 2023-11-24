# Criado por Matheus Zanivan Andrade | Multiple Image Converter


import os
from PIL import ImageEnhance, Image 
from pillow_heif import register_heif_opener

register_heif_opener()

def get_image_path() -> str:
    while True:
        images_path = input('Onde as imagens estão localizadas: ')
        if os.path.exists(images_path):
            return images_path        
        else:
            print('Caminho inválido')

if __name__ == '__main__':
    directory = get_image_path()
    test_folder = "testing_data"
    test_diretory = directory + '/' + test_folder
    path = os.path.join(directory,test_folder)
    # os.mkdir(path)

    # print('Criando novas imagens...')
    # files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.HEIC')]
    
    # for file in files:
    #     image = Image.open(os.path.join(directory, file))
    #     image.convert('RGB').save(os.path.join(directory, os.path.splitext(file)[0] + '.jpg'))


    # print('Deletando imagens antigas...')
    # trash = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.HEIC')]

    # for file in trash:
    #     file_to_delete = os.path.join(directory, file) 
    #     os.remove(file_to_delete)

    new_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    size = 200,200
    sizeZao = 400,400
    rand_float = 0.5
    
    # print('Gerando thumbnails 200x200...')
    # for file in new_files:
    #     image = Image.open(os.path.join(directory,file))
    #     image.thumbnail(size)
    #     image.save(test_diretory + '/' + '200x200'+ file )
    
    # print('Gerando thumbnails 400x400...')
    # for file in new_files:
    #     image = Image.open(os.path.join(directory,file))
    #     image.thumbnail(sizeZao)
    #     image.save(test_diretory + '/' + '400x400'+ file )

    # for file in new_files:
    #     image = Image.open(os.path.join(directory,file))
    #     enhancer = ImageEnhance.Brightness(image)
    #     new_image = enhancer.enhance(0.5)
    #     new_image.save(test_diretory + '/' + 'escura'+ file )


# /Users/zanivan/Desktop/TrainingData/Avião
# /Users/zanivan/Desktop/TrainingData/Teletubbies
# /Users/zanivan/Desktop/TrainingData/exhaust
	
