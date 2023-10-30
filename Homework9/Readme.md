# Архитектура ПО (семинары)
## Урок 9. Способы организации передачи данных между компонентами приложения, протоколы и API. REST, gRPC, очереди


![Снимок экрана 2023-10-30 в 16.57.25.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-30%20%D0%B2%2016.57.25.png)


## Кусок доработанного кода 
```yaml
  /cloud:
    get:
      summary: Метод получения списка облачных хранилищ
      tags:
        - Cloud
      operationId: getAllCloudStorage
      responses:
        "200":
          description: Успешный ответ со списком облачных хранилищ
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/CloudStorage"
        "default":
          description: Всё остальное
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/Error"
    post:
      summary: Метод добавления нового облачного хранилища в список
      tags:
        - Cloud
      operationId: createCloudStorage
      requestBody:
        required: true
        content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/CloudStorage"
      responses:
        "200":
          description: Успешный ответ добавления нового облачного хранилища
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/CloudStorage"
        "default":
          description: Всё остальное
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/Error"
  /cloud/{idStorage}:
    get:
      summary: Метод получения облачного хранилища по id
      tags:
        - Cloud
      operationId: getCloudStorageById
      parameters:
        - name: idStorage
          in: path
          required: true
          description: id Cloud Storage
          schema:
            type: string
      responses:
        "200":
          description: Успешный ответ получения облачного хранилища по id
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/CloudStorage"
        "default":
          description: Всё остальное
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/Error"
    delete:
      summary: Удаление облачного хранилища по id
      tags:
        - Cloud
      operationId: deleteCloudStorageById
      parameters:
        - name: idStorage
          in: path
          required: true
          description: id Cloud Storage
          schema:
            type: string
      responses:
        "200":
          description: Успешное удаление облачного хранилища по id
          content:
            adplication/json: {}
        "default":
          description: Всё остальное
          content:
            adplication/json:
              schema:
                $ref: "#/components/schemas/Error"

```


# Код целиком 
```yaml
openapi: 3.0.1
info:
  title: Получение информации о клиентах
  version: 0.0.3
servers:
  - url: http://localhost:8080/api/v1
paths:
    /clients:
      get:
        summary: Метод получения списка клиентов
        tags: 
          - Clients
        operationId: getAllClients
        responses:
          "200":
            description: Успешный ответ со спиcком клиентов
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Clients"
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"
      post:
        summary: Метод добавления нового клиента в список
        tags: 
          - Clients
        operationId: createClient
        requestBody:
          required: true
          content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Client" 
        responses:
          "200":
            description: Усшный ответ добавления нового клиента
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Client"
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"
    /clients/{idClient}:
      get:
        summary: Метод получения клиента по id
        tags:
          - Clients
        operationId: getClientId
        parameters:
          - name: idClient
            in: path
            required: true
            description: id Client
            schema:
              type: string
        responses:
          "200":
            description: Усшный ответ получения клиента по id
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Client"
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"     
      delete:
        summary: Удаление клиента по id
        tags:
          - Clients
        operationId: deleteClientById
        parameters:
          - name: idClient
            in: path
            required: true
            description: id Client
            schema:
              type: string
        responses:
          "200":
            description: Успешное удаление клиента по id
            content:
              adplication/json: {}
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error" 
    /cloud:
      get:
        summary: Метод получения списка облачных хранилищ
        tags:
          - Cloud
        operationId: getAllCloudStorage
        responses:
          "200":
            description: Успешный ответ со списком облачных хранилищ
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/CloudStorage"
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"
      post:
        summary: Метод добавления нового облачного хранилища в список
        tags:
          - Cloud
        operationId: createCloudStorage
        requestBody:
          required: true
          content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/CloudStorage"
        responses:
          "200":
            description: Успешный ответ добавления нового облачного хранилища
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/CloudStorage"
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"
    /cloud/{idStorage}:
      get:
        summary: Метод получения облачного хранилища по id
        tags:
          - Cloud
        operationId: getCloudStorageById
        parameters:
          - name: idStorage
            in: path
            required: true
            description: id Cloud Storage
            schema:
              type: string
        responses:
          "200":
            description: Успешный ответ получения облачного хранилища по id
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/CloudStorage"
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"
      delete:
        summary: Удаление облачного хранилища по id
        tags:
          - Cloud
        operationId: deleteCloudStorageById
        parameters:
          - name: idStorage
            in: path
            required: true
            description: id Cloud Storage
            schema:
              type: string
        responses:
          "200":
            description: Успешное удаление облачного хранилища по id
            content:
              adplication/json: {}
          "default":
            description: Всё остальное
            content:
              adplication/json:
                schema:
                  $ref: "#/components/schemas/Error"
    

components:
  schemas:
    Client:
      type: object
      required:
        - idClient
        - name
      properties:
        idClient:
          type: integer 
          example: 1
          description: Id клиента
        name:
          type: string
          example: Кирилл
          description: Имя клиента
    Clients:
      type: array
      items:
        $ref: "#/components/schemas/Client"
    Error:
      type: object
      required:
        - codeError
        - messageError
      properties:
        codeError:
          type: string
          example: 123f456
          description: Код ошибки
        messageError:
          type: string
          example: error
          description: Сообщение ошибки
    Cloud:
      type: object
      required:
        - OS
        - RAM
        - CPU
        - SSD
        - idClient
      properties:
        OS:
          type: string
          enum:
            - Windows
            - Linux
        RAM:
          type: integer
          example: 256
          description: Количество оперативной памяти
        CPU:
          type: integer
          example: 8
          description: Количество ядер процессора 
        SSD:
          type: integer
          example: 1024
          description: Количетсво ssd памяти
        idClient:
          type: integer
          example: 1
    CloudStorage:
      type: object
      required:
        - idStorage
        - name
        - location
        - capacity
      properties:
        idStorage:
          type: integer
          example: 1
          description: Идентификатор хранилища
        name:
          type: string
          example: Облачное хранилище 1
          description: Название хранилища
        location:
          type: string
          example: Россия
          description: Расположение хранилища
        capacity:
          type: integer
          example: 1024
          description: Емкость хранилища (в ГБ)
        clients:
          type: array
          items:
            type: integer
          description: Список клиентов, использующих это хранилище

```