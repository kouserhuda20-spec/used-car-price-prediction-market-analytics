-- PostgreSQL/SQL analytics examples.
-- Table: used_cars

-- 1. Brand performance
SELECT brand, COUNT(*) AS listings, ROUND(AVG(price_lakh),2) AS avg_price
FROM used_cars GROUP BY brand ORDER BY avg_price DESC;

-- 2. Price by vehicle age
SELECT age, ROUND(AVG(price_lakh),2) AS avg_price
FROM used_cars GROUP BY age ORDER BY age;

-- 3. Mileage bands
SELECT CASE
 WHEN kilometers < 30000 THEN '<30K'
 WHEN kilometers < 60000 THEN '30K-60K'
 WHEN kilometers < 100000 THEN '60K-100K'
 ELSE '100K+'
 END AS mileage_band,
 COUNT(*) AS listings, ROUND(AVG(price_lakh),2) AS avg_price
FROM used_cars GROUP BY mileage_band ORDER BY avg_price DESC;

-- 4. Location analysis
SELECT location, COUNT(*) AS listings, ROUND(AVG(price_lakh),2) AS avg_price
FROM used_cars GROUP BY location ORDER BY avg_price DESC;

-- 5. Fuel + transmission segmentation
SELECT fuel, transmission, COUNT(*) AS listings, ROUND(AVG(price_lakh),2) AS avg_price
FROM used_cars GROUP BY fuel, transmission ORDER BY avg_price DESC;

-- 6. Window function: brand rank
SELECT brand, ROUND(AVG(price_lakh),2) AS avg_price,
       RANK() OVER (ORDER BY AVG(price_lakh) DESC) AS price_rank
FROM used_cars GROUP BY brand;

-- 7. Top models by average price
SELECT brand, model, COUNT(*) AS listings, ROUND(AVG(price_lakh),2) AS avg_price
FROM used_cars GROUP BY brand, model
HAVING COUNT(*) >= 10
ORDER BY avg_price DESC LIMIT 20;
