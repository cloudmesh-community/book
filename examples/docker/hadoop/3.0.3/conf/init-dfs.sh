#!/bin/sh
nohup /usr/sbin/sshd -D &
rm -rf /tmp/*.pid
${HADOOP_HOME}/sbin/start-dfs.sh
${HADOOP_HOME}/bin/hdfs dfs -mkdir /user
${HADOOP_HOME}/bin/hdfs dfs -mkdir /user/root
