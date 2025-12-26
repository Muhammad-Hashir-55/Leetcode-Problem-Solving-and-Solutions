-- Write your PostgreSQL query statement below
select w.id
from weather w
where w.temperature > (select ww.temperature from weather ww where ww.recorddate = (w.recorddate -1) )
