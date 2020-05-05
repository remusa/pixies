FROM node:alpine AS build

COPY package.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn build

FROM nginx:alpine AS final

COPY --from=build build/* /usr/share/nginx/html/
