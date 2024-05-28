FROM python:3.8.12

# Set working directory in the container
WORKDIR /app

# Copy model code and requirements file
COPY app.py /app/app.py
COPY script.py /app/script.py
COPY app_model/96308_knn_model.pkl /app/app_model/96308_knn_model.pkl
COPY static /app/static
COPY templates /app/templates
COPY __pycache__ /app/__pycache__

COPY requirements.txt requirements.txt

EXPOSE 5000
# Install dependencies
RUN pip install -r requirements.txt
RUN ls
# RUN python script.py 2000 2000 7 2
# Define command to run your model

# CMD ["python", "script.py", "2000", "2000", "7", "2"]
# CMD ["python", "app/app.py"]
# CMD ["python", "flask run --host=0.0.0.0 "]
# CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["flask", "run", "--host", "0.0.0.0"]
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD flask run -h 0.0.0.0 -p 5000
