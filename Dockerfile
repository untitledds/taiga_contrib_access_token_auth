FROM taigaio/taiga-back:6.8.1

# Копируем и устанавливаем плагин для аутентификации по токену доступа
COPY --chown=taiga:taiga ./back /tmp/taiga-contrib-access-token-auth
RUN pip install /tmp/taiga-contrib-access-token-auth && \
    rm -rf /tmp/taiga-contrib-access-token-auth

# Копируем настройки и добавляем их в config.py
COPY --chown=taiga:taiga ./config.snippet.py /taiga-back/settings/
RUN cat /taiga-back/settings/config.snippet.py >> /taiga-back/settings/config.py