FROM python:3.9

LABEL Name="Django" \
      Version="1.0" \
      Description="Django web application"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py /app/
COPY task_manage/ /app/task_manage/
COPY task/ /app/task/

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]