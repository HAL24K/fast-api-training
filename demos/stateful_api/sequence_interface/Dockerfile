FROM python:3.9-slim

RUN apt-get update && pip install --upgrade pip && pip install streamlit numpy requests

EXPOSE 8501

COPY app /app

WORKDIR /app

CMD ["streamlit", "run", "streamlit_app.py"]
CMD ["streamlit", "run", "streamlit_app.py"]