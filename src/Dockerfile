#Os = Ubuntu 20.04 LTS
FROM ubuntu:20.04

MAINTAINER "johan.piron@chu-brugmann.be"

RUN ENV DEBIAN_FRONTEND=noninteractive apt update -y && ENV DEBIAN_FRONTEND=noninteractive apt install -y python3.9 python3-pip libaio1 wget zip git

#***************************************************************************************************************************************************
#************* Oracle Instant Client install *******************************************************************************************************
#**********************************************************************************************************************>#***************************

#Installation Directory
WORKDIR /opt/oracle

#Pull and unzip client
RUN wget https://download.oracle.com/otn_software/linux/instantclient/216000/instantclient-basic-linux.x64-21.6.0.0.0db>
RUN unzip instantclient-basic-linux.x64-21.6.0.0.0dbru.zip

#Add instant client in the shared library path config file.
RUN sh -c "echo /opt/oracle/instantclient_21_6 > /etc/ld.so.conf.d/oracle-instantclient.conf"

#reload library loader cache
RUN ldconfig

#**********************************************************************************************************************>#*******************************************
#****************************** Clone/Download th REST API *********************************************************************************************************
#**********************************************************************************************************************>#*******************************************

WORKDIR /app

RUN git clone http://johan:Cbr600f4I**@10.20.180.99:31080/gitlab-instance-888dde44/humann-provisioning-refid_iop_prov_a>
WORKDIR /app/humann

#*******************************************************************************************************************************************************************
#**************************** install Python Library in the requirements.txt which is located in the root **********************************************************
#*******************************************************************************************************************************************************************
RUN pip install -r requirements.txt

#**********************************************************************************************************************************

ENTRYPOINT [ "python3" ]
CMD [ "wsgi.py" ]