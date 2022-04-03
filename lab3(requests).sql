#1
 Получить список туров с датой, на неделю превышающей текущую.

SELECT * FROM tourorders WHERE startdate BETWEEN '2019-11-25' AND '2019-12-01' AND enddate BETWEEN '2019-11-25' AND '2019-12-01'

#2
  Получить список свободных номеров каждого типа в конкретном отеле (на усмотрение студента) на текущую дату. При необходимости внести изменения в структуру БД. (добавить кол-во комнат)(разница)

SELECT h.title, r.title,  r.quantity - COUNT(ro.room) avelable
FROM Rooms r 
LEFT OUTER JOIN roomorders ro ON ro.room = r.id AND CURRENT_DATE BETWEEN startdate AND enddate
INNER JOIN Hotels h ON h.id = r.hotel
GROUP BY h.title, r.title, r.quantity;
#3
Получить список клиентов, побывавших абсолютно во всех странах, представленных в базе агентства./
#4
 Получить туров, в описании которых содержится какой-либо из вариантов слова «экскурси(и|я)».

SELECT * FROM Tours WHERE Description SIMILAR TO '%экскурси(и|я)%'
#5
  Получить перечень туров, ранжированных по количеству посещаемых стран.

SELECT title, city FROM Tours ORDER BY city;
#6
 Поднять стоимости всех туров в конкретную страну в 3 раза. При необходимости выполнить несколько запросов.

UPDATE tours SET price = price * 3 WHERE city = 1
#6/2 (обратная)
UPDATE tours SET price = price / 3 WHERE city = 1
#7
 Отменить перевозку (даже на заказанные туры) конкретным видом транспорта в конкретную страну (вид и страна на усмотрение студента). При необходимости выполнить несколько запросов.(Удалить заказы с перевозкой в конкретную страну)
#8
SELECT tour, SUM(prices) FROM tourorders WHERE tour = 2 GROUP BY tour
#9
Составить список клиентов, отправляющихся в поездку в заданный период.
#10
Получить список клиентов заказавших в рамках тура отель(-и), но не заказавших проезд (трансфер).