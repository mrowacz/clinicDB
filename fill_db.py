import mysql.connector
from faker import Factory

cnx = mysql.connector.connect(user='root', database='clinic', password='db-password')
cur = cnx.cursor(buffered=True)

new_patient = (
    "INSERT INTO patients (name, address, phone) "
    "VALUES (%s, %s, %s)"
  )

for x in xrange(100):
    fake = Factory.create()
    cur.execute(new_patient, (fake.name(), fake.address(), fake.phone_number()))
    cnx.commit()

cnx.close()

