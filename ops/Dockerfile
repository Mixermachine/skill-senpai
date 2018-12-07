
FROM python:2

WORKDIR /usr/src/app

RUN apt install default-libmysqlclient-dev

COPY ./ops/python_requirements ./
RUN pip install --no-cache-dir -r python_requirements

COPY ./ops/migrate_and_run.sh ./

COPY ./studysite/ ./

RUN ["chmod", "+x", "migrate_and_run.sh" ]

ENTRYPOINT ["python", "manage.py"]

CMD [ "runserver", "0.0.0.0:8000" ]
