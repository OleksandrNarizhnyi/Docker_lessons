FROM node:18-slim

WORKDIR /app

COPY package.json ./

RUN npm install --only=production

COPY app.js ./

CMD ["npm", "start"]