# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using SAS Token
# MAGIC Steps to follow
# MAGIC - Register Azure AD Application / Service Principal
# MAGIC - Generate a secret/ password for the Application
# MAGIC - Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret
# MAGIC   - Create secrets in Azurekey vault
# MAGIC   - Create databricks secrets scope ( Add #secrets/createScope in the url of databricks home page and create scope formula1dl-scope)
# MAGIC - Assign Role 'Storage Blob Data Contributor' to the Data Lake.

# COMMAND ----------

client_id = dbutils.secrets.get(scope="formula1-scope", key="formula1dl-clientid")
tenant_id = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-tenantid")
client_secret = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-client-secret")

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula1dlrjsa.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.formula1dlrjsa.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.formula1dlrjsa.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.formula1dlrjsa.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.formula1dlrjsa.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlrjsa.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlrjsa.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


