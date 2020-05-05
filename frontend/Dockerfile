FROM node:alpine AS build

COPY package.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn build

FROM nginx:alpine AS final

COPY --from=build /build/* /usr/share/nginx/html/

COPY boot.sh /
RUN chmod +x /boot.sh && dos2unix /boot.sh
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf.template
CMD ["/boot.sh"]
