-- Write your PostgreSQL query statement below
select (select name from department where department.id = employee.departmentId ) as Department,name as Employee , salary as salary from employee
where (salary, departmentId) in
(select max(salary) , departmentId   from employee
group by departmentId )
