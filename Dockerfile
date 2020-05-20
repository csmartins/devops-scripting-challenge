FROM centos:7

RUN yum -y install epel-release git-core
RUN yum -y install maven unzip java-1.8.0-openjdk python3 which pip3 git
RUN pip3 install pipenv

ENV CI_PATH /opt/ci
COPY src $CI_PATH
COPY Pipfile $CI_PATH/Pipfile
COPY Pipfile.lock $CI_PATH/Pipfile.lock
RUN chmod +x $CI_PATH/ci.py
ENV PATH $PATH:$CI_PATH
RUN alias ci="pipenv run $CI_PATH/ci.py"

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
WORKDIR $CI_PATH
RUN pipenv install --deploy --system --ignore-pipfile