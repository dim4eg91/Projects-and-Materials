### Модели данных

В этом уроке:
1. С помощью сервиса [SqlDBM](https://sqldbm.com/Home/) были разработаны:
  * Концептуальная модель данных
  * Логическая модель данных
  * Физическая модель данных
2. Используя Forward Engineering, были получены DDL таблиц для схемы dwh и выполнены в DBeaver.
3. Сделано INSERT INTO SQL, чтобы заполнить Dimensions таблицы и Sales Fact таблицу. Сначала заполнены Dimensions таблицы, где в качестве id сгенерирована последовательность чисел, а зачем Sales Fact таблицу, в которую вставлил id из Dimensions таблиц. 
4. Перенос данных stg to dwh был успешно выполнен.







* Концептуальная модель данных

![img](https://github.com/dim4eg91/Projects-and-Materials/blob/main/data_engineering/module_02_SQL/2.1%20Модели%20Данных/Концептуальная%20модель.jpg)

* Логическая модель данных

![img](https://github.com/dim4eg91/Projects-and-Materials/blob/main/data_engineering/module_02_SQL/2.1%20Модели%20Данных/Логическая%20модель.jpg)

* Физическая модель данных

![img](https://github.com/dim4eg91/Projects-and-Materials/blob/main/data_engineering/module_02_SQL/2.1%20Модели%20Данных/Физическая%20модель.jpg)
