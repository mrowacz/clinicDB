use clinic;

select d.name, spec.spec 
from 
    doctors as d,
    specializations as spec
where
    d.specialization = spec.id
order by d.name