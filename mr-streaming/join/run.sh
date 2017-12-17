#!/usr/bin/env bash


HADOOP_JAR=123
HADOOP_CMD=12
HDFS_CMD=

INPUT1=12
INPUT2=122

OUTPUT=

HDFS dfs -rm -r $OUTPUT

HADOOP jar $HADOOP_JAR \
    -input $INPUT2 \
    -output $OUTPUT1 \
    -mapper "python map_file.py 1" \
    -file ./map_file.py

HADOOP jar $HADOOP_JAR \
    -input $INPUT2 \
    -output $OUTPUT2\
    -mapper "python map_file.py 2" \
    -file ./map_file.py


# cat 作为 mapper
HADOOP jar $HADOOP_JAR \
    -input $OUTPUT2, $OUTPUT1 \
    -output $OUTPUT \
    -mapper "cat" \
    -reducer "python red.py" \
    -file ./map.py \
    -file ./red.py \
    -jobconf num.key.fields.for.partition=1

