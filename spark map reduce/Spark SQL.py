## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable(name = 'census2010')
tables = sqlCtx.tableNames()
print(tables)

## 3. Querying ##

haha = sqlCtx.sql('SELECT age FROM census2010')
haha.show()

## 4. Filtering ##

query = 'SELECT males,females FROM census2010 WHERE age > 5 AND age < 15'
haha = sqlCtx.sql(query)
haha.show()

## 5. Mixing Functionality ##

query = 'SELECT males, females FROM census2010'
haha = sqlCtx.sql(query).describe()
haha.show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
df = sqlCtx.read.json('census_1980.json')
df.registerTempTable('census1980')
df = sqlCtx.read.json('census_1990.json')
df.registerTempTable('census1990')
df = sqlCtx.read.json('census_2000.json')
df.registerTempTable('census2000')
tables = sqlCtx.tableNames()

## 7. Joins ##

query = 'SELECT census2010.total,census2000.total from census2010 INNER JOIN census2000 ON census2010.age = census2000.age'
sqlCtx.sql(query).show(20)


## 8. SQL Functions ##

query = 'SELECT SUM(census1990.total),SUM(census2000.total),SUM(census2010.total) FROM census1990 INNER JOIN census2000 ON census1990.age = census2000.age INNER JOIN census2010 ON census2000.age = census2010.age'
sqlCtx.sql(query).show()