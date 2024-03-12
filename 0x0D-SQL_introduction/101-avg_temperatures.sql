-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS "average"  FROM temperature GROUP BY city ORDER BY "average" DESC;
