# Comentarios

Este documento tiene la intencion de funcionar como referencia de comentarios.
Ir agregando comentarios en cada uno de sus documentos:


Dia 1:
Rodri: Input/Output en Python
Seba/Jimmy: Wrapper simple para calcular energía a partir de sys
Beto: Correr casos de referencia (Solucionar input)
Solucion: el programa esta usando standart input, por lo que lee cada linea del
archivo que se igresa luego de "<". (Importante notar que .res entrega las posiciones
de las particulas a tiempo 0.
```
./*.x < DIR/*.inp
```  

Medios de comunicacion/colaboracion: Funcion/Ventajas/
  - GitHub -> Personal branches inside DEV with comment file
  - Whatsapp group
  - Email group
  - Project management app.

**gitignore**
Se agregaron las terminaciones
```
*.so
*.pyc
*.dat
*.xyz
```
a la lista de ignorados.
Para forzar la sincronizacion, utilizar:
```
git add -f <file.ignored>
```

**Trello**
Se crea sistema de Manejo de Proyecto, deadlines y aviso segun integrante. (App Mobil)

**Estructura de ljmd.c**
Se genera un archivo de referencia con las estructuras y funciones de ljmd.c


#**ESTANDAR COMENTARIOS**

## En C (OJO, que los ``` ``` estan puestos por el MARKDOWN:code)
1. Comentario archivo (Al principio de archivo .c)
    ```
    /** Descripcion  archivo
    * Need to use
    *  ::
    *    <file>(function)(other)
    *
    */
    ```

2. Comentario en clases/funciones (Acordarse de indentar)
    ```
    /// Descripcion corta

    /** Descripcion larga
    *
    * Parameters
    * ----------
    * parametro : caracteristica (virtual, callable,etc)
    * Que es este parámetro
    *
    * Returns
    * -------
    * t : callable
    * The decorated test `t`.
    *
    * Examples
    * --------
    * Algun ejemplo?
    *
    */
    ```
3. Comentarios internos de codigo (indentados)
    ```
    /// comentario de codigo
    ```


## En Python
1. Comentario archivo (Al principio de archivo .py)
    """
    Descripcion corta archivo.

    Descripcion detallada archivo
    Need to use
      ::
        <file>(function)(other)

    """

2. Comentario en clases/funciones (Acordarse de indentar)
    """
    Descripcion corta

    Descripcion larga

    Parameters
    ----------
    parametro : caracteristica (virtual, callable,etc)
    Que es este parámetro

    Returns
    -------
    t : callable
    The decorated test `t`.

    Examples
    --------
    Algun ejemplo?

    """
3. Comentarios internos de codigo (indentados)
    """comentario de codigo"""
