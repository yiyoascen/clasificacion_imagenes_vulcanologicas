#  OBJETIVO DEL PROGRAMA:
#  Clasifica imágenes vulcanológicas a partir de un modelo guardado en el mismo
#  directorio en el que se encuentra este script

# FORMA DE USO
# Busca una carpeta llamada "test_images", en la cual solo se encuentra
# otra carpeta llamada "test_container",
# la cual contiene las imágenes a procesar.
# Si ya se tienen las imágenes en el órden deseado, solo se necesita correr
# este script de la siguiente forma: python clasifica.py

# PRECAUCIÓN
# Muestra los resultados en el orden alfanumérico de los archivos. Por
# ejemplo: si en la carpeta se encuentran 1.jpg, 2.jpg, 11.jpg, serán
# leídas en el siguiente orden: 1.jpg, 11.jpg, 2.jpg.


# importa las librerias necesarias
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

# importa el modelo a utilizar. Si se creó otro modelo nuevo,
# unicamente hay que cambiar el nombre del archivo en la siguiente linea:
model = load_model('volcano_analysis1.0.h5')

# Normalizan y extraen las imágenes del directorio 'test_images/'
# si desea cambiar el nombre de 'test_images'  hágalo aquí también
test_datagen = ImageDataGenerator(rescale=1. / 255)

test_generator = test_datagen.flow_from_directory(
    'test_images/',
    target_size=(255, 255),
    color_mode="rgb",
    shuffle=False,
    class_mode='binary',
    batch_size=1)

filenames = test_generator.filenames
nb_samples = len(filenames)


# Imprime el resultado de las clasificaciones
predict = model.predict_generator(test_generator, steps=nb_samples)
print(predict)
