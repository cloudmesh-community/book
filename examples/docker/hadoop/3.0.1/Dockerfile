# Hadoop 3.0.1
FROM centos

ARG HADOOP_VERSION=3.0.1
ARG HADOOP_HOME=/usr/local/hadoop

RUN yum update -y && \
	    yum install -y openssh-server openssh-clients

USER root

# JDK 8
RUN curl -LO 'http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.rpm' -H 'Cookie: oraclelicense=accept-securebackup-cookie' && \
    rpm -i jdk-8u161-linux-x64.rpm && \
    rm jdk-8u161-linux-x64.rpm
ENV JAVA_HOME /usr/java/default
ENV PATH $PATH:$JAVA_HOME/bin
RUN rm /usr/bin/java && ln -s $JAVA_HOME/bin/java /usr/bin/java

# Passphrase-less SSH using port 2122
ADD conf/ssh_config /root/.ssh/config
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
	    ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \
	    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
	    chmod 600 /root/.ssh/config && chown root:root /root/.ssh/config && \
	    sed  -i "/^[^#]*UsePAM/ s/.*/#&/"  /etc/ssh/sshd_config && \
	    echo "Port 2122" >> /etc/ssh/sshd_config

# Hadoop 3.0.1
RUN curl -s http://apache.cs.utah.edu/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz | tar -xz -C /usr/local && \
	    ln -s /usr/local/hadoop-${HADOOP_VERSION} ${HADOOP_HOME}

# configuration files
COPY conf/core-site.xml.template ${HADOOP_HOME}/etc/hadoop/
COPY conf/core-site.xml ${HADOOP_HOME}/etc/hadoop/core-site.xml
COPY conf/hdfs-site.xml ${HADOOP_HOME}/etc/hadoop/
COPY conf/mapred-site.xml ${HADOOP_HOME}/etc/hadoop/
COPY conf/yarn-site.xml ${HADOOP_HOME}/etc/hadoop/

ENV HDFS_NAMENODE_USER="root"
ENV HDFS_DATANODE_USER="root"
ENV HDFS_SECONDARYNAMENODE_USER="root"
ENV YARN_RESOURCEMANAGER_USER="root"
ENV YARN_NODEMANAGER_USER="root"
ENV HADOOP_HOME="${HADOOP_HOME}"
ENV PATH="$PATH:${HADOOP_HOME}/bin"

RUN echo "export JAVA_HOME=$JAVA_HOME" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh

RUN ${HADOOP_HOME}/bin/hdfs namenode -format
COPY conf/init-dfs.sh /tmp
RUN /tmp/init-dfs.sh

# Statistics Example
RUN mkdir -p /cloudmesh/exer1
COPY exer1 /cloudmesh/exer1

# PageRank Example
RUN mkdir -p /cloudmesh/pagerank
COPY pagerank /cloudmesh/pagerank

COPY conf/bootstrap.sh /etc/bootstrap.sh
CMD ["/etc/bootstrap.sh", "-d"]

# HDFS ports
EXPOSE 50010 50020 50070 50075 50090 8020 9000
# Mapred ports
EXPOSE 10020 19888
#YARN ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088
#SSH port
EXPOSE 2122
