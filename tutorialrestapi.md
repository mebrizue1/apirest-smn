# 1. Introducción a REST

## ¿Qué es REST?

REST significa Transferencia de Estado de Representación (Representational State Transfer).
Entendamos el significado de cada palabra del acrónimo REST.

•	 Estado (State) = datos

•	 REpresentacional = formatos (como XML, JSON, YAML, HTML, etc.)

•	 Transferir = llevar datos entre el consumidor y el proveedor utilizando el protocolo HTTP

## Transferencia de estado representacional

•	REST fue acuñado originalmente por Roy Fielding, quien también fue el inventor del protocolo HTTP.

•	Una API REST es una interfaz de programación de aplicaciones intermediaria que permite que dos aplicaciones se comuniquen entre sí a través de HTTP, de forma muy similar a cómo los servidores se comunican con los navegadores.

•	El estilo arquitectónico REST se ha vuelto rápidamente muy popular en todo el mundo para diseñar aplicaciones que puedan comunicarse.

•	La necesidad de API REST aumentó mucho con el aumento drástico de dispositivos móviles. Se volvió lógico crear API REST y dejar que los clientes web y móviles consumieran la API en lugar de desarrollar aplicaciones separadas.

# 2. Arquitectura REST

El siguiente diagrama muestra la arquitectura REST típica:

![Diagrama REST](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrF2AyWS4JnOXV3R2vV9UWOdun7kcoxaF6PyEo6wKQqnBdJnDI9O6NdcdcvbvJgqNX-Xr4CdL_eE5kswqLeaFjmsNJqJT0ZfJmVNPFc6tFPmFYTuoPneUWny2AO0EHYH9ved0Et0ql5GA/s1280/Slide4.PNG "Diagrama REST")

Comprendamos algunos términos de servicios web observando la arquitectura anterior:

(Request y response) Solicitud y respuesta: la solicitud es la entrada a un servicio web y la respuesta es la salida de un servicio web.

(Message Exchange Format) Formato de intercambio de mensajes: es el formato de la solicitud y la respuesta. Existen dos formatos de intercambio de mensajes más conocidos: XML y JSON.

(Service Provider o Server) Proveedor de servicios o servidor:  El proveedor de servicios es aquel que aloja el servicio web.

Consumidor o cliente de servicio: Un consumidor de servicio es aquel que utiliza un servicio web.

Es responsabilidad del consumidor, es decir, de la aplicación cliente, preparar y enviar el mensaje de solicitud HTTP.

Es responsabilidad del componente empresarial (desarrollado por un proveedor de servicios) preparar y enviar el mensaje de respuesta HTTP.

# 3. Restricciones arquitectónicas REST

Una API que tiene las siguientes restricciones se conoce como API RESTful:

(Client-server architecture) Arquitectura cliente-servidor: el cliente es el front-end y el servidor es el back-end del servicio. Es importante destacar que ambas entidades son independientes entre sí.

(Stateless) Sin estado: no se deben almacenar datos en el servidor durante el procesamiento de la transferencia de la solicitud. El estado de la sesión se debe guardar en el extremo del cliente.

(Cacheable) Almacenamiento en caché: el cliente debe tener la capacidad de almacenar respuestas en caché. Esto mejora enormemente el rendimiento de la API.

(Uniform Interface) Interfaz Uniforme: Esta restricción indica una interfaz genérica para gestionar todas las interacciones entre el cliente y el servidor de forma unificada, lo que simplifica y desacopla la arquitectura. 

(Layered System) Sistema en capas: el servidor puede tener varias capas para su implementación. Esta arquitectura en capas ayuda a mejorar la escalabilidad al permitir el equilibrio de carga.

(Code on Demand) Código a pedido: esta restricción es opcional. Esta restricción indica que la funcionalidad de las aplicaciones cliente se puede ampliar en tiempo de ejecución al permitir la descarga de código desde el servidor y ejecutarlo.

# 4. Conceptos clave de REST
Recurso
El concepto fundamental de un sistema basado en REST es el recurso. Un recurso es cualquier cosa que desee exponer al mundo exterior a través de tu aplicación.

Ejemplo 1: Recursos para el sistema de gestión de empleados:

- Empleado
- Departamento
- Proyectos
- Tarea
- Dirección

Ejemplo 2: Recursos para el sistema de gestión de estudiantes:

