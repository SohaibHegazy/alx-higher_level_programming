-- a script that displays the average temperature (Fahrenheit) by city ordered
-- by temperature (descending).
SELECT city, AVG(value) AS "av"
FROM `temperatures`
GROUP BY city
ORDER BY "av" DESC;
