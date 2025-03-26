FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Define environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]