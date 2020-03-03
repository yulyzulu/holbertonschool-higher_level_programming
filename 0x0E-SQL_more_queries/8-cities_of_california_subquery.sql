-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT states FROM cities
WHERE name = (SELECT name FROM cities WHERE name = 'California')
ORDER BY cities.id DESC;
