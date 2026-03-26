FROM metabase/metabase:latest

RUN mkdir -p /metabase-data && chown 2000:2000 /metabase-data

COPY --chown=2000:2000 metabase.db.mv.db /metabase-data/

ENV MB_DB_FILE=/metabase-data/metabase.db