    Spark JDBC Connection to SQL DB: Python

Step 1: Download JDBC Driver
    1.download "sqljdbc_6.0.8112.200_enu.exe" from here .
    2.Run the exe you will found "Microsoft JDBC Driver 6.0 for SQL Server" folder.
    3.you will find driver jar at "Microsoft JDBC Driver 6.0 for SQL Server\sqljdbc_6.0\enu\jre8" location.

step 2: Python Code
    1.Create "sparkJDBC" folder .
    2.Copy "sqljdbc42.jar" driver file from "Microsoft JDBC Driver 6.0 for SQL Server\sqljdbc_6.0\enu\jre8" to "sparkJDBC" folder.
    3.Open folder in visual code.
    4.Create json file for DB details as "DBDetails.json".
    5.Create DBConnection class in separate file "DBConnection.py".
    6.Create main function in "main.py"

Step 3:Configure TCP port on SQL Server
    1.Open SQL Server Configuration Manager -> SQL Server Network Configuration -> Protocols for <DB Instance Name> -> TCP/IP -> IP Address -> IPALL -> TCP Port 
    2.Change Port Number to 1433.
    3.Restart SQL Service.
    4.Open Command Prompt and execute "netstat -na" to see the port is listing or not. 

Step 4:Execution
    1. Press Ctrl + ` in Visual code to open internal command prompt
    2.execute command "spark-submit --driver-class-path C:\sparkJDBC\sqljdbc42.jar main.py"

Reference:
    •https://docs.databricks.com/spark/latest/data-sources/sql-databases.html
