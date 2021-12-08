FROM frolvlad/alpine-python-machinelearning

ENV PYTHONPATH "${PYTHONPATH}:/src"
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libc-dev gpgme-dev
RUN apk add linux-headers 

#installing requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#adding files
ADD service.py /service.py
WORKDIR /src
ADD . /src

#run tests
RUN ["pytest", "-vv"]

ENTRYPOINT ["python", "service.py"]