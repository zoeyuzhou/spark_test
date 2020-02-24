import sys
import time
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .master("local") \
        .appName("spark_test") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    file1 = spark.read.format("csv").options(header='true', inferSchema='true').load('/Users/zoe/Applications/py_spark_test/spark_test/data/file1.csv')
    file2 = spark.read.format("csv").options(header='true', inferSchema='true').load('/Users/zoe/Applications/py_spark_test/spark_test/data/file2.csv')

    # if the file got the duplicated columnName
    file1 = file1.withColumnRenamed("id","id_1")
    file2 = file2.withColumnRenamed("id","id_2")

    # For API join mode
    result = file1.join(file2,on='token')
    result.show()

    """
        # For SQL mode    
        file1.createOrReplaceTempView("file1")
        file2.createOrReplaceTempView("file2")
        query = '''SELECT * FROM file1 JOIN file2 ON file1.token = file2.token'''
        result = spark.sql(query)
        result.show()
    """

    ts1 = time.strftime('%X_%d_%m_%Y')
    result.write.format("csv")\
        .option("mode", "OVERWRITE")\
        .option("header", "true")\
        .option("path","/Users/zoe/Applications/py_spark_test/spark_test/data/result_" + ts1)\
        .save()


if __name__=="__main__":
    sys.exit(main())

