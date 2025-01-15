-- 코드를 입력하세요
SELECT P.PRODUCT_ID, P.PRODUCT_NAME, sum(p.price*o.amount) AS TOTAL_SALES
FROM FOOD_PRODUCT P
JOIN FOOD_ORDER O
ON P.PRODUCT_ID = O.PRODUCT_ID
where to_char(o.produce_date, 'YYYYMM') = '202205'
GROUP BY p.PRODUCT_ID, p.product_name
ORDER BY TOTAL_SALES desc, P.PRODUCT_ID ASC