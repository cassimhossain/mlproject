#feature engineering + data cleaning
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
import os
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    #creating model and saving as pkl file
    preprocessor_obj_file_path=os.path.join('artifact', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):

        #data transformation function

        try:
            numerical_features=["writing_score","reading_score"]
            categorical_features=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")), #handling of outliers through median
                    ("scaler",StandardScaler())
                ]
            )

            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                ]
            )


            logging.info(f"Categorical Columns:{categorical_features}")
            logging.info(f"Numerical Columns: {numerical_features}")


            preprocessor=ColumnTransformer(
                [
                    ("numerical pipeline", numerical_pipeline, numerical_features),
                    ("categorical pipeline", categorical_pipeline, categorical_features)
                ]
            )


            return preprocessor
        except Exception as e:
            
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Train and Test Data Reading Completed")

            logging.info("Obtaining Preprocessing Object")

            preprocessing_object=self.get_data_transformer_object() #can be converted in to pkl file

            target_column_name="math_score"            
            numerical_features=["writing_score","reading_score"]
            
            input_feature_train_df=train_df.drop(columns=[target_column_name])
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name])
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying PREPROCESSING Object on Training and Testing Dataframes")

            input_feature_train_arr=preprocessing_object.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_object.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info("Saved Preprocessing Object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_object
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e,sys)