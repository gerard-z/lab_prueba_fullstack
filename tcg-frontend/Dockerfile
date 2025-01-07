FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

# Eliminamos el COPY . . ya que usaremos volúmenes
# COPY . .

EXPOSE 5173

# Habilita polling para hot reload para webpack/vite
ENV CHOKIDAR_USEPOLLING=true
ENV WATCHPACK_POLLING=true     

CMD ["npm", "run", "dev"]