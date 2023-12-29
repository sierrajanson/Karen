# 
FROM python:3.11
ENV PYTHONUNBUFFERED 1
#                                                                                                                                                                               
WORKDIR /Karen_python

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]