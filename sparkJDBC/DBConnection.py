import json

class DBConnection:
    def __init__(self,spark):
        with open('DBDetails.json') as dbDetails:
            #read json file
            dbDetailsJSON=json.load(dbDetails)
            
            #Create the JDBC Url
            self.Url="jdbc:sqlserver://{0}:{1};database={2};".format(dbDetailsJSON['hostName'],dbDetailsJSON['port'],dbDetailsJSON['databaseName'])
            self.ConnectionProperties={ 
                    "user":dbDetailsJSON['userName'], 
                    "password":dbDetailsJSON['password'], 
                    "driver":"com.microsoft.sqlserver.jdbc.SQLServerDriver" 
            }
            self.spark=spark 

    def getDatarame(self,pushdown_query):
        #Push down a query to the database engine
        df=self.spark.read.jdbc(url=self.Url,table=pushdown_query,properties=self.ConnectionProperties) 
        return df


    