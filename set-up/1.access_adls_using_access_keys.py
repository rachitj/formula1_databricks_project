# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. List files from demo container ( create storage account: formula1dlrjsa)
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dlrjsa.dfs.core.windows.net",
    "<input-access-key>")
    

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlrjsa.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlrjsa.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


