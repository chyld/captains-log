FROM ubuntu:18.10

RUN apt-get update && \
    apt-get install -y build-essential gdb vim tree htop

COPY .bashrc /root

# docker build -t cpp .
# docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app --cap-add=SYS_PTRACE --security-opt seccomp=unconfined cpp bash
