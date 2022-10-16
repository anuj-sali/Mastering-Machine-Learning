import os
import prefect
from prefect import task,flow
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import logging


def main(project_dir):
    ''' main method to get kaggle data & store it in raw folder of data'''
    
    #Get the logger:
    logger = logging.getLogger(__name__)
    logger.info("Getting the raw data")

    logger.info("Authenticating kaggle dataset:")
    #call authenticate kaggle
    api = authenticate_kaggle()
    
    #raw_data_file_path to which data will be downloaded.
    raw_data_file_path = os.path.join(project_dir,'data','raw')

    logger.info("Downloading iris kaggle dataset:")
    #download kaggle dataset & store in raw_data folder
    api.dataset_download_file('uciml/iris',file_name='Iris.csv',path=raw_data_file_path)

    logger.info("Downloaded iris kaggle dataset & store in raw folder of data:")


def authenticate_kaggle():
    api= KaggleApi()
    api.authenticate()
    return api

if __name__== "__main__":
    #Define the project directory
    project_dir = os.path.join(os.path.dirname(__file__),os.pardir,os.pardir)

    #Setting up logger:
    logging.basicConfig(filename = 'file.log',
                    level = logging.INFO,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    #call the main 
    main(project_dir)
