FROM python:3.10
RUN mkdir -p /main/fast_api

WORKDIR /fast_api/
COPY . /fast_api/

RUN pip3 install -r req.txt
CMD ["python3", "main.py"]