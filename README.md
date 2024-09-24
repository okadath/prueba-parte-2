## Ejecucion
ejecutar con docker
```sh
docker compose build
docker compose up
```

y abrir la url 

[http://0.0.0.0:8000/](http://0.0.0.0:8000/)

en ese link se encuentra la pagina de visualizacion de los endpoints, desde ahi se pueden probar el endpoint que muestra todos los numeros y el endpoint que extrae un numero del conjunto de numeros 

![swagger](https://raw.githubusercontent.com/okadath/prueba-parte-2/refs/heads/master/swagger.png)


## parte 2
• La aplicación debe de implementarse en el lenguaje de acuerdo con el perfil:
Python3.8

• Se debe de implementar una clase que represente al conjunto de los primero 100 números
```py
class NumberSet:
    def __init__(self):
        self.numbers = set(range(0, 101))
        self.extracted_number = None
```

• La clase implementada debe de tener el método Extract para extraer un cierto número deseado
```py
    def extract(self, number):
        if not (0 <= number <= 100):
            raise ValueError("El número debe estar entre 1 y 100.")
        if number in self.numbers:
            self.numbers.remove(number)
            self.extracted_number = number
        else:
            raise ValueError(f"El número {number} ya fue extraído o no está en el conjunto.")

```

• La clase implementada debe de poder calcular que numero se extrajo y presentarlo
```py
    def find_missing_number(self):
        if self.extracted_number is None:
            return "No se ha extraído ningún número aún."
        return self.extracted_number

```

• Debe de incluir validación del input de datos (numero, número menor de 100)
```py
@api_view(['POST'])
def extract_number(request):
    try:
        number = int(request.data.get('number')) 

```

• La aplicación debe de poder ejecutarse con un argumento introducido por el usuario que haga uso de nuestra clase y muestre que pudo calcular que se extrajo ese número

```py
    number_set.extract(number)

    return Response({
        'message': f"El número {number} ha sido extraído exitosamente.",
        'missing_number': number_set.find_missing_number()
    }, status=200)

```
