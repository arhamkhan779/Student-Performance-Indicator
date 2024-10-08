import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    Train_Dataset_Path : str=os.path.join('artifacts','train.csv')
    Test_Dataset_Path : str=os.path.join('artifacts','test.csv')
    Raw_Dataset_Path : str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def Initiate_Data_Ingestion(self):
        logging.info("Entered the Data Ingestion Method Or Component")
        try:
            Data_Frame=pd.read_csv('Notebook\\data\\stud.csv')
            logging.info("Read the Dataset as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.Raw_Dataset_Path),exist_ok=True)
            Data_Frame.to_csv(self.ingestion_config.Raw_Dataset_Path,index=False,header=True)
            logging.info("Train Test Split Initiated")

            TRAIN_SET,TEST_SET=train_test_split(Data_Frame,test_size=0.2,random_state=45)
            TRAIN_SET.to_csv(self.ingestion_config.Train_Dataset_Path,index=False,header=True)
            TEST_SET.to_csv(self.ingestion_config.Test_Dataset_Path,index=False,header=True)
            logging.info("Ingestion Of Data is Completed")

            return(
                self.ingestion_config.Train_Dataset_Path,
                self.ingestion_config.Test_Dataset_Path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    Obj=DataIngestion()
    Obj.Initiate_Data_Ingestion()