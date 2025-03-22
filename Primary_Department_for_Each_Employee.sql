-- Write your PostgreSQL query statement below
select employee_id , department_id
from employee
where employee_id in (select employee_id from employee e group by e.employee_id
having count(employee_id) = 1
) or primary_flag = 'Y'
