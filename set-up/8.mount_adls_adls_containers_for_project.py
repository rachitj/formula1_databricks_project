# Databricks notebook source
# MAGIC %md
# MAGIC ### Mount Azure Data Lake Containers for the Project
# MAGIC

# COMMAND ----------

def mount_adls(storage_account_name,container_name):

    #Get secrets fro azure key vault
    client_id = dbutils.secrets.get(scope="formula1-scope", key="formula1dl-clientid")
    tenant_id = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-tenantid")
    client_secret = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-client-secret")

    # set spark configs
    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
     
    # unmount if mount exists
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        print(f"Unmounting {storage_account_name}/{container_name}")
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{container_name}") 
    # Mount storage acount
    dbutils.fs.mount(
        source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account_name}/{container_name}",
        extra_configs = configs)
    print(f"Mounting {storage_account_name}/{container_name}") 
    
    # display mounted storage account
    display(dbutils.fs.mounts())




# COMMAND ----------

mount_adls("formula1dlrjsa","demo")

# COMMAND ----------

# MAGIC %md
# MAGIC Mount other containers

# COMMAND ----------

mount_adls("formula1dlrjsa","raw")

# COMMAND ----------

mount_adls("formula1dlrjsa","processed")

# COMMAND ----------

mount_adls("formula1dlrjsa","presentation")

# COMMAND ----------

mount_adls("formula1dlrjsa","demo")

# COMMAND ----------


