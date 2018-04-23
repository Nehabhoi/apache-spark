from pyspark.sql import SparkSession
from DBConnection import DBConnection

if __name__ == "__main__":
    #get spark session object
    spark = SparkSession.builder.appName("JDBCSpark").getOrCreate()

    #get DBConnection object
    dbConnection=DBConnection(spark)

    #Push down a query to the database engine
    df=dbConnection.getDatarame("<Table Name>")

    #show the Result
    df.show()

#execute the below command
#spark-submit --driver-class-path <driver path> main.py