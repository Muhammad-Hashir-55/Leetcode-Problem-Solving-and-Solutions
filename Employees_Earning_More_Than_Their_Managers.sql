-- Write your PostgreSQL query statement below
select e.name as Employee
from Employee e
where e.managerId is not NULL
and
e.salary > (select salary from employee where e.managerId = id);
