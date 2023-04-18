for f in /var/lib/mysql/data/users/*.csv.gz
do
    gunzip -d $f
    mysql --local-infile=1 -u root -pccccc1234 m3_db -e "SET unique_checks=0; LOAD DATA LOCAL INFILE '${f%.gz}' INTO TABLE users COLUMNS terminated by '\t' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done