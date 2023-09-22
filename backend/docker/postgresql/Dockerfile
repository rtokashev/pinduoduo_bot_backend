FROM postgres

RUN apt-get update && apt-get -y install git build-essential postgresql-server-dev-16
RUN git clone https://github.com/citusdata/pg_cron.git
RUN cd pg_cron && make && make install
COPY postgres/scripts/init.sql /docker-entrypoint-initdb.d/
COPY postgres/scripts/cron.sql /docker-entrypoint-initdb.d/
COPY postgres/scripts/triggers.sql /docker-entrypoint-initdb.d/
