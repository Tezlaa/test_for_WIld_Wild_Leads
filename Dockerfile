FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER_RUN=True


# Update files
RUN apt-get update && apt-get -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim \
    && apt-get install -y postgresql-client build-essential libpq-dev

# Copy and download requirements
COPY requirements.txt /temp/
RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt

# Add a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Copy the source code
COPY ./src /app/
WORKDIR /app/

# Change ownership to the non-root user
RUN chown -R myuser:myuser .

# Switch to the non-root user
USER myuser

CMD ["manage.py", "runserver", "0.0.0.0:8000"]