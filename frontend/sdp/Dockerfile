FROM node:14 AS frontend

WORKDIR /app/frontend/sdp

COPY ./frontend/sdp /app/frontend/sdp

RUN npm install
RUN npm run build

WORKDIR /app/frontend

CMD ["npm", "start"]