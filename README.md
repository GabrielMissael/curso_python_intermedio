# Notas del Curso de Python: Comprehensions, Lambdas y Manejo de Errores 🐍

## Preparación antes de empezar

### El Zen de Python

- Fueron creados hace 20 años, por uno de los cofundadores de Python 🐍.
- ¿Qué es? Son los 20 principios de software que tiene Python para escribir nuestro código de manera correcta y precisa. 😄
- Para ver los 20 principios, hacemos *`import this`.* La lista completa:
    1. *Beautiful is better than ugly.*
    2. *Explicit is better than implicit.*
    3. *Simple is better than complex.*
    4. *Complex is better than complicated.*
    5. *Flat is better than nested.*
    6. *Sparse is better than dense.*
    7. *Readability counts.*
    8. *Special cases aren't special enough to break the rules.*
    9. *Although practicality beats purity.*
    10. *Errors should never pass silently.*
    11. *Unless explicitly silenced.*
    12. *In the face of ambiguity, refuse the temptation to guess.*
    13. *There should be one-- and preferably only one --obvious way to do it.*
    14. *Although that way may not be obvious at first unless you're Dutch.*
    15. *Now is better than never.*
    16. *Although never is often better than **right now.***
    17. *If the implementation is hard to explain, it's a bad idea.*
    18. *If the implementation is easy to explain, it may be a good idea.*
    19. *Namespaces are one honking great idea -- let's do more of those!*

