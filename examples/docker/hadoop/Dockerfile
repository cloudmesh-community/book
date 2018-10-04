# Creates pseudo distributed hadoop 2.7.5
#
FROM tianon/centos:6.5

ADD conf/Centos-Source.repo /etc/yum.repos.d/Centos-Source.repo
# Overlay yum patch
RUN rpm --rebuilddb && yum install -y yum-plugin-ovl

RUN yum update -y

RUN yum install -y tar bzip2 yum-utils rpm-build

RUN yum-builddep -y pam
RUN yumdownloader --source pam
RUN rpmbuild --rebuild  --define 'WITH_AUDIT 0' --define 'dist +noaudit' pam*.src.rpm
RUN rpm -Uvh --oldpackage ~/rpmbuild/RPMS/*/pam*+noaudit*.rpm

RUN rm -f /*.rpm
RUN rm -rf ~/rpmbuild

# CENTOS section is complete

# Hadoop installation

USER root

# install dev tools
RUN yum clean all; \
    rpm --rebuilddb; \
    yum install -y curl which tar sudo openssh-server openssh-clients rsync
# update libselinux. see https://github.com/sequenceiq/hadoop-docker/issues/14
RUN yum update -y libselinux

# passwordless ssh
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys


# java
RUN curl -LO 'http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.rpm' -H 'Cookie: oraclelicense=accept-securebackup-cookie' && \
	rpm -i jdk-8u161-linux-x64.rpm && \
	rm jdk-8u161-linux-x64.rpm
	
ENV JAVA_HOME /usr/java/default
ENV PATH $PATH:$JAVA_HOME/bin
RUN rm /usr/bin/java && ln -s $JAVA_HOME/bin/java /usr/bin/java

# hadoop
RUN curl -s http://mirrors.ocf.berkeley.edu/apache/hadoop/common/hadoop-2.7.5/hadoop-2.7.5.tar.gz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./hadoop-2.7.5 hadoop

ENV HADOOP_PREFIX /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_YARN_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop

RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh
#RUN . $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh

RUN mkdir $HADOOP_PREFIX/input
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input

# pseudo distributed
ADD conf/core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template
RUN sed s/HOSTNAME/localhost/ /usr/local/hadoop/etc/hadoop/core-site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml
ADD conf/hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml

ADD conf/mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml
ADD conf/yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml

RUN $HADOOP_PREFIX/bin/hdfs namenode -format

ADD conf/ssh_config /root/.ssh/config
RUN chmod 600 /root/.ssh/config
RUN chown root:root /root/.ssh/config

# # installing supervisord
# RUN yum install -y python-setuptools
# RUN easy_install pip
# RUN curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -o - | python
# RUN pip install supervisor
#
# ADD supervisord.conf /etc/supervisord.conf

ADD conf/bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

ENV BOOTSTRAP /etc/bootstrap.sh

# workingaround docker.io build error
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh

# fix the 254 error code
RUN sed  -i "/^[^#]*UsePAM/ s/.*/#&/"  /etc/ssh/sshd_config
RUN echo "UsePAM no" >> /etc/ssh/sshd_config
RUN echo "Port 2122" >> /etc/ssh/sshd_config

RUN service sshd start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && $HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -mkdir -p /user/root
RUN service sshd start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && $HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -put $HADOOP_PREFIX/etc/hadoop/ input

# Statistic Example
RUN mkdir -p /cloudmesh/exer1
COPY exer1 /cloudmesh/exer1

# PageRank Example
RUN mkdir -p /cloudmesh/pagerank
COPY pagerank /cloudmesh/pagerank
ENV PATH="${HADOOP_PREFIX}/bin:${PATH}"

CMD ["/etc/bootstrap.sh", "-d"]

# Hdfs ports
EXPOSE 50010 50020 50070 50075 50090 8020 9000
# Mapred ports
EXPOSE 10020 19888
#Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088
#Other ports
EXPOSE 49707 2122
