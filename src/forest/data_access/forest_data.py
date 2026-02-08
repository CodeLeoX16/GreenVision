from src.forest.configuration.mongo_db_connection import MongoDBClient
from src.forest.constant.database import DATABASE_NAME
from src.forest.exception import ForestException
import pandas as pd
import sys
from typing import Optional
import numpy as np

class ForestData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise ForestException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                if self.mongo_client.client is None:
                    raise ForestException("MongoDB client is not initialized", sys)
                collection = self.mongo_client.client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise ForestException(e,sys)

