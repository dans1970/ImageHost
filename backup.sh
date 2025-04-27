#!/usr/bin/bash
bu_date=$(date +%Y-%m-%d_%H%M%S)
backup_dir="${BACKUP_DIR:=backups}"
mkdir -p $backup_dir

container="${POSTGRES_CONTAINER:=db}"
db_user="${POSTGRES_USER:=postgres}"
db_name="${POSTGRES_NAME:=postgres}"
file_name="backup_${bu_date}.sql"
docker exec -t $container pg_dump -U $db_user $db_name > $backup_dir/$file_name
#Резервное копирование данных из БД.