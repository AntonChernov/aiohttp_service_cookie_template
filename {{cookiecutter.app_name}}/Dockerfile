FROM python:3.8

ADD ./ /{{cookiecutter.app_name}}

WORKDIR {{cookiecutter.app_name}}

RUN pip3 install -r /{{cookiecutter.app_name}}/requirements.txt

WORKDIR /{{cookiecutter.app_name}}

CMD python server.py -P 8080

EXPOSE 8080