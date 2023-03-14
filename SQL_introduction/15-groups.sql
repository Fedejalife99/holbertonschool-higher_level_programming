--Show the scores that are repited in the table
SELECT `score`, COUNT(*) AS `number`
FROM `hbtn_0c_0.second_table`
GROUP BY `score`
ORDER BY `number` DESC;