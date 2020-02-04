FROM python:3.8-alpine3.11

# Setup base
RUN \
    apk add --no-cache \
        git=2.24.1-r0 \
    \
    && pip3 install \
        hassio-repo-updater==0.4.2

# Entrypoint
ENTRYPOINT ["repository-updater"]

# Labels
LABEL \
    maintainer="Andrey Khrolenok <andrey@khrolenok.ru>" \
    org.label-schema.description="Community Hass.io Add-ons Repository Updater" \
    org.label-schema.name="Repository Updater" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/Limych/repository-updater" \
    org.label-schema.usage="https://github.com/Limych/repository-updater/tree/master/README.md" \
    org.label-schema.vcs-url="https://github.com/Limych/repository-updater" \
    org.label-schema.vendor="Community Hass.io Add-ons"
