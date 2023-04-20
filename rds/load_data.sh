for f in ./address/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE address COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./email/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE email COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./email_type/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE email_type COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./phone_number/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE phone_number COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./phone_number_type/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE phone_number_type COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./role_profile/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE role_profile COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./role_profile_type/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE role_profile_type COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./user/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE user COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done

for f in ./user_profile/*
do
    mysql --local-infile=1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;SET SQL_MODE='ALLOW_INVALID_DATES';" -h dms-sample.cu144p4hztzw.us-east-1.rds.amazonaws.com -P 3306 -u admin -pchangeit aspen -e "LOAD DATA LOCAL INFILE '$f' INTO TABLE user_profile COLUMNS terminated by ',' LINES TERMINATED BY '\n';"
echo "Done: '"$f"' at $(date)"
done