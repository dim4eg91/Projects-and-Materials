-- Создание в схеме stg таблицы orders

DROP TABLE IF EXISTS stg.orders;
CREATE TABLE stg.orders(
   Row_ID        int4  NOT NULL PRIMARY KEY 
  ,Order_ID      text NOT NULL
  ,Order_Date    DATE  NOT NULL
  ,Ship_Date     DATE  NOT NULL
  ,Ship_Mode     TEXT NOT NULL
  ,Customer_ID   text NOT NULL
  ,Customer_Name TEXT NOT NULL
  ,Segment       TEXT NOT NULL
  ,Country       TEXT NOT NULL
  ,City          TEXT NOT NULL
  ,State         TEXT NOT NULL
  ,Postal_Code   text 
  ,Region        TEXT NOT NULL
  ,Product_ID    text NOT NULL
  ,Category      TEXT NOT NULL
  ,SubCategory   TEXT NOT NULL
  ,Product_Name  TEXT NOT NULL
  ,Sales         NUMERIC(9,4) NOT NULL
  ,Quantity      int4  NOT NULL
  ,Discount      NUMERIC(4,2) NOT NULL
  ,Profit        NUMERIC(21,16) NOT NULL
);



