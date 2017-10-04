import random
import mysql.connector
from faker import Factory

# config
patients = 1000;
doctors = 200;

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

cnx.close()

