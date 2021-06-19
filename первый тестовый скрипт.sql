select 
customer_id as Покупатель,
product_Name as Товар
from kuzmin_test.orders
where order_date = '2016-06-09';


select
distinct customer_id as Покупатель,
count(product_id) as Куплено_товаров,
sum(sales) as Потрачено
from kuzmin_test.orders o
where order_date = '2016-06-09'
group by 1;