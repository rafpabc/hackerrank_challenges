select t1.n,
case
    when t1.p is null then 'Root'
    when t2.p is null then 'Leaf' 
    else 'Inner' end as type
from bst t1
left join
(select distinct(t2.p) from bst t2 where t2.p is not null) t2
on t1.n = t2.p
order by t1.n;