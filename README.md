# Crear una API

## Introduccion

El objetivo es crear una API REST , en este caso usamos Flask , conectada a una base de datos. Con el repositorio [Ollivanders/GildedRose](https://github.com/ErikPC/DDD_Gilded_Rose) teniamos que añadir los items magicos a la base de datos y realizar el CRUD sobre dichos item.

## Objetivo

- Con esta practica logramos entender el patrón MVC
- Como funciona una API REST.
- Controlar los requisitos.
- Manejar items en la BBDD a traves de una API
- Entender como crear un pryecto con Flask sencillo
- Saber elegir un ORM

### Conclusion

Ha estado entretenido crear la API REST , empezar con el hello world y luego ir cambiandolo ha ido bastante rodado. A la hora de elegir la BBDD y como convertir los objetos de a JSON ha hecho que dependa de la libreria flask_restful la cual me ha facilitado bastante el trabajo.

Con la conexion a la BBDD con mongoengine deberia cambiar en un futuro ya que han salido warnings de deprecated en los tests. Controlar las dependencias y diferenciarlas de las de desarrollo ha sido más simple de lo esperado , pero si ya hubiera estado apuntando las que instalaba antes seria aun más sencillo.

Los test ha sido más complicado de lo esperado usando el archivo conftest de pytest. Al principio creaba la base de datos y lo testeaba todo de forma visual en el navegador y reseteaba la BBDD a mano. Una vez se creaba la BBDD en los test por session entera , a lod días por recomendacion de un compañero cambié que que en vez de crearse por session se creara por modulo , de esta manera teniamos controlada la BBDD. Tambien tener en cuenta lo que te devuelve exactamente es importante para que los test funcionen y no estes todo el rato fixeando test.

Los test se deberian haber creado antes 🤘😔

La API REST funciona como un camarero

<img src="./docs/camarero.png" width=35%>
