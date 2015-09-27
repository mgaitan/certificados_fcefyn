#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import tempfile


def main():
    profe = input('Profesor: ')
    curso = input('Titulo curso: ')
    duracion = input('Duración en hs: ')
    nrores = input('resolucion nº: ')
    mes = input('mes: ')
    year = input('año: ')

    datos = locals()

    with open('BulkCertificados.tex') as template:
        latex = template.read()
    for var, value in datos.items():
        latex = latex.replace('@{}@'.format(var.upper()), value)

    temp = tempfile.mkstemp(suffix='.tex', text=True)[1]
    with open(temp, 'w') as output:
        output.write(latex)

    subprocess.call(['pdflatex', "-jobname", "certificados", '-interaction', 'batchmode', temp])




if __name__ == '__main__':
    main()

