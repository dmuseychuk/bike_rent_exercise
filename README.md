Alquiler de bicicletas
----

Desarrollo hecho en python 3.6. No se requieren librerias externas. 

El codigo esta documentado y cumple con los requisitos de PEP8.

* Algunos ejemplos de uso con resultados imprimidos: *python3 run.py*

* Para correr los tests: *python3 tests.py*

* Todas las clases se encuentran en *lib.py*

* Se adjunta .coverage con reporte (para generarlo se uso el plugin Coverage.py)

---

La clase *Rent* es la que maneja las rentas. Recibe 2 paramentros posicionales en el constructor. El primero es tipo de renta. Puede ser cualquier clase de tipo de renta definido en *lib.py* u otro extendido de la clase *BaseRentType* (si el tipo de renta no es extendido de *BaseRentType*, se lanzara una excepcion de tipo *TypeError* al momento de llamar al metodo *get_total_price()*). El segundo parametro es la cantidad de rentas. La cantidad debe ser de tipo entero (se lanzara una excepcion de tipo *TypeError* en la llamada del metodo *get_total_price()* si el valor no es un entero). En la llamada del metodo *get_total_price()* se calculan tambien todos los descuentos seteados en atributo *_discounts*. Este atributo es un listado de descuentos a aplicar al precio total. En este caso hay un solo tipo de descuento *FamilyDiscount*. Es posible agregarle otros tipos de descuentos. Para esto hay que extender de la clase *BaseDiscount* e implementar el metodo *apply()* con sus condiciones para el descuento.   

---

Tipos predefinidos de rentas son *RentByHour*, *RentByDay*, *RentByWeek*. Si quieremos definir otro tipo de renta, deberiamos extender la clase *BaseRentType*.

---

Tipos predefinidos de descuentos son *FamilyDiscount*(30% sobre el total si la cantidad de rentas es entre 3 y 5). Si quieremos definir otro tipo de descuento, deberiamos extender la clase *BaseDiscount*. El constructor de la clase extendida de *BaseDiscount* deberia recibir la instacia de la clase *Rent*

---

