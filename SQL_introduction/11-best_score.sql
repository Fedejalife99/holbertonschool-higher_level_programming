-- show the scores that are bigger or equals to 10
SELECT `name`, `score`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;