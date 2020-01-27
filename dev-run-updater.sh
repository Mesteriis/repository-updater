#!/usr/bin/env bash

ROOT_DIR=$(dirname "$(readlink -f "$0")")

set -a
. "${ROOT_DIR}/.env.dev"
set +a

python3 -m repositoryupdater  --token ${GITHUB_TOKEN} --repository Limych/hassio-addons --dry-run
