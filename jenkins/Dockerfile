FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y docker.io python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install docker
USER jenkins

# Copy pipeline definitions into the Jenkins reference job directory so that
# they are available on first start.
COPY pipelines /usr/share/jenkins/ref/pipelines
