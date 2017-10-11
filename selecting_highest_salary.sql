# show highest salary from each specialization
select specs.spec, max(docs.salary)
from
    doctors as docs,
    specializations as specs
where specs.id = docs.specialization
group by docs.specialization;

# show average salary per specialization
select specb.spec, avg(docs.salary)
from 
    doctors as docs,
    specializations as specb
where
    specb.id = docs.specialization
group by specb.spec

