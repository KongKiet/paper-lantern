# paper-lantern: OptiSigns support-article scraper / Gemini File Search uploader.
# Python 3.14 matches the local development interpreter used with requirements.txt.
FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Runtime state lives here; bind-mount these to persist across runs.
RUN mkdir -p /app/data/articles /app/state /app/logs

ENTRYPOINT ["python", "main.py"]
CMD ["run"]
