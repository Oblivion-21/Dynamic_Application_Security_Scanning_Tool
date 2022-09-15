FROM node:18

# RUN echo '::1' >> /etc/hosts

RUN apt-get update && apt-get install \
    libx11-xcb1 libxcb-dri3-0 libxtst6 libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libdrm2 libgbm1 xauth pip \
    -yq --no-install-suggests --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN chown -R node /app
RUN chown root /app/gui/node_modules/electron/dist/chrome-sandbox
RUN chmod 4755 /app/gui/node_modules/electron/dist/chrome-sandbox

USER node
# RUN pip install -r requirements.txt
# RUN python3 API.py

RUN cd ./gui && npm install
CMD cd ./gui && npm start


###########################################################################################
# This works as well, if you are having issues getting the electron GUI up give this a go #
###########################################################################################

# FROM centos
# RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
# RUN yum install firefox -y
# CMD firefox
