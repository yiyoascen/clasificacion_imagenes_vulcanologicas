#  OBJETIVO DEL PROGRAMA:
#  Clasifica imágenes vulcanológicas a partir de un modelo guardado en el mismo
#  directorio en el que se encuentra este script
#  Genera un .txt de nombre (fecha)resultados.txt


# FORMA DE USO
# se ejecuta en la consola de comandos y genera
# necesita dos argumentos:
# el nombre de la carpeta con las imagenes
# y el nivel minimo de confianza
# ejemplo:  python clasifica_a_texto.py imagenes_naranjal .9

# PRECAUCIÓN
# Muestra los resultados en el orden alfanumérico de los archivos. Por
# ejemplo: si en la carpeta se encuentran 1.jpg, 2.jpg, 11.jpg, serán
# leídas en el siguiente orden: 1.jpg, 11.jpg, 2.jpg.


# importa las librerias necesarias
import argparse
import datetime
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

# importa el modelo a utilizar. Si se creó otro modelo nuevo,
# unicamente hay que cambiar el nombre del archivo en la siguiente linea:
model = load_model('volcano_analysis1.0.h5')

parser = argparse.ArgumentParser(
    description='define una carpeta con imágenes a clasificar y retorna un .txt')
parser.add_argument('folder', type=str)
parser.add_argument('nivel_confianza', type=float)
args = parser.parse_args()

test_datagen = ImageDataGenerator(rescale=1. / 255)

test_generator = test_datagen.flow_from_directory(
    args.folder,
    target_size=(255, 255),
    color_mode="rgb",
    shuffle=False,
    class_mode='binary',
    batch_size=1)

filenames = test_generator.filenames
nb_samples = len(filenames)


# Imprime el resultado de las clasificaciones
predict = model.predict_generator(test_generator, steps=nb_samples)
result = zip(predict, filenames)

f = open('%s.txt' % datetime.datetime.now(), 'w')
f.write('nivel de confianza, imagen' + '\n')
for i, j in result:
    if i >= args.nivel_confianza:
        read_data = f.write(str(i) + ' ' + j + '\n')
f.close()
print('exitosamente guardado a texto')
