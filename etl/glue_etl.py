
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

import pip
import pandas as pd
from awsglue.dynamicframe import DynamicFrame
pip.main (['install', 'openpyxl'])
role_profile = pd.read_excel("s3://aspendataxlsx/data_engineer_raw_data.xlsx", sheet_name="role_profile", engine='openpyxl')
borrower = pd.read_excel("s3://aspendataxlsx/data_engineer_raw_data.xlsx", sheet_name="borrower", engine='openpyxl')
df_rp = spark.createDataFrame(
    role_profile, 
    'borrower_id: string, role_profile: string'
)
df_br = spark.createDataFrame(
    borrower,
    'id: string, full_name: string, street: string, city: string, state: string, zip_code: string, phone_home: string, phone_cell: string, email: string'
)
# dyf_rp = DynamicFrame.fromDF(df_rp, glueContext, "role_profile")
# dyf_br = DynamicFrame.fromDF(df_br, glueContext, "borrower")
# print(dyf_rp.printSchema())
# print(dyf_br.printSchema())
# df_rp.take(5)

# role_profile_type
from pyspark.sql.functions import *
from pyspark.sql.types import *
import boto3
distinct_values = df_rp.select(col("role_profile").alias("type")).distinct()
distinct_values_with_index = distinct_values.rdd.map(lambda x: x[0]).zipWithIndex()
rp_type = distinct_values_with_index.toDF(["type", "role_profile_type_id"])
rp_type = rp_type.withColumn("role_profile_type_id", col("role_profile_type_id").cast(IntegerType()))
rp_type = rp_type.withColumn("created", current_timestamp())
account_id = boto3.client("sts").get_caller_identity()["Account"]
rp_type = rp_type.withColumn("created_by", lit(account_id))
rp_type = rp_type.withColumn("updated", lit(None).cast(StringType()))
rp_type = rp_type.withColumn("updated_by", lit(None).cast(StringType()))
# print(rp_type.printSchema())
# print(rp_type.show())
rp_type.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/role_profile_type")

# user
distinct_values = df_br.select(col("id").alias("user_profile_id")).distinct()
distinct_values_with_index = distinct_values.rdd.map(lambda x: x[0]).zipWithIndex()
user = distinct_values_with_index.toDF(["user_profile_id", "user_id"])
user = user.withColumn("user_id", col("user_id").cast(IntegerType()))
user = user.withColumn("created", current_timestamp())
user = user.withColumn("created_by", lit(account_id))
user = user.withColumn("updated", lit(None).cast(StringType()))
user = user.withColumn("updated_by", lit(None).cast(StringType()))
# print(user.printSchema())
# print(user.show())
user.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/user")

# user_profile
up = df_br.withColumn("full_name_split", split(df_br["full_name"], " "))
up = up.withColumn("first_name", up["full_name_split"].getItem(0))
up = up.withColumn("last_name", up["full_name_split"].getItem(1))
up = up.drop("full_name_split")
up = up.select(col("id").alias("user_profile_id"), col("first_name"), col("last_name"))
up = up.withColumn("created", current_timestamp())
up = up.withColumn("created_by", lit(account_id))
up = up.withColumn("updated", lit(None).cast(StringType()))
up = up.withColumn("updated_by", lit(None).cast(StringType()))
# print(up.printSchema())
# print(up.show())
up.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/user_profile")

# role_profile
rp = df_rp.select(col("borrower_id").alias("user_profile_id"), col("role_profile").alias("type"))
rp = rp.join(rp_type, "type", "left")
rp = rp.select(col("user_profile_id"), col("role_profile_type_id"))
rp = rp.join(user, "user_profile_id", "left")
rp = rp.select(col("user_id"), col("role_profile_type_id"))
rp_rdd = rp.rdd.zipWithIndex()
rp = rp_rdd.toDF(['col', 'role_profile_id'])
rp = rp.select("*", col("col.user_id").alias("user_id"), col("col.role_profile_type_id").alias("role_profile_type_id")).drop("col")
# rp = rp.withColumn("role_profile_id", monotonically_increasing_id())
# rp = rp.withColumn("role_profile_id", col("role_profile_id").cast(IntegerType()))
rp = rp.withColumn("created", current_timestamp())
rp = rp.withColumn("created_by", lit(account_id))
rp = rp.withColumn("updated", lit(None).cast(StringType()))
rp = rp.withColumn("updated_by", lit(None).cast(StringType()))
# print(rp.printSchema())
# print(rp.show())
rp.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/role_profile")

# phone_number_type
mapping = [("home", 0), ("cell", 1)]
pn_type = spark.createDataFrame(mapping, ["type", "phone_number_type_id"])
pn_type = pn_type.withColumn("phone_number_type_id", col("phone_number_type_id").cast(IntegerType()))
pn_type = pn_type.withColumn("created", current_timestamp())
pn_type = pn_type.withColumn("created_by", lit(account_id))
pn_type = pn_type.withColumn("updated", lit(None).cast(StringType()))
pn_type = pn_type.withColumn("updated_by", lit(None).cast(StringType()))
# print(pn_type.printSchema())
# print(pn_type.show())
pn_type.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/phone_number_type")
df_br_rpid = df_br.join(user, expr("id = user_profile_id"))
# df_br_rpid.show()

