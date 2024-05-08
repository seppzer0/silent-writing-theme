FROM alpine:3.19 as base

WORKDIR /build

# install npm packages
RUN apk update && apk add npm && npm install -g @vscode/vsce

CMD [ "/bin/sh" ]
