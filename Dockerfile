FROM dev.exactspace.co/python-base-es2:r1
COPY *.py /tmp/
COPY index /tmp/
COPY main /tmp/
COPY BUILD_TIME /tmp/
RUN chmod +x /tmp/main
RUN chmod +x /tmp/index
WORKDIR /tmp
ENTRYPOINT ["./main"]
