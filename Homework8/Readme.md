# Архитектура ПО (семинары)

# На сколько я понял разрабатываем приложение для бронирования ресторанов! 

Урок 8. Типы архитектур прикладных приложений (мобильные): MVC, MVP, MVVM.

Разработать экранные формы интерфейса в https://www.figma.com/ или https://app.diagrams.net/.

Разработать полную ERD домена в https://www.dbdesigner.net/.

Доработать uml MVP.

## Разработать экранные формы интерфейса
### Разработал сразу в html (все файлы в on_screen_forms_of_the_interface)

### Авторизация 

![Снимок экрана 2023-10-26 в 13.18.43.png](on_screen_forms_of_the_interface%2Fscreenshots%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-26%20%D0%B2%2013.18.43.png)

### Регистрация

![Снимок экрана 2023-10-26 в 13.20.32.png](on_screen_forms_of_the_interface%2Fscreenshots%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-26%20%D0%B2%2013.20.32.png)

### Домашняя страница

![Снимок экрана 2023-10-26 в 13.22.00.png](on_screen_forms_of_the_interface%2Fscreenshots%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-26%20%D0%B2%2013.22.00.png)

### Бронирование столика  
![Снимок экрана 2023-10-26 в 13.23.07.png](on_screen_forms_of_the_interface%2Fscreenshots%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-26%20%D0%B2%2013.23.07.png)

### Подтверждение бронирования 
![Снимок экрана 2023-10-26 в 13.24.08.png](on_screen_forms_of_the_interface%2Fscreenshots%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-26%20%D0%B2%2013.24.08.png)


# Разработать полную ERD домена в https://www.dbdesigner.net/.

```mysql-sql
Customer {
    id integer pk increments
    name string
    address integer
    hash integer
    }
Table {
    id integer pk increments
    places integer
    idHalf integer *> Hall.id
    idImage integer >* Image.id
    comment string
    price integer
    }
Hall {
    id integer pk increments
    typeName string pk increments
    }
Image {
    id integer pk increments
    byte integer
    }
Order{
    id integer pk
    endTime time
    startDateTime timestamp
    idTable integer > Table.id
    idcustomer integer > Customer.id
    idcoef integer > Coefficient.id
    }
Coefficient {
    id integer pk increments
    coefficient integer 
    }
```
![Снимок экрана 2023-10-26 в 14.18.53.png](on_screen_forms_of_the_interface%2Fscreenshots%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-26%20%D0%B2%2014.18.53.png)

# Доработать uml MVP.
## MVC 
![mvc.png](on_screen_forms_of_the_interface%2Fscreenshots%2Fmvc.png)

## MVP
![mvp.png](on_screen_forms_of_the_interface%2Fscreenshots%2Fmvp.png)