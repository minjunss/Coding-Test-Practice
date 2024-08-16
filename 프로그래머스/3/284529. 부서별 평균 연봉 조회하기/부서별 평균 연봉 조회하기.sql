-- dept_id, dept_name_en, avg(sal)

select 
    hd.dept_id, hd.dept_name_en, round(avg(he.sal), 0) as avg_sal
from
    HR_DEPARTMENT hd
join 
    HR_EMPLOYEES he
on 
    hd.DEPT_ID = he.DEPT_ID
group by 
    dept_id
order by avg_sal desc
