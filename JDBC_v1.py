import os
import pandas as pd
import mysql.connector

class JDBC(object):
  
  def __init__(self, db):
    self.db = db
    self.user = 'roiblock'
    self.password = os.getenv("SQLCAMPAIGN_PASSWORD")
    self.host = "localhost"
  
  def create_dataframe(self, table):
    """Create pandas DataFrame from a database table
    Args:
      table (string): Table name in database.
    Returns:
      pandas DataFrame: DataFrame from a database table.
    """  
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    query = f"SELECT * FROM {table}"
    data = pd.read_sql(query, connection)
    connection.close()
    return data
  
  def create_dataframe_sql(self, sql):
    """Creates a pandas DataFrame from the provided SQL query.

    Args:
      sql (string): SQL query.

    Returns:
      pandas DataFrame: DataFrame from a database table.
    """  
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    data = pd.read_sql(sql, connection)
    connection.close()
    return data
  
  def overwrite_table(self, df, table):
    """Writes data from a pandas DataFrame to a table in the database.
    Drops the original table and creates a new one with DataTypes infered
    from the pandas dataframe.

    Args:
      df (pandas DataFrame): pandas DataFrame to be written into the database.
      table (string): Name of the table to be overwritten.

    Returns:
      Boolean: True/False based on the outcome of the overwrite.
    """  
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"CREATE TABLE {table} LIKE {df}")
    cursor.close()
    connection.close()
    df.to_sql(table, connection, if_exists='append', index=False)
    print(f"Table {table} successfully saved.")
    return True
  
  def truncwrite_table(self, df, table):
    """Writes data from a pandas DataFrame to a table in the database.
    Truncates the original table while preserving table DataTypes.

    Args:
      df (pandas DataFrame): pandas DataFrame to be written into the database.
      table (string): Name of the table to be overwritten.

    Returns:
      Boolean: True/False based on the outcome of the overwrite.
    """  
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    cursor = connection.cursor()
    cursor.execute(f"TRUNCATE TABLE {table}")
    cursor.close()
    connection.close()
    df.to_sql(table, connection, if_exists='append', index=False)
    print(f"Table {table} successfully saved.")
    return True
  
  def append_table(self, df, table):
    """Appends data from a pandas DataFrame to a table in the database.

    Args:
      df (pandas DataFrame): Data to be appened into the database table.
      table (string): Name of the destination table for the append operation.

    Returns:
      Boolean: True/False based on the outcome of the oappend.
    """  
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    df.to_sql(table, connection, if_exists='append', index=False)
    connection.close()
    return True

  def create_view(self, name, table):
    """Creates a view from a database table so it can be further queried with SQL.

    Args:
      name (string): Name of the created view.
      table (string): Name of the input table.

    Returns:
      Boolean: True/False based on the outcome of the view creation.
    """
    df = self.create_dataframe(table)
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    cursor = connection.cursor()
    cursor.execute(f"DROP VIEW IF EXISTS {name}")
    cursor.execute(f"CREATE VIEW {name} AS SELECT * FROM {table}")
    cursor.close()
    connection.close()
    print(f"View {name} successfully created.")
    return True
  
  def create_view_sql(self, name, sql):
    """Creates a view from a database table based on a query so it can be further queried with SQL.

    Args:
      name (string): Name of the created view.
      sql (string): SQL query.

    Returns:
      Boolean: True/False based on the outcome of the view creation.
    """  
    df = self.create_dataframe_sql(sql)
    connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.db
    )
    cursor = connection.cursor()
    cursor.execute(f"DROP VIEW IF EXISTS {name}")
    cursor.execute(f"CREATE VIEW {name} AS {sql}")
    cursor.close()
    connection.close()
    print(f"View {name} successfully created.")
    return True
