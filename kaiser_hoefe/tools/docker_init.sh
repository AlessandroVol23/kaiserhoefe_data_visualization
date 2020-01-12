#!/usr/bin/env bash
set -o errexit

root="$(dirname "$0")/.."
echo "Root is ${root}"
app="/kaiser_hoefe"


echo "Initializing database"
# python "${app}/manage.py" wait_for_db
python "${app}/manage.py" makemigrations
python "${app}/manage.py" migrate

if [[ -n "${ADMIN_USERNAME}" ]] && [[ -n "${ADMIN_PASSWORD}" ]] && [[ -n "${ADMIN_EMAIL}" ]]; then
  python "${app}/manage.py" create_admin \
    --username "${ADMIN_USERNAME}" \
    --password "${ADMIN_PASSWORD}" \
    --email "${ADMIN_EMAIL}" \
    --noinput \
  || true
fi

echo "Starting django"
python -u "${app}/manage.py" runserver 0.0.0.0:8000