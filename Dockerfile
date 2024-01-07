FROM runpod/pytorch:2.0.1-py3.10-cuda11.8.0-devel

WORKDIR /

RUN pip install runpod

ENV CUDA_DOCKER_ARCH=all
ENV LLAMA_CUBLAS=1
RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

ADD handler.py .
COPY ./models/* /models/

CMD ["python", "-u", "handler.py"]