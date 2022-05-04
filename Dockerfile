FROM python:3.8.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir owlready2

# Download Package Information
RUN apt-get update -y
RUN apt-get update && apt-get install -y x11-apps xauth
# Install Tkinter
RUN apt-get install tk -y
# RUN echo "install python, pip and packages through pip"
# RUN chmod +x /app
CMD ["main.py"]
ENTRYPOINT ["python3"]