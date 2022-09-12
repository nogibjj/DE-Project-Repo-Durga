#! /bin/bash

import os
os.environ["SPARK_HOME"] = "/home/vscode/spark-3.1.1-bin-hadoop3.2"

import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from pyspark.sql.functions import *

df = spark.read.csv("/workspaces/DE-Project-Repo-Durga/data/loan.csv", inferSchema = True, header = True)
df.printSchema()
