import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    PreProcessorObjectPath : str=os.path.join("artifacts","preproccessor.pkl")

class Data_Transformation:
    def __init__(self):
        self.Data_Transformation_Config=DataTransformationConfig()

    def Get_Data_Transformation_Object(self):

        '''
        This Function is Responsible for data transformation
        '''
        try:
            numerical_features=['writing_score','reading_score']
            categorical_features=[
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scalar",StandardScaler(with_mean=False))
                ]
            )

            Categorical_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="most_frequent")),
                    ("HotEncoder",OneHotEncoder()),
                    ("scalar",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical Columns Encoded Completed")
            logging.info("Numerica Columns Scaling Completed")

            preprocessor=ColumnTransformer([
                ("num_pipeline",numerical_pipeline,numerical_features),
                ("categorical_pipeline",Categorical_pipeline,categorical_features)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def Initiate_Data_Transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Train and Test Data Imported Successfully")
            logging.info("Obtaining Preprocessor object")

            preprocessor_obj=self.Get_Data_Transformation_Object()

            target_column_name="math_score"
            numerical_features=['writing_score','reading_score']

            input_feature_train_df=train_df.drop(columns=[target_column_name])
            target_feature_train_df=train_df[[target_column_name]]

            input_feature_test_df=test_df.drop(columns=[target_column_name])
            target_feature_test_df=test_df[[target_column_name]]

            logging.info(
                f"Applying transformation on training and testing dataframe"
            )

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.fit_transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
                ]
            logging.info("Preprocessing object is saved successfully")
            
            save_object(
                file_path=self.Data_Transformation_Config.PreProcessorObjectPath,
                obj=preprocessor_obj
            )
            return(
                train_arr,
                test_arr,
                self.Data_Transformation_Config.PreProcessorObjectPath,
            )

        except Exception as e:
            raise CustomException(e,sys)
            
            
