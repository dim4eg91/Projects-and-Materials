# Модели данных

За основной источник данных взят файл Sample - Superstore.xls
Создана схема stg для источника данных, а также 3 таблицы.

С помощью сервиса [SqlDBM](https://sqldbm.com/Home/) были разработаны:

* Концептуальная модель данных

![img](https://github.com/dim4eg91/Projects-and-Materials/blob/main/data_engineering/module_02_SQL/2.4%20Установка%20DBeaver%20и%20создание%20БД/Концептуальная%20модель.jpg)

* Логическая модель данных

![img](https://github.com/dim4eg91/Projects-and-Materials/blob/main/data_engineering/module_02_SQL/2.4%20Установка%20DBeaver%20и%20создание%20БД/Логическая%20модель.jpg)

* Физическая модель данных

![img](https://github.com/dim4eg91/Projects-and-Materials/blob/main/data_engineering/module_02_SQL/2.4%20Установка%20DBeaver%20и%20создание%20БД/Физическая%20модель.jpg)



Используя Forward Engineering, были получены DDL таблиц для схемы dwh.
Перенос данных stg to dwh был успешно выполнен.
