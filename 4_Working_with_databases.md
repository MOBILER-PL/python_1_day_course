## Python: Code, Test, Deploy

# Working with databases
 ---

# Synopsis

# Working with databases

## SQLite
[Source](https://sqlite.org/index.html)
[Installation Instructions](https://sqlite.org/index.html)

According to the official docs "SQLite is the most used database engine in the world..."

### Run Sqlite3:
```bash
$ sqlite3
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> 
```

### Import sqlite3 then connect, create, and save a new database table
```python
import sqlite3

conn = sqlite3.connect("operations.db")

c = conn.cursor()

# Create the menu table
c.execute('''CREATE TABLE menu (item text, price real, ingredients text, calories real)''')

# Insert a few rows of data
new_menu_items = [['Ice Cream',2.34,'sugar,water,salt',109],['Brownie',4.50,'sugar,chocolate powder',340],['Hamburger',12.50,'90% Beef,salt,sugar',12000],['Taco',7.00,'Cheese,corn tortilla,chicken,onion',6000],['Cola',2.99,'sugar,water',1200]]

for item in new_menu_items:
    c.execute(f"INSERT INTO menu VALUES ({item[0]},{item[1]},{item[2]},{item[3]})")

# commit your chanegs
conn.commit

# close the database
```
### Query a database table
```python
import sqlite3

conn = sqlite3.connect('operations.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM menu'):
    print(row)
```

## MongoDB
[Source](https://docs.mongodb.com/)
[Installation Instructions](https://docs.mongodb.com/manual/installation/#tutorial-installation)

## Bonus Database Links!
* [The Little MongoDB Book](https://www.openmymind.net/mongodb.pdf)
