# Write your MySQL query statement below
SELECT email as Email
from Person email
GROUP BY email
HAVING count(email) > 1;