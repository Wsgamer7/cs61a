.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) as price from inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT a.name, b.store FROM products as a, lowest_prices as b WHERE a.name = b.item 
            GROUP BY a.category HAVING MIN(a.MSRP/a.rating);


CREATE TABLE total_bandwidth AS 
  SELECT SUM(a.Mbs) from stores as a, shopping_list as b WHERE a.store = b.store;