- Alumno
- Maestro
- Escuela
- Clase
- Sujeto

## URI - Identificador uniforme de recursos 

El recurso se puede identificar mediante un identificador uniforme de recursos (URI). En el caso de los sistemas basados en la Web, el protocolo HTTP es el más utilizado para comunicarse con sistemas externos. Se puede identificar un recurso único mediante un URI.

Considerá que estamos desarrollando una aplicación de blog simple y se puede definir una URI para un recurso de publicación de blog:

GET— http://localhost:8080/api/posts/: Devuelve una lista de todas las publicaciones

GET— http://localhost:8080/api/posts/2 : Devuelve una publicación cuyo ID es 2

POST— http://localhost:8080/api/posts/ : Crea un nuevo recurso de publicación

PUT— http://localhost:8080/api/posts/2: Actualiza un recurso POST cuyo ID es 2

DELETE— http://localhost:8080/api/posts/2: Elimina un recurso POST cuyo ID es 2

## Subrecurso (sub-resource)

En REST, las relaciones suelen estar modeladas por un subrecurso. Usá el siguiente patrón para los subrecursos.

GET  /{resource}/{resource-id}/{sub-resource}

GET  /{resource}/{resource-id}/{sub-resource}/{sub-resource-id}

POST /{resource}/{resource-id}/{sub-resource}

Ejemplo: 

GET  /{post}/{post-id}/{comments}

GET  /{post}/{post-id}/{comments}/{comment-id}

POST /{post}/{post-id}/{comments}

Utilizá subrecursos. El objeto secundario (child) no puede existir sin su padre.

## Métodos HTTP

Verbos HTTP comunes:

• 	GET: para obtener una colección o un solo recurso

• 	PUT: para crear un nuevo recurso

• 	PUT: para actualizar un recurso existente

• 	DELETE: para eliminar una colección o un solo recurso

Código de estado HTTP

Algunos de los códigos de estado utilizados con frecuencia en esta clase son los siguientes:

•	200 OK: Este código indica que la solicitud es exitosa y el contenido de la respuesta se devuelve al cliente según corresponda.

•	201 Creado: Este código indica que la solicitud es exitosa y se crea un nuevo recurso.

•	400 Solicitud incorrecta: este código indica que el servidor no pudo procesar la solicitud debido a una sintaxis incorrecta. El cliente puede volver a intentarlo después de corregir la solicitud.

•	401 No autorizado: este código indica que se requiere autenticación para el recurso. El cliente puede volver a intentarlo con la autenticación adecuada.

•	403 Prohibido: este código indica que el servidor se niega a responder a la solicitud, incluso si esta es válida. El motivo se indicará en el contenido del cuerpo si la solicitud no es un método HEAD.

•	404 No encontrado: este código indica que el recurso solicitado no se encuentra en la ubicación especificada en la solicitud.

•	500 Error interno del servidor: este código indica un mensaje de error genérico y dice que ocurrió un error inesperado en el servidor y que no se puede cumplir la solicitud.

# 5. Cree una API REST con Java
## 1. Conceptos básicos de REST
✅   [Descripción general de REST](https://www.javaguides.net/2018/06/overview-of-rest.html)

✅   [¿Qué es la carga útil (Payload) en REST API? ](https://www.javaguides.net/2021/05/what-is-payload-in-rest-api.html)

✅   [API REST: métodos HTTP](https://www.javaguides.net/2021/01/rest-api-http-methods.html)

✅   [API REST: códigos de estado HTTP](https://www.javaguides.net/2021/01/rest-api-http-status-codes.html) 

✅   [Ventajas de REST](https://www.javaguides.net/2018/07/advantages-of-rest.html)

✅   [API REST: restricciones arquitectónicas de REST  ](https://www.javaguides.net/2018/06/rest-architectural-constraints.html)

✅   [API REST: propiedades arquitectónicas de REST  ](https://www.javaguides.net/2018/06/rest-architectural-properties.html)

✅   [API REST: elementos arquitectónicos de REST  ](https://www.javaguides.net/2018/06/rest-architectural-elements.html)

✅   [Diferencia entre servicios web SOAP y REST  ](https://www.javaguides.net/2018/07/rest-vs-soap.html)

## 2. Guía de diseño de API REST

✅   [Cómo identificar recursos REST  ](https://www.javaguides.net/2018/06/how-to-identify-rest-resources.html)

✅   [Cómo diseñar URL para recursos REST  ](https://www.javaguides.net/2018/06/how-to-design-url-to-rest-resource.html)

✅   [Cómo asignar métodos HTTP a recursos REST  ](https://www.javaguides.net/2018/06/how-to-assign-http-methods-to-rest-resources.html)

✅   [Cómo modelar el formato de representación JSON  ](https://www.javaguides.net/2018/06/how-to-model-json-representation-format.html)

✅   [Qué código de estado HTTP devolver  ](https://www.javaguides.net/2018/06/what-http-status-code-to-return.html)

## 3. Prácticas recomendadas para el diseño de API Rest
✅   [Prácticas recomendadas para el diseño de una API Restful  ](https://www.javaguides.net/2018/06/restful-api-design-best-practices.html)

## 4. Cree una API REST con Jersey Rest Framework
✅   [Ejemplo de Jersey Rest Hola mundo](https://www.javaguides.net/2018/06/jersey-rest-hello-world-example.html)

✅   [Ejemplo de servicios web CRUD Restful JAX-RS de Jersey  ](https://www.javaguides.net/2018/06/jersey-jax-rs-restful-crud-web-services-example.html)

✅   [Guía para desarrolladores de Jersey Rest  ](https://www.javaguides.net/p/jersey-rest.html)

## 5. Cree una API REST utilizando JAX-RS RESTEasy Framework
✅   [Tutorial de ejemplo de "Hola mundo" de RESTEasy](https://www.javaguides.net/2020/01/resteasy-hello-world-example-tutorial.html)

✅   [Tutorial de RESTEasy JAX-RS Get, POST, PUT y DELETE](https://www.javaguides.net/2020/01/resteasy-jax-rs-get-post-put-and-delete-tutorial.html)

✅   [Cliente RESTEasy para API RESTFul GET, POST, PUT y DELETE](https://www.javaguides.net/2020/01/resteasy-client-for-get-post-put-and-delete-rest-apis.html)

## 6. Cree una API REST con Spring Boot
✅  [Proyecto de API CRUD REST de Spring Boot con IntelliJ IDEA | Postman | MySQL](https://www.javaguides.net/2021/10/spring-boot-crud-rest-api-project-using-IntelliJ-IDEA.html)

✅  [Tutorial de API CRUD Restful de Spring Boot, MySQL, JPA e Hibernate](https://www.javaguides.net/2020/04/spring-boot-mysql-jpa-hibernate-restful-crud-api-tutorial.html)

✅  [Ejemplo de API Rest de carga y descarga de archivos de Spring Boot](https://www.javaguides.net/2020/04/spring-boot-file-upload-download-rest-api-example.html)

✅  [Tutorial de API Restful CRUD de Spring Boot, H2, JPA e Hibernate](https://www.javaguides.net/2020/04/spring-boot-h2-jpa-hibernate-restful-crud-api-tutorial.html)

✅  [API REST de inicio de sesión de Spring Boot con Spring Security y MySQL](https://www.javaguides.net/2020/04/spring-boot-h2-jpa-hibernate-restful-crud-api-tutorial.html)

✅  [API REST de inicio de sesión y registro con Spring Boot, Spring Security, Hibernate y base de datos MySQL](https://www.javaguides.net/2020/04/spring-boot-file-upload-download-rest-api-example.html)

✅  [Documentación de la API REST de Spring Boot con Swagger](https://www.javaguides.net/2021/06/spring-boot-rest-api-documentation-with-swagger.html)

✅  [Búsqueda de API REST con Spring Boot, Spring Data JPA y base de datos MySQL](https://www.javaguides.net/2022/04/search-rest-api-using-spring-boot.html)

✅  [Pruebas unitarias de Spring Boot de la API CRUD REST con JUnit y Mockito](https://www.javaguides.net/2022/03/spring-boot-unit-testing-crud-rest-api-with-junit-and-mockito.html)

✅  [Tutorial de la API CRUD REST de MySQL para pruebas de integración de Spring Boot](https://www.javaguides.net/2022/03/spring-boot-integration-testing-mysql-crud-rest-api-tutorial.html)

Fuente:  https://www.javaguides.net/p/rest-api-tutorial.html (Autor: Ramesh Fadatare)
