FROM python:3.8-slim
WORKDIR /ml2
COPY requirements.txt /ml2/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /ml2/
EXPOSE 8501
CMD ["streamlit", "run", "ml2.py"]
