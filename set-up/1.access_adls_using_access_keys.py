# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. List files from demo container ( create storage account: formula1dlrjsa)
# MAGIC     - Create secrets in Azurekey vault
# MAGIC     - Create databricks secrets scope ( Add #secrets/createScope in the url of databricks home page and create scope formula1dl-scope)
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

formula1dl_account_key = dbutils.secrets.get(scope="formula1-scope", key="formula1dlrj-account-key")

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dlrjsa.dfs.core.windows.net",
    formula1dl_account_key)
    

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlrjsa.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlrjsa.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


