FROM python:3.10

WORKDIR /usr/src/app
COPY entrypoint.sh .
COPY req.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r req.txt
RUN chmod +x ./entrypoint.sh
COPY . .
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
