# clasificacion_imagenes_vulcanologicas
Creador de modelos para análisis automatizado de imágenes vulcanológicas con aprendizaje autónomo y ejecución del modelo clasificador.

# Requerimientos para utilización
- Instalación de Python3 y Keras (y jupyter lab para crear un modelo nuevo), las instrucciones para instalar Python3 a través de Miniconda se encuentran aquí: https://docs.conda.io/en/latest/miniconda.html.
Las instrucciones para instalar Keras se encuentran aquí: https://anaconda.org/conda-forge/keras
Para instalar jupyter lab: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

Se recomiendan por lo menos 4gb de RAM para un buen funcionamiento del programa.


# Clasificación con el modelo incluido
Al momento de escribir esta documentación, el modelo incluido es la version 1.0. Es utilizable para cualquier estratovolcán, ya que fue entrenado con volcanes de diferentes pates del mundo.

# Clasificación:
Descargar volcano_analysis1.0.h5 (se encuentra en .zip por el peso, hay que extraer) y clasifica.py, y en el mismo directorio. Crear una carpeta llamada "test_images", en la cual solo se encuentra otra carpeta llamada "test_container", dentro de la cual se colocan las imágenes a clasificar. Es necesaria esta carpeta interna para el funcionamiento correcto.

Si ya se tienen las imágenes en el órden deseado, solo se necesita correr este script de la siguiente forma: 

python clasifica.py

El modelo imprimirá un número del 0 al 1 indicando el nivel de confianza con el que determina si es una erupción o está inactivo, el 1 siendo mayor certeza de actividad, y el 0 inactividad.

No necesariamente indica el poder o alcance de la explosión, solo la certeza con la que cree clasificar un evento. Se puede confundir con climas sumamente nublados, o con imágenes que muestren el sol justamente encima de la caldera del volcán, y puede dar falsos positivos en estos casos; pero raramente dará un falso negativo, es decir, no ignorará los eventos reales, especialmente si contienen incandescencias visibles aunque sean pequeñas.

Si se requiere clasificar con otro modelo, hay que cambiar el nombre del modelo en clasifica.py y correrlo igual.


Ejemplo de la estructura:
├── clasifica.py
├── test_images
│   └── test_container
│       ├── a.jpg
│       ├── b.jpg
│       ├── c.jpg
│       ├── d.jpg
│       └── e.jpg
└── volcano_analysis1.0.h5


# PRECAUCIÓN
Evite confusiones.
Muestra los resultados en el orden alfanumérico de los archivos. Por ejemplo: si en la carpeta se encuentran 1.jpg, 2.jpg, 11.jpg, serán leídas en el siguiente orden: 1.jpg, 11.jpg, 2.jpg. Es más un órden de  diccionario que numérico.


# CREACIÓN DE MODELOS NUEVOS
Dentro de "creacion_de_modelo_volcanico.ipynb" se encuentra detallado el proceso de creación y detalles del modelo. Si se requiere crear un modelo con un set de imágenes nuevas, se debe de correr este script nuevamente sin cambiar nada más que el nombre del archivo final en model.save("ejemplo_nombre.h5")  ojo, puede tardar una hora o más según la potencia de la computadora. Se creará un nuevo archivo con el nombre declarado en .save() .

Antes de correrlo, se debe de crear una estructura de dos directorios ("train" y "validation"), las cuales a su vez contienen sudirectorios llamados "0inactivo" y "1activo", las cuales corresponden a las clases de imágenes. ES DE SUMA IMPORTANCIA MANTENER CADA CLASE LIMPIAMENTE DISCERNIBLE DE LA OTRA O EL MODELO NO SERVIRÁ BIEN, solo imágenes claramente activas en 1activo y viceversa.

Ejemplo visual de la estructura

images_crop
├── train
│      ├── 0inactivo
│      │   ├── 053094_result.jpg
│      │   ├── 19113850995_74422e1180_b_result.jpg
│      │   ├── 2221234682_252326bf9d_c.jpg
│      │   ├── 30357976288_c63c5becc2_c.jpg
│      │   ├── 3314314680_bf0fc39418_z.jpg
│      └── 1activo
│          ├── Cam1-20140312184211-01_result.jpg
│          ├── Cam1-20140312184217-01_result.jpg
│          ├── Cam1-20140312184229-01_result.jpg
│          ├── Erupción_en_el_volcán_Sabancaya,_Perú.jpg
├── validation
│       ├── 0inactivo
│       │   ├── 12.jpg
│       │   ├── 8219088696_919eb19d9b_c.jpg
│       │   ├── 9.jpg
│       │   └── m02_00517027.jpg
│       └── 1activo
│           ├── 10.jpg
│           ├── 13701955364_f955a3e9d1_c.jpg
│           ├── 1.jpeg


Le agradezco a la Universidad de Colima todo el apoyo para desarrollar este proyecto
Asesores:
Dr. Arturo García González
Dra. Erika M. Ramos Michel
 

Con participación y ayuda de :
Ingeniero Gerardo Manzanilla Aznarez por la formación sobre la importancia de la mantenibilidad del software.
Dr. María Eugenia Cabello Espinosa por ayudarme a definir conceptos
Dr. Mauricio Bretón González por motivarme a este reto
M.C.  Alex Whitsil por su ayuda técnica y amabilidad inmediata
Autor: Rodrigo Ascencio Flores
rascencio@ucol.mx, yiyoascen@gmail.com  

