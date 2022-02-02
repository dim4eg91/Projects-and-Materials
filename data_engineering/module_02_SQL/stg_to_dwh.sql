-- create sales_fact table
-- match number of rows between staging and dw (business layer)

-- Создание схемы dwh

create schema dwh;

-----------------------------------------------------------------------------

-- Создание таблицы  SHIPPING_DIM
drop table if exists dwh.shipping_dim cascade;
CREATE TABLE dwh.shipping_dim
(
 ship_id   serial NOT NULL,
 ship_mode varchar(20) NOT NULL,
 CONSTRAINT PK_shipping_dim PRIMARY KEY (ship_id)
);

-- Удаление строк
truncate table dwh.shipping_dim;

-- Генерация ship_id и заполнение таблицы из таблицы orders
insert into dwh.shipping_dim 
select 100 + row_number() over(), ship_mode from (select distinct ship_mode from stg.orders) a;

-- Проверка
select * from dwh.shipping_dim sd; 

-----------------------------------------------------------------------------

-- Создание таблицы PRODUCT_DIM
drop table if exists dwh.product_dim cascade;
CREATE TABLE dwh.product_dim
(
 prod_id   serial NOT NULL, --we created surrogated key
 product_id   varchar(50) NOT NULL,
 category     varchar(50) NOT NULL,
 subcategory  varchar(50) NOT NULL,
 segment      varchar(50) NOT NULL,
 product_name varchar(150) NOT NULL,
 CONSTRAINT PK_product_dim  PRIMARY KEY ( prod_id )
);

-- Удаление строк
truncate table dwh.product_dim;

-- Генерация prod_id и заполнение таблицы из таблицы orders
insert into dwh.product_dim 
select 100 + row_number() over () as prod_id ,product_id, category, subcategory, segment, product_name from (select distinct product_id, category, subcategory, segment, product_name from stg.orders) a;

-- Проверка
select * from dwh.product_dim cd; 

-----------------------------------------------------------------------------

-- Создание таблицы CUSTOMER
drop table if exists dwh.customer_dim ;
CREATE TABLE dwh.customer_dim
(
 cust_id serial NOT NULL,
 customer_id   varchar(8) NOT NULL, --id can't be NULL
 customer_name varchar(22) NOT NULL,
 CONSTRAINT PK_customer_dim PRIMARY KEY ( cust_id )
);

-- Удаление строк
truncate table dwh.customer_dim;

-- Заполнение таблицы из таблицы orders
insert into dwh.customer_dim 
select 100 + row_number() over(), customer_id, customer_name from (select distinct customer_id, customer_name from stg.orders) a;

-- Проверка
select * from dwh.customer_dim cd;  

-----------------------------------------------------------------------------

-- Создание таблицы GEOGRAPHY
drop table if exists dwh.geography_dim;
CREATE TABLE dwh.geography_dim
(
 geo_id      serial NOT NULL,
 country     varchar(20) NOT NULL,
 city        varchar(20) NOT NULL,
 "state"     varchar(20) NOT NULL,
 postal_code varchar(30) NULL,
 CONSTRAINT PK_geo_dim PRIMARY KEY ( geo_id )
);

-- Удаление строк
truncate table dwh.geography_dim;

-- Заполнение таблицы из таблицы orders
insert into dwh.geography_dim
select 100 + row_number() over(), country, city, state, postal_code from (select distinct country, city, state, postal_code from stg.orders ) a;

-- Проверка
select * from dwh.geography_dim;

-----------------------------------------------------------------------------

-- Проверка качества данных
select distinct country, city, state, postal_code from dwh.geography_dim
where country is null or city is null or postal_code is null;

-- City Burlington, Vermont doesn't have postal code
update dwh.geography_dim
set postal_code = '05401'
where city = 'Burlington'  and postal_code is null;

-- Исправление таблицы stg.orders - запись postal_code, где он был NULL
update stg.orders
set postal_code = '05401'
where city = 'Burlington'  and postal_code is null;

-----------------------------------------------------------------------------


--CALENDAR use function instead 
-- examplehttps://tapoueh.org/blog/2017/06/postgresql-and-the-calendar/

--creating a table
drop table if exists dwh.calendar_dim ;
CREATE TABLE dwh.calendar_dim
(
dateid serial  NOT NULL,
year        int NOT NULL,
quarter     int NOT NULL,
month       int NOT NULL,
week        int NOT NULL,
date        date NOT NULL,
week_day    varchar(20) NOT NULL,
leap  varchar(20) NOT NULL,
CONSTRAINT PK_calendar_dim PRIMARY KEY ( dateid )
);

-- Удаление строк
truncate table dwh.calendar_dim;

-- Заполнение таблицы
insert into dwh.calendar_dim 
select 
to_char(date,'yyyymmdd')::int as date_id,  
       extract('year' from date)::int as year,
       extract('quarter' from date)::int as quarter,
       extract('month' from date)::int as month,
       extract('week' from date)::int as week,
       date::date,
       to_char(date, 'dy') as week_day,
       extract('day' from
               (date + interval '2 month - 1 day')
              ) = 29
       as leap
  from generate_series(date '2000-01-01',
                       date '2030-01-01',
                       interval '1 day')
       as t(date);
      

-- Проверка
select * from dw.calendar_dim; 

-----------------------------------------------------------------------------

--METRICS

-- Создание таблицы SALES_FACT 
drop table if exists dwh.sales_fact ;
CREATE TABLE dwh.sales_fact
(
 sales_id      serial NOT NULL,
 cust_id integer NOT NULL,
 order_date_id integer NOT NULL,
 ship_date_id integer NOT NULL,
 prod_id  integer NOT NULL,
 ship_id     integer NOT NULL,
 geo_id      integer NOT NULL,
 order_id    varchar(25) NOT NULL,
 sales       numeric(9,4) NOT NULL,
 profit      numeric(21,16) NOT NULL,
 quantity    int4 NOT NULL,
 discount    numeric(4,2) NOT NULL,
 CONSTRAINT PK_sales_fact PRIMARY KEY ( sales_id ));


insert into dwh.sales_fact 
select
	 100 + row_number() over() as sales_id
	 ,cust_id
	 ,to_char(order_date,'yyyymmdd')::int as  order_date_id
	 ,to_char(ship_date,'yyyymmdd')::int as  ship_date_id
	 ,p.prod_id
	 ,s.ship_id
	 ,geo_id
	 ,o.order_id
	 ,sales
	 ,profit
     ,quantity
	 ,discount
from stg.orders o 
inner join dwh.shipping_dim s on o.ship_mode = s.ship_mode
inner join dwh.geography_dim g on o.postal_code = g.postal_code and g.country=o.country and g.city = o.city and o.state = g.state --City Burlington doesn't have postal code
inner join dwh.product_dim p on o.product_name = p.product_name and o.segment=p.segment and o.subcategory=p.subcategory and o.category=p.category and o.product_id=p.product_id 
inner join dwh.customer_dim cd on cd.customer_id=o.customer_id and cd.customer_name=o.customer_name ;











