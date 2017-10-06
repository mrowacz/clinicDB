select count(*) from visit;
select * from visit limit 30 offset 20;

select * from visit where dt >='2017-10-05' and dt <= '2017-10-06';
select * from visit where problem = "chills";
select * from doctors limit 30;

SELECT V.id, V.dt, D.name AS DoctorName, P.name AS patientName , V.problem, V.medicaments
from visit V
LEFT JOIN doctors D ON (V.doctor = D.id)
LEFT JOIN patients P ON (V.patient = P.id)
LIMIT 10;