FROM python:3.9-slim as base

# Update existing packages and install necessary SSL/TLS related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends openssl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

    # get packages
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app


#install opentelemetry packages
RUN pip install opentelemetry-distro \
	opentelemetry-exporter-otlp

RUN opentelemetry-bootstrap -a install

# Add the application
COPY app.py .

ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_LOGS_EXPORTER=otlp

EXPOSE 8082

# ENTRYPOINT [ "opentelemetry-instrument", "python", "main.py"]
CMD ["opentelemetry-instrument", "flask", "run", "--host", "0.0.0.0", "--port", "8082"]
