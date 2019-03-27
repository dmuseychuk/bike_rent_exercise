Alquiler de bicicletas
----

Desarrollo hecho en python 3.6. No se requieren librerias externas. 

El codigo esta documentado y cumple con los requisitos de PEP8.

* Algunos ejemplos de uso con resultados imprimidos: *python3 run.py*

* Para correr los tests: *python3 tests.py*

* Todas las clases se encuentran en *lib.py*

* Se adjunta reporte de coverage en HTML: ver directorio coverage_report. El reporte fue generado con plugin Coverage.py.

---

###Rent 
Recibe 2 parametros posicionales en el constructor. 
El primero es tipo de renta. Puede ser cualquier clase de tipo de renta definido en *lib.py* u otro extendido de la clase *BaseRentType*. 
El segundo parametro es la cantidad de rentas. La cantidad debe ser de tipo entero. 
En la llamada del metodo *get_total_price()* se calcula el precio total de la renta. El metodo retornara el precio total en *float*. 
Puede lanzar excepcion *TypeError*, si tipo de renta o cantidad de rentas tienen tipos de datos invalidos.

---
###FamilyRent
Debe recibir entre 3 a 5 objetos de tipo *Rent* en el constructor. 
El metodo *get_total_price()* calculara los precios para todas las rentas y le aplicara un descuento de 30% al precio total. 
Retorna el precio en *float*. Todos los parametros tienen que ser de tipo rent, sino el metodo lanzara excepcion de tipo *TypeError*. 
La cantidad de rentas debe ser entre 3 y 5 inclusive, sino se lanzara excepcion de tipo *ValueError*.  

---

Tipos predefinidos de rentas son *RentByHour*, *RentByDay*, *RentByWeek*. Si quieremos definir otro tipo de renta, deberiamos extender la clase *BaseRentType*.

---