[python-zen](https://zen-python-test.netlify.app/)

### ¿Qué es la documentación?

- La documentación es la información que nos explica como funciona un lenguaje o tecnología 😄 es como un manual de instrucciones. Nos explica detalladamente como operarlo y las características.
- La documentación de Python 🔥:

    [3.9.7 Documentation](https://docs.python.org/3/)

- Podemos encontrar tutoriales, referencias de la biblioteca, etc. 🤓.
- Los Índices PEP (Python Enhancement Proposals) son los documentos que conforman a toda la guía de estilos del lenguaje (como deberíamos escribirlo). El más importante es el **PEP8**, que nos explica las buenas prácticas que debemos seguir. 🤯 PEP8 es:

    [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Entorno virtual

### ¿Qué es un entorno virtual?

- Un módulo es código escrito por otra persona que a nosotros nos sirve para resolver un problema de manera rápida (no reinventar la rueda 😆).
- En principio, cada proyecto funciona dentro de nuestra instalación de Python, el cual tiene varios módulos. Cuando actualizamos un módulo para un proyecto, puede haber problemas con el resto de los proyectos 😵.
- Para resolver esto, usamos **entornos virtuales**, donde tenemos una *copia* de Python (aislada) en cada proyecto, con módulos independientes en cada entorno 😄.

### El primer paso profesional: Creación de un entorno virtual

- Podemos crear un entorno virtual para un proyecto en particular, dentro de una carpeta en específico (donde está el proyecto).
- Es recomendable iniciar un repositorio de Git para cada proyecto 😄.
- Para crear el entorno virtual, primero hacemos `python3 -m venv <nombre de ambiente>` , donde la bandera *-m* nos deja llamar a un módulo, en este caso `venv` de virtual environment. 🔥
- Una vez que hayamos creado el entorno virtual, debemos entrar en dicho entorno para comenzar a trabajar con el 🤔. Para esto, en WSL, usamos `source <nombre de ambiente>/bin/activate`. Para que sea más fácil usar esto, podemos crear un alias 👀.
- Para salir del entorno virtual usamos `deactivate`.
- Para crear un alías temporal en Ubuntu, es igual `alias <nombre>="<comando>"`. Pero para que quede de manera permanente, debes agregarlo al documento `.bashrc` (el mismo comando).

### Instalación de dependencias con pip

- `pip` dentro de Python es el *Package Installer for Python* 😃. Esto es ya que hay módulos de Python que no están instalados de fábrica como *Pandas*  o *Numpy*. Hay varios manejadores de módulos, como *pio, conda* o *pyenv.*
- Debemos usar `pip` dentro del entorno virtual donde queremos instalar dependencias.
- `pip freeze` nos dice que módulos tenemos instalados en ese momento.
- `pip install <nombre de módulo>` para instalar un módulo. Es muy similar a `npm` de JavaScript.
- Cuando instalas un módulo complejo (como Pandas) podrían instalarse más módulos del que este depende 🧭.
- Hay un caso particular: Si queremos compartir un proyecto, entonces es necesario que todos los desarrolladores tengan exactamente el mismo entorno virtual. Para eso, hacemos `pip freeze > requirements.txt`. Si tiene formato raro, también puedes usar `pip list --format=freeze > requirements.txt`.
- Luego, otra persona puede tener el mismo entorno con `pip install -r requirements.txt`.

### Una alternativa: Anaconda

- Anaconda es una alternativa muy famosa a `pip`. Es muy famosa para data science 🔥.
- Si ya tenías Conda instalado pero quieres decidir si usar Conda en un proyecto o usar Pip, puedes usar `conda config --set auto_activate_base false` para que no se active el base envirment de conda de manera automática y puedas usar tus envs creados como lo vimos en las clases pasadas 😄.

## Alternativa a los ciclos: Comprehensions

### Listas y diccionarios anidados

- Para ignorar el environment `env` lo agregamos en el archivo `.gitignore` 😃.
- Las listas y los diccionarios son estructuras de datos, ambas son maneras de organizar objetos. Las listas pueden almacenar diccionarios y los diccionarios listas 🤯.
- `if __name__=='__main__'` es el entry point del script 🐍.

    ```python
    def main():
        # Lists with dictionaries inside 😋
        super_list = [
            {'firstname':'Missael', 'lastname':'Barco'},
            {'firstname':'Gabriel', 'lastname':'Torres'},
            {'firstname':'David', 'lastname':'Mendoza'},
            {'firstname':'María', 'lastname':'García'}
        ]
    
        # Dictionaries with lists inside 👀
        super_dict = {
            'natural_nums':[1, 2, 3, 4, 5],
            'integer_nums':[-1, -2, 0, 1, 2],
            'floating_nums':[1.1, 4.5, 6.43]
        }
    
        # Check the content of the super_dict 🤔
        for key, value in super_dict.items():
            print(key, '=', value)
    
        # Check the content of the super_list 🔍
        for dictionarie in super_list:
            print(dictionarie)
    
    if __name__=='__main__':
        main()
    ```

### List comprehensions

- Algunas veces, queremos crear listas con ciertas características que se repiten. Podemos hacer esto con un ciclo loop, pero también con list comprehension 😃.
- La estructura general es: 🔥

    ```python
    list_comprehension = [function(element) for element in iterable if condition]
    ```

- Mi solución al reto 👀:

    ```python
    def filter_num(x):
        # Function to check if the number follow the rules
        return (x % 4 == 0 and x % 6 == 0 and x % 9 == 0 and x < 10**5)
    
    def main():
    
        # First, with a for loop 😀
        number_list1 = []
        for x in range(1, 10**5):
            if filter_num(x):
                number_list1.append(x)
    
        # Look at the first 10 terms
        print('With a for loop: ', number_list1[0:10])
    
        # Now, with list comprehension 🔥
        number_list2 = [x for x in range(1, 10**5) if filter_num(x)]
        print('With list comprehensions', number_list2[0:10])
    
        # Check if the lists are aqual
        if number_list1 == number_list2:
            print('They are equal 🎉')
        else:
            print('They are different 😟')
    
    if __name__ == '__main__':
        main()
    ```

### Dictionary comprehensions

- Lo mismo que hicimos con listas podemos hacerlo con diccionarios 👀.
- La estructura es la misma que con las listas:

    ```python
    my_dict = {key:value for value in iterable if condition}
    ```

- Mi solución al reto 😃:

    ```python
    def main():
    
        # First, with a for loop 😋
        dict_1 = {}
        for i in range(1, 1001):
            dict_1[i] = i**0.5
    
        # Print 5 elements of the dict
        five_keys1 = list(dict_1.keys())[0:5]
        print('With a for loop: ', [(i, dict_1[i]) for i in five_keys1])
    
        # Now, with dictionary comprehension 🔥
        dict_2 = {i: i**0.5 for i in range(1, 1001)}
    
        five_keys2 = list(dict_1.keys())[0:5]
        print('With dict comprehension: ', [(i, dict_2[i]) for i in five_keys2])
    
        # Check if the dicts are aqual
        if dict_1 == dict_2:
            print('They are equal 🎉')
        else:
            print('They are different 😟')
    
    if __name__ == '__main__':
        main()
    ```

## Conceptos avanzados de funciones

### Funciones anónimas: lambda

- Las funciones normales nos sirven para reutilizar código que se aplica en varias secciones. Sin embargo, hay otro tipo de funciones: lambda 😎.
- Son funciones si nombre o anónimas; estás no tienen un nombre. La estructura en general es:

    ```python
    lambda argumentos: expresión
    ```

- Las funciones lambda pueden tener los argumentos que queramos, pero **una sola línea de código.** 🤯
- Ejemplo con palíndromos:

    ```python
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))
    ```

    En este caso, `palindrome` es una variable que guarda un objeto de tipo función, no es la función en si misma.

- Código de la sesión:

    ```python
    def main():
        # With normal function
        def palindrome(string):
            return string == string[::-1]
        print('With normal function', palindrome('ana'))
    
        # With lambda function
        palindrome_lambda = lambda string: string == string[::-1]
        print('With lambda variable:', palindrome_lambda('ana'))
    
        # Check type of variable
        print('Type of variable:', type(palindrome_lambda))
    
    if __name__ == '__main__':
        main()
    ```

### High order functions: filter, map y reduce

- Una función de orden superior es una función que recibe como parámetro a otra función. 😆 Ejemplo de función de orden superior.
- En este caso, `saludo` es de orden superior ya que recibe una función como argumento.
- Hay **tres funciones de orden superior** que son muy importantes: filter, map y reduce.

```python
def saludo(func):
    func()
def hola():
    print("Holaaa!!!")
def adios():
    print("Adioooos!!")

saludo(hola)
saludo(adios)
```

- **Filter:** Recibe una función con la cual se filtran los elementos (Debe regresar True o False) de un iterable (esos son sus dos argumentos). La función `filter` regresa un iterator, que es un tipo especial de objeto, por lo que debemos pasarlo a tipo lista. 🔍

```python
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = list(filter(lambda x: x%2 !=0, my_list))
print(odd)
```

- **Map:** Recibe una función y un iterable. Aplica la función al iterable. De nuevo, debemos pasarlo a tipo lista. 🗺️

```python
my_list = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, my_list))
```

- **Reduce:** Recibe también una función y un iterable. Debe importarse del módulo `functools`. La función debe recibir dos elementos, y la función `reduce` regresa un único valor resultado de aplicar a pares el último resultado con el siguiente elemento del iterable. 🧠

```python
from functools import reduce

my_list = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a*b, my list)
```

### Proyecto: filtrando datos

- Tenemos una lista con diccionarios sobre distintas personas. 👀
- Cuando en Python colocamos una variable en mayúsculas, significa que no esperamos modificarla, esto es, es una constante ⛵.
- El operador pipe `|` te permite unir un diccionario viejo con uno nuevo, y es un feature nuevo de python 3.9 🤯 (sumar diccionarios).
- Solución al reto:

    ```python
    def main():
        all_python_devs = list(
            filter(lambda worker: worker['language'] == 'python', DATA))
        all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    
        all_platzi_devs = list(
            filter(lambda worker: worker['organization'] == 'Platzi', DATA))
        all_platzi_devs = list(map(lambda worker: worker['name'], all_platzi_devs))
    
        adults = [worker['name'] for worker in DATA if worker['age'] > 18]
        old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    
        print(all_python_devs, all_platzi_devs, adults, old_people)
    
    if __name__ == '__main__':
        main()
    ```

## Manejo de errores

### Los errores en el código

- Es muy normal equivocarse programando, y es cosa de todos los días: debemos aprender a recibir y manejar errores 🛑.
- Hay dos tipos de errores:
  - Error de lógica: Python no nos avisa: entonces nosotros programamos mal, y para resolverlo debemos revisar nuestro programa de principio a fin para encontrar donde falla. Una de las técnicas para resolver esto es debugging. 🧠
  - Cuando Python si nos avisa y nos devuelve un traceback.
- De cuando si nos avisa, entonces hay dos opciones:
  - SyntaxError: Cuando tenemos un typo o escribimos algo mal. Aquí se detiene el programa sin si quiera ejecutarse porque está mal escrito. 📕
  - Exception: Aquí si se ejecuta el código, pero la lógica se rompe en algún punto. Esto pasa en una línea específica, y todas las anteriores si se ejecutan. 😵
- Sobre Exception, los mas comúnes:
  - KeyboardInterrupt: Ocurre cuando pulsamos Ctrl + C en la consola 👽. Para poder cortar el proceso, eleva una excepción.
  - KeyError: Cuando queremos entrar a una llave de un diccionario que no existe.
  - IndexError: Similar al anterior, pero en listas.
  - FileNotFoundError: Como su nombre lo indica 😆
  - ZeroDivisionError: 👀
  - ImportError: Cuando intentas importar un módulo que no está funcionando.
- Dentro del mensaje que aparece cuando hay un error se encuentra el **traceback**, y la manera correcta de leerlo es leerlo del final al inicio. En este orden, la primera contiene el tipo de error. En la siguiente, el archivo donde sucedió el error, la línea y el módulo. 🤯 La antepenultima línea, aparece el traceback, y nos explica de donde parte el error.

### Debugging

- Una de las técnicas para resolver errores de lógica (cuando Python no nos avisa el error) es *debugging* o *depuración*. VSCode tiene esto como una de sus funcionalidades. 👀
- Cuando hacemos debugging, podemos poner *pausa* a nuestro programa e ir línea por línea viendo que sucede. Podemos avanzar en las líneas de código y, en caso que estemos sobre una línea que llama una función, podemos optar por entrar en esta 🤯.  Los botones del debugger:
  - pause → permite pausar la ejecución del programa
  - step over → permite avanzar un solo paso en el programa
  - step in → igresamos a un bloque secundario del programa (funciones)
  - step out → salimos del bloque secundario
  - restart → reinicia el programa
  - stop → detiene el programa
- Existen *break points* o puntos de quiebre 🛑 que nos sirve para detener nuestro programa en un punto específico, donde creamos que nuestro programa falla.

### Manejo de excepciones

- Try, except → Nos sirve para configurar acciones predeterminadas dado que sucede alguna Exception. 👀 El formato general es:

    ```python
    try: 
     <código>
    except <tipo de excepción> as <alias>:
     <otro código>
    ```

- raise → Esto nos sirve para manejar *errores* que python no reconoce como errores directamente. Con esto, nosotros creamos o definimos algo que si es un error.

    ```python
    if <condición>:
     raise <tipo de excepción>(<Mensaje>)
    ```

    Eso en principio interrumpe el programa (dado que es una excepción). Podemos poner esto dentro de un try-except.

- finally → Es muy rara de encontrar: cerrar archivos, conexiones y liberar recursos externos 🤔. Suceda un error o no esto sucede.

- Es importante definir bien el orden en el que ponemos cada excepción dentro del try, ya que cada excepción es leída de arriba a abajo, y la primera coincidencia que encuentra es la que ejecuta omitiendo las demás. Se pueden poner varios `except` para los distintos tipos de errores.

    ```python
    try:
      numero = 1 / 0
      print(numero)
    except ZeroDivisionError:
      print('No se puede divir entre 0')
    except ArithmeticError:
      print('Se encontro un error aritmetico')
    except:
      print('Se encontro un error')
    ```

### Poniendo a prueba el manejo de excepciones

- Solución al reto 😄

    ```python
    def divisors(num):
        divisors = []
        for x in range(1, num+1):
            if num%x == 0:
                divisors.append(x)
    
        return divisors
    
    def main():
    
        try:
            num = int(input('Ingresa un número entero positivo: '))
            if num < 0 or num%1 != 0:
                raise Exception('Debes ingresar un número entero positivo 🙄')
            print(divisors(num))
    
        except ValueError:
            print('Debes ingresar un número 👀')
    
        except Exception as ve:
            print(ve)
            exit()
    
        else:
            print('Ningun error en el camino 😁')
    
        finally:
            print('Terminó mi programa 💓')
    
    if __name__=='__main__':
        main()
    ```

### Assert statements

- Es una manera mas *extravagante* de manejar los errores. Esto puede marcar un diferencial al programar 😛. Esto es con los assert o afirmaciones. Estas son expresiones. La estructura general:

    ```python
    assert condicion, mensaje de error
    ```

- Por ejemplo, podríamos agregar en el código de palíndromos:

    ```python
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    ```

- Esto es una alternativa al try, except, raise y finally. No importa cual usar, pero es mucho más común encontrar try, except.

## Manejo de archivos

### ¿Cómo trabajar con archivos?

- Hay muchísimos tipos de archivos 📁. Dentro de la programación, es muy común trabajar con archivos. Los podemos clasificar en dos:
  - **Archivos de texto**: .json, .csv, .js, .txt, .py, etc. Solo hay letras! ✉️.
  - **Archivos binarios**: .mp3, .png, .ddl, .jpg, .avi, etc. En este caso almacenan cosas mucho más complejas ⛓️.
- Normalmente, al trabajar con Python 🐍 solo trabajaremos con archivos de texto, no con binarios. 👀.
- Hay tres modos de apertura de una archivo de texto:
  - r → Lectura.
  - w → Escritura (sobrescribir).
  - a → Escritura append (agregar al final).
- Para abrir un archivo, es con la siguiente línea y la palabra clave `with` que es un **manejador contextual** que maneja el archivo y, en caso de que se finalice el programa, no se rompa el archivo:

    ```python
    with open('archivo.txt', 'r') as f:
    ```

### Trabajando con archivos de texto en Python

```python
def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['Rodolfo', 'Ricardo', 'Bubu', 'Fanny']
    with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name+'\n')

def main():
    read()
    write()

if __name__ == '__main__':
    main()
```
