FROM node:18

RUN apt-get update && apt-get install \
    libx11-xcb1 libxcb-dri3-0 libxtst6 libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libdrm2 libgbm1 host \
    -yq --no-install-suggests --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN chown -R node /app
RUN chown root /app/node_modules/electron/dist/chrome-sandbox
RUN chmod 4755 /app/node_modules/electron/dist/chrome-sandbox

USER node
RUN npm install
CMD export REACT_APP_BACK_END=$(host back_end | grep -oP "\d+.\d+.\d+.\d+") && npm start

