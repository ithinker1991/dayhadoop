#!/usr/bin/env bash

JOB_NAME='ip_lib'
HADOOP_CMD='$HADOOP_HOME/bin/hadoop'
STREAMING_JAR_PATH='$HADOOP_HOME/share/streaming-jar'

OUTPUT_PATH="output/$JOB_NAME/"
IP_LIB_PATH='input/$JOB_NAME/ip.lib.txt'
QUERY_TEXT_PATH="input/$JOB_NAME/query_cookie_ip.txt.small"

hdfs dfs -rm -r $OUTPUT_PATH

$HADOOP_CMD jar $STREAMING_JAR_PATH \
    -input  $QUERY_TEXT_PATH\
    -output $OUTPUT_PATH \
    -mapper "python map.py " \
    -reducer "cat" \
    -file ./map.py \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf  "mapred.job.name=$JOB_NAME" \
    -cacheFile "IP_LIB_PATH/ip.lib.txt#IPLIB"


$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func IPLIB" \
    -reducer "cat" \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf "mapreduce.reduce.memory.mb=5000" \
    -jobconf  "mapred.job.name=ip_lib_demo" \
    -cacheFile "hdfs://master:9000/ip.lib.txt#IPLIB"
    -file "./map.py"