# Архитектура ПО (семинары)
Урок 7. Типа архитектур WEB-приложений: MPA, SPA.

## Убедительная просьба на странице с д/з формулируйте более развернуто задание, а то приходится гадать что нужно сделать. Какая цель домашнего задания какие инструменты использовать и тд.. очень прошу четко формулировать ТЗ


Доработать экранные формы интерфейса в https://www.figma.com/ или https://app.diagrams.net/. __Что доработать ? какие экранные формы? каие интерфейсы? что сделать с этими ресурсами? https://www.figma.com/ или https://app.diagrams.net/ в них что то нуно доработать? или доработать что что с использованием этих инструментов? и что нужно доработать?__

Разработать полную ERD домена в https://www.dbdesigner.net/. __Опять какого домена? какого проекта?__

Разработать диаграмму компонент в UML включая слои пользовательского интерфейса и бизнес-логики. __И тут же для чего разработать диаграмму компонент в UML? какой проект?__

На сколько я понял мы выполняем задачу "Необходимо спроектировать сервис отчётов для компании оптовой торговли."
Если прописать задачу в условие домашней работы, то эо бы сняло большую часть вопросов. 

Поскольку нет желания и знаний делать формы интерфейса в фигме, я мне проще сделать сразу html страницу home.html (Просто запустите ее где угодно) 
![Снимок экрана 2023-10-24 в 19.22.17.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-24%20%D0%B2%2019.22.17.png)

# ERD диаграмма 

![Снимок экрана 2023-10-24 в 19.54.52.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-24%20%D0%B2%2019.54.52.png)

код mysql
```mysql-sql
CREATE TABLE CUSTOMER (
  customer_id INT,
  customer_name VARCHAR(255)
);

CREATE TABLE `ORDER` (
  order_id INT,
  order_date DATE,
  customer_id INT
);

CREATE TABLE ADDRESS (
  address_id INT,
  address VARCHAR(255),
  customer_id INT
);

CREATE TABLE ORDER_ITEM (
  item_id INT,
  order_id INT,
  product_id INT
);

CREATE TABLE PRODUCT_CATEGORY (
  category_id INT,
  category_name VARCHAR(255)
);

CREATE TABLE PRODUCT (
  product_id INT,
  product_name VARCHAR(255),
  category_id INT
);

ALTER TABLE CUSTOMER ADD CONSTRAINT PK_CUSTOMER PRIMARY KEY (customer_id);
ALTER TABLE `ORDER` ADD CONSTRAINT PK_ORDER PRIMARY KEY (order_id);
ALTER TABLE ADDRESS ADD CONSTRAINT PK_ADDRESS PRIMARY KEY (address_id);
ALTER TABLE ORDER_ITEM ADD CONSTRAINT PK_ORDER_ITEM PRIMARY KEY (item_id);
ALTER TABLE PRODUCT_CATEGORY ADD CONSTRAINT PK_PRODUCT_CATEGORY PRIMARY KEY (category_id);
ALTER TABLE PRODUCT ADD CONSTRAINT PK_PRODUCT PRIMARY KEY (product_id);

ALTER TABLE `ORDER` ADD CONSTRAINT FK_ORDER_CUSTOMER FOREIGN KEY (customer_id) REFERENCES CUSTOMER (customer_id);
ALTER TABLE ADDRESS ADD CONSTRAINT FK_ADDRESS_CUSTOMER FOREIGN KEY (customer_id) REFERENCES CUSTOMER (customer_id);
ALTER TABLE ORDER_ITEM ADD CONSTRAINT FK_ORDER_ITEM_ORDER FOREIGN KEY (order_id) REFERENCES `ORDER` (order_id);
ALTER TABLE ORDER_ITEM ADD CONSTRAINT FK_ORDER_ITEM_PRODUCT FOREIGN KEY (product_id) REFERENCES PRODUCT (product_id);
ALTER TABLE PRODUCT ADD CONSTRAINT FK_PRODUCT_CATEGORY FOREIGN KEY (category_id) REFERENCES PRODUCT_CATEGORY (category_id);

```

