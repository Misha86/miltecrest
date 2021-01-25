FROM node:15.5.1-alpine3.10

# Create a directory where our app will be placed
RUN mkdir -p /usr/src/miltec-frontend

# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/miltec-frontend

# Copy dependency definitions
COPY package*.json /usr/src/miltec-frontend/

# Install dependecies
RUN npm i -g npm-upgrade
RUN npm install

# Get all the code needed to run the app
COPY . /usr/src/miltec-frontend/

# Serve the app
# CMD ["npm", "start"]
