# clingo-testing
Compara el tiempo entre dos encodings distinto de un problema con clingo y los exporta como un CSV. Escrito para el ramo [IIC2613 @ PUC.](https://github.com/IIC2613) 
# Pasos de uso
1. Tus problemas deben estar en archivos `.lp` independientes en una carpeta llamada `problems`. Puedes encontrar un generador de problemas [aquí](https://gist.github.com/aecanales/7cd774485a8adff9dabc4afcf7d00e22) o [aquí.](https://github.com/IIC2613/Syllabus/issues/29)
2. Abre `test` en un editor texto. Cambia `bodegas.lp` por el nombre del encoding viejo, y cambia `parte_1.lp` por el nombre de tu encoding nuevo.
3. Corre `./test` en tu terminal.
4. El resultado final se guardará en `results.csv` para luego ser visualizado en algún programa como Microsoft Excel.
