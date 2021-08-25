FROM python:3.8.10-buster

COPY requirements.txt ./vk_tg_scheduler/

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN pip install -r ./vk_tg_scheduler/requirements.txt --no-cache-dir \
    &&chmod 777 /usr/local/bin/docker-entrypoint.sh \
    && ln -s /usr/local/bin/docker-entrypoint.sh /

WORKDIR ./vk_tg_scheduler

COPY . .

HEALTHCHECK --interval=5s --timeout=5s --retries=5 --start-period=5s CMD curl -f 0.0.0.0:8080/healthcheck || exit 1

EXPOSE 8080

ENTRYPOINT ["docker-entrypoint.sh"]
