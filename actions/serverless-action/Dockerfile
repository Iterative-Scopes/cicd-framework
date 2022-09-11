FROM node:slim
RUN npm install -g serverless 
ENV SLS_INTERACTIVE_SETUP_ENABLE 0
COPY entrypoint.sh entrypoint.sh
RUN mkdir src
ENTRYPOINT ["./entrypoint.sh"]