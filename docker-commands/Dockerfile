FROM tiangolo/uwsgi-nginx-flask

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app.py /app/main.py
