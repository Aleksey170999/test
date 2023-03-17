# Задание 4

- SELECT * FROM cities CROSS JOIN orderers;
- select * from orderers o join cities c on o.city_code = c.id;
- select * from cities c join orderers o on c.id = o.city_code;