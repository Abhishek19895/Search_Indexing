"""
-- Author: Abhishek Singh
--connecting to EMR - r3.4xlarge instance (320 Gibs/Instance) 2 Master No slaves
--ssh -i Abhishek_DC_Project.pem hadoop@ec2-52-53-180-198.us-west-1.compute.amazonaws.com

--Copy data from S3 to hdfs in the /dchw folder
--hadoop fs -cp s3://projectdistri/ /dchw
"""

--Entering HIVE
hive
set hive.cli.print.header=true; #To get all headers

--HiveQl queries for data loading & Data querying
--Creating the ‘text_data’ table
CREATE TABLE text_data (title string)
CLUSTERED BY (title) SORTED BY (title) 
INTO 32 BUCKETS
STORED AS TEXTFILE;

--Loading the data from hdfs to hive table
LOAD DATA INPATH '/dchw/full_data.txt' OVERWRITE INTO TABLE text_data;

--Querying for specific strings
select * from text_data
where title like '%Dog food%'
limit 5;

--Barack Obama 
--Chinese San Francisco
--Tomato soup recipes
--German Shepherd
--Fast Cars
--Pretty woman
--Great beaches
--Short circuit
--Car Crash