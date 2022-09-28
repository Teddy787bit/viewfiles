FROM alpine:latest
ENV hostname myhost
RUN apk update &&  apk upgrade
