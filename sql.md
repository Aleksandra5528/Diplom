Задание 1. Вывод логинов курьеров с заказами в статусе "InDelivery"

SELECT c.login, COUNT(inDelivery)
FROM "Orders" AS o
JOIN "Couriers" AS c ON c.id = o.courierId
WHERE inDelivery = true
GROUP BY c.login;

Задание 2. Вывод всех трекеров заказов и их статусов

SELECT track,
cancelled,
finished,
inDelivery,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN inDelivery = true THEN 1
           ELSE 0
       END
FROM "Orders";

