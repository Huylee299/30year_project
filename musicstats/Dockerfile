FROM python:3.10

WORKDIR /msmusicapi

COPY . /msmusicapi

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV NAME TestMusic

CMD ["python3", "manage.py", "runserver"]