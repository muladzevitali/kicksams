FROM python:3.9-slim

ENV DJANGO_SETTINGS_MODULE="config.settings"
WORKDIR /api

RUN apt-get update && apt-get install -y build-essential curl libpq-dev --no-install-recommends
RUN useradd --create-home kicksams
RUN chown kicksams:kicksams -R  /tmp /api

USER kicksams

COPY --chown=kicksams:kicksams requirements.txt /api

ENV PYTHONUNBUFFERED="${PYTHONUNBUFFERED}" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/kicksams/.local/bin" \
    USER="kicksams"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY --chown=kicksams:kicksams . /api
COPY --chown=kicksams:kicksams .env /api/.env
COPY --chown=kicksams:kicksams app-entrypoint.sh /
COPY --chown=kicksams:kicksams celery-entrypoint.sh /

RUN chmod u+x /app-entrypoint.sh
RUN chmod u+x /celery-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]