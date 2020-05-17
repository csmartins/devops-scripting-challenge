FROM centos:7

RUN yum -y install epel-release git-core
RUN yum -y install maven unzip java-1.8.0-openjdk python3 which

ENV CI_PATH /opt/ci/
COPY src $CI_PATH
RUN chmod +x $CI_PATH/ci.py
ENV PATH $PATH:$CI_PATH
RUN alias ci="$CI_PATH/ci.py"