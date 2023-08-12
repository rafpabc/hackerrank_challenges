select 
t0.company_code,
t0.founder,
t1.count_lead,
t2.count_senior,
t3.count_man,
t4.count_emp
from
(select t0.company_code,t0.founder from company t0) t0
left join
(select t1.company_code,count(t1.company_code) count_lead from
(select distinct company_code,lead_manager_code from lead_manager) t1 group by
t1.company_code) t1
on t0.company_code = t1.company_code
left join
(select t2.company_code,count(t2.company_code) count_senior from
(select distinct company_code,senior_manager_code from senior_manager) t2 group by
t2.company_code) t2
on t0.company_code = t2.company_code
left join
(select t3.company_code,count(t3.company_code) count_man from
(select distinct company_code,manager_code from manager) t3 group by
t3.company_code) t3
on t0.company_code = t3.company_code
left join
(select t4.company_code,count(t4.company_code) count_emp from
(select distinct company_code,employee_code from employee) t4 group by
t4.company_code) t4
on t0.company_code = t4.company_code
order by t0.company_code asc;