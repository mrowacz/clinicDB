import random
import datetime
import mysql.connector
from tqdm import *
from faker import Factory

# config
patients = 2000;
doctors = 200;
visits = 10000;

cnx = mysql.connector.connect(user='root', database='clinic', password='db-password')
cur = cnx.cursor(buffered=True)

# queries
new_patient = (
    "INSERT INTO patients (name, address, phone) "
    "VALUES (%s, %s, %s)"
)

new_doctor = (
    "INSERT INTO doctors (name, address, phone, specialization, salary) "
    "VALUES (%s, %s, %s, %s, %s)"
)

for x in xrange(patients):
    fake = Factory.create()
    cur.execute(new_patient, (fake.name(), fake.address(), fake.phone_number()))
cnx.commit()

specializations = map(lambda x: x.rstrip(), open("specialty_list.txt").readlines())
for spec in specializations:
    cur.execute("INSERT INTO specializations(spec) VALUES (%s)", (spec,))
cnx.commit()

for x in xrange(doctors):
     fake = Factory.create()
     cur.execute(new_doctor,
         (fake.name(), fake.address(), fake.phone_number(), random.randint(1, len(specializations)),
         random.randint(6000, 20000)))
cnx.commit()

# generate visits
medicaments = map(lambda x: x.rstrip(), open("medicaments_list.txt").readlines())
illnesses = map(lambda x: x.rstrip(), open("illness_list.txt").readlines())

start = datetime.datetime.strptime("1-10-2017", "%d-%m-%Y")
end = datetime.datetime.strptime("31-10-2017", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

med_bucket = []
for date in  tqdm(date_generated):
    for entries in xrange(1, random.randint(120, 300)):
        doctor_id = random.randint(1, doctors)
        patient_id = random.randint(1, patients)
        problem_type = illnesses[random.randint(1, len(illnesses)-1)]

        med_bucket = ""
        for med_cnt in xrange(1, 3):
            med_bucket += medicaments[random.randint(1, len(medicaments)-1)] + ", "

        new_visit = (
            """INSERT INTO visit (dt, doctor, patient, problem, medicaments)
            VALUES (%s, %s, %s, %s, %s)"""
        )

        tp = (date.isoformat(), doctor_id, patient_id, problem_type, med_bucket)
        cur.execute(new_visit, tp)
    cnx.commit()
    pass

cnx.close()