# phone_number
pn = df_br_rpid.selectExpr(
    "stack(2, 'home', phone_home, 'cell', phone_cell) as (type, value)",
    "user_id"
)
pn = pn.filter(pn["value"] != "NaN")
pn = pn.join(pn_type, "type", "left")
pn = pn.select(col("phone_number_type_id"), col("value"), col("user_id"))
# pn = pn.join(user, "user_profile_id", "left")
# pn = pn.select(col("phone_number_type_id"), col("user_id"), col("value"))
pn = pn.join(rp, "user_id", "left")
pn = pn.select(col("phone_number_type_id"), col("role_profile_id"), col("value"))
pn_rdd = pn.rdd.zipWithIndex()
pn = pn_rdd.toDF(['col', 'phone_number_id'])
pn = pn.select("*", col("col.phone_number_type_id").alias("phone_number_type_id"), 
               col("col.role_profile_id").alias("role_profile_id"),
               col("col.value").alias("value")).drop("col")
# pn = pn.withColumn("phone_number_id", monotonically_increasing_id())
# pn = pn.withColumn("phone_number_id", col("phone_number_id").cast(IntegerType()))
pn = pn.withColumn("created", current_timestamp())
pn = pn.withColumn("created_by", lit(account_id))
pn = pn.withColumn("updated", lit(None).cast(StringType()))
pn = pn.withColumn("updated_by", lit(None).cast(StringType()))
# print(pn.printSchema())
# print(pn.show())
pn.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/phone_number")

# address
ad = df_br_rpid.select(col("street"), col("city"), col("state"), col("zip_code"), col("user_id"))
ad = ad.join(rp, "user_id", "left")
ad = ad.select(col("street"), col("city"), col("state"), col("zip_code"), col("role_profile_id"))
ad_rdd = ad.rdd.zipWithIndex()
ad = ad_rdd.toDF(['col', 'address_id'])
ad = ad.select("*", col("col.street").alias("street"), 
               col("col.city").alias("city"),
               col("col.state").alias("state"),
               col("col.zip_code").alias("zip_code"),
               col("col.role_profile_id").alias("role_profile_id")).drop("col")
# ad = ad.withColumn("address_id", monotonically_increasing_id())
# ad = ad.withColumn("address_id", col("address_id").cast(IntegerType()))
ad = ad.withColumn("created", current_timestamp())
ad = ad.withColumn("created_by", lit(account_id))
ad = ad.withColumn("updated", lit(None).cast(StringType()))
ad = ad.withColumn("updated_by", lit(None).cast(StringType()))
# print(ad.printSchema())
# print(ad.show())
ad.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/address")

# email_type
df_br_etype = df_br_rpid.filter(df_br["email"] != "NaN").withColumn("type", split(col("email"), "@")[1])
distinct_values = df_br_etype.select(col("type")).distinct()
distinct_values_with_index = distinct_values.rdd.map(lambda x: x[0]).zipWithIndex()
e_type = distinct_values_with_index.toDF(["type", "email_type_id"])
e_type = e_type.withColumn("email_type_id", col("email_type_id").cast(IntegerType()))
e_type = e_type.withColumn("created", current_timestamp())
e_type = e_type.withColumn("created_by", lit(account_id))
e_type = e_type.withColumn("updated", lit(None).cast(StringType()))
e_type = e_type.withColumn("updated_by", lit(None).cast(StringType()))
# print(e_type.printSchema())
# print(e_type.show())
e_type.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/email_type")


# email
e = df_br_etype.select(col("email"), col("type"), col("user_id"))
e = e.join(rp, "user_id", "left")
e = e.select(col("email"), col("type"), col("role_profile_id"))
e = e.join(e_type, "type", "left")
e = e.select(col("email").alias("value"), col("email_type_id"), col("role_profile_id"))
e_rdd = e.rdd.zipWithIndex()
e = e_rdd.toDF(['col', 'email_id'])
e = e.select("*", col("col.value").alias("value"), 
               col("col.email_type_id").alias("email_type_id"),
               col("col.role_profile_id").alias("role_profile_id")).drop("col")
# e = e.withColumn("email_id", monotonically_increasing_id())
# e = e.withColumn("email_id", col("email_id").cast(IntegerType()))
e = e.withColumn("created", current_timestamp())
e = e.withColumn("created_by", lit(account_id))
e = e.withColumn("updated", lit(None).cast(StringType()))
e = e.withColumn("updated_by", lit(None).cast(StringType()))
# print(e.printSchema())
# print(e.show())
e.write.format("csv").option("timestampFormat", "yyyy-MM-dd HH:mm:ss").mode("overwrite").save("s3://aspendatatar/aspen/email")

job.commit()

