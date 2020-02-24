# Spark Test
## Overview
This repository is to implement a simple spark test example in python for two huge datasets join.
The Structured API and Spark SQL both have been addressed in the test python function.

## Requirements
* Spark
* Python3
* pyspark

### Installation Guide on Mac
* Install Java
```bash
brew cask install java
```
* Install Scala
```bash
brew install Scala
```
* Install Apache Spark
```bash
brew install apache-spark
```
* Install Python
```bash
brew install python3
```
* Install pyspark
```bash
pip3 install pyspark
```

### Starting a standalone cluster
* Manual Launch
  * Start the master process on the machine that we want to run on. Then the masterprints out a spark://HOST:PORT URI ( http://master-ip-address:8080 by default ) 
 ```bash
        $SPARK_HOME/sbin/start-master.sh
``` 
-  * Start worker nodes by logging into each machine and running the following script using the URI you just received from the master node.
 ```bash
        $SPARK_HOME/sbin/start-slave.sh <master-spark-URI>
```
* Cluster launch scripts
  * Create conf/slaves in your Spark directoryto contain the hostnames of all the machines one per line. The master will 
  access workers via SSH which needed to be setup. Then launch or stop your cluster by scripts. Details at [here](http://spark.apache.org/docs/latest/spark-standalone.html#cluster-launch-scripts)
  
  ```bash
      $SPARK_HOME/sbin/start-all.sh 
      $SPARK_HOME/sbin/stop-all.sh
    ```


### Running the Application 
* Run in a standalone local env
```bash
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.5/libexecexport

$Spark_HOME/bin/spark-submit --master local <working_directory>/spark_test.py
```
* Run a Python application on a Spark standalone cluster. Details at [here](https://spark.apache.org/docs/latest/submitting-applications.html)
```bash
./bin/spark-submit \
  --master spark://207.184.161.138:7077 \
  examples/src/main/python/pi.py
```

