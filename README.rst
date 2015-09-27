Generador de certificados
--------------------------

Dado un archivo de datos `data.csv` con los datos `apellido, dni, nombre`, genera un pdf
con los certificados del curso


Uso
+++

::

   $ python3 make.py

El script pedirá algunos datos de entradas y creará un archivo `certificados.pdf` con un certificado por página


Dependencias
+++++++++++++

requiere `pdflatex`. En ubuntu::


    $ sudo apt-get install texlive-full


Créditos
+++++++++

Código latex original por Ing. Maximiliano Eschoyez


Customización
+++++++++++++


Se pueden editar `background.png`  y/o el template latex `BulkCertificados.tex`