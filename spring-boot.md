Crear una API REST en Java usando Spring Boot con IntelliJ IDEA y Swagger para la documentación, para después probarla con Postman. Combinamos Spring Boot para crear la API, Swagger para documentarla y Postman para probarla.

# 1. Configurar un Proyecto de Spring Boot en IntelliJ IDEA

## a) Crear un nuevo proyecto de Spring Boot en IntelliJ IDEA:

•	Abrí IntelliJ IDEA y seleccioná New Project.

•	Elegí Spring Initializr como generador del proyecto.

•	Configurá los datos del proyecto:

o	Grupo: com.sii

o	Artefacto: api-rest

o	Nombre del proyecto: api-rest-smn

•	En "Dependencies" agrega las siguientes dependencias:

o	Spring Web (para crear controladores REST).

o	Spring Data JPA (si vas a usar base de datos).

o	MySQL Driver (para conectarte a una base de datos MySQL).

o	Spring Boot DevTools (para recargar el servidor automáticamente durante el desarrollo).

o	SpringFox Swagger UI (para agregar la documentación de Swagger).

##  b) Configurar application.properties:
Si estás utilizando MySQL, configurá tu conexión en el archivo src/main/resources/application.properties:
````
properties

spring.datasource.url=jdbc:mysql://localhost:3306/tu_basedatos
spring.datasource.username=tu_usuario
spring.datasource.password=tu_contraseña
spring.jpa.hibernate.ddl-auto=update
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
````
# 2. Crear las Entidades y Controladores

## a) Crear una Entidad:

Por ejemplo, cuando trabajamos con empleados, creamos una clase Employee en el paquete model.
````
java

package com.example.api.model;

import javax.persistence.*;

@Entity
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String position;
    private String email;

    // Getters y Setters
}
````
## b) Crear un Repositorio:
Creamos un EmployeeRepository en el paquete repository para interactuar con la base de datos.
````
java

package com.example.api.repository;

import com.example.api.model.Employee;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository<Employee, Long> {
}
````

## c) Crear un Controlador REST:

En el paquete controller, creá un controlador para manejar las solicitudes HTTP, como POST para agregar un empleado.
````
java

package com.example.api.controller;

import com.example.api.model.Employee;
import com.example.api.repository.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/employees")
public class EmployeeController {

    @Autowired
    private EmployeeRepository employeeRepository;

    @PostMapping
    public Employee createEmployee(@RequestBody Employee employee) {
        return employeeRepository.save(employee);
    }
}
````
# 3. Configurar Swagger para Documentar la API

## a) Agregar Configuración de Swagger:
Crea una clase de configuración en el paquete config para habilitar Swagger.
````
java

package com.example.api.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

@Configuration
public class SwaggerConfig {

    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.api.controller"))
                .paths(PathSelectors.any())
                .build();
    }
}
````
## b) Acceder a Swagger UI:
Cuando corras tu aplicación, Swagger estará disponible en la URL:
````
bash

http://localhost:8080/swagger-ui.html
````
Desde ahí, podés ver la documentación y probar los diferentes endpoints.

# 4. Probar la API con Postman
## a) Crear una solicitud POST en Postman:
•	Abrí Postman y creá una nueva solicitud POST.

•	En la URL, colocá el endpoint de tu API:

````
bash

http://localhost:8080/api/employees
````
•	En la pestaña Body, seleccioná raw y luego el formato JSON.

•	Escribí el cuerpo de la solicitud con los datos que querés enviar, por ejemplo:
````
json

{
  "name": "Juan Perez",
  "position": "Meteorólogo",
  "email": "juan.perez@smn.gob.ar"
}
````
•	Clickeá en Send para enviar la solicitud y, si todo está bien, vas a ver la respuesta con el empleado que acabás de agregar.


Flujo Completo:
1.	IntelliJ IDEA: Desarrollo del backend con Spring Boot.

2.	Swagger: Documentación y prueba de la API desde el navegador.

3.	Postman: Prueba más avanzada de la API, especialmente con diferentes tipos de datos y solicitudes.

Esto es básicamente el ciclo completo de trabajo para desarrollar, documentar y probar una API REST en un entorno profesional de Java.
