FROM mysql:8
COPY . /db
RUN chmod +x /db/import_sql_data.sh
RUN /db/import_sql_data.sh