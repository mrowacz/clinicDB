# clinicDB
clinic database example

# mysql server

```bash
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=db-password -v ${MYSQL_DIR}:/var/lib/mysql mysql

further use only

docker start mysql

or

docker stop mysql

```
