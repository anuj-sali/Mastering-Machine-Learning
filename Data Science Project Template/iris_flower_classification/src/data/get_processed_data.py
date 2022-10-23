import os
import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder



def main(project_dir):
    
    """main method to get the interim data to process it to store as processed_iris.csv
    """
    
    #Initializing logger:
    Logger=logging.getLogger(__name__)

    Logger.info("Getting raw data from local")
    #Getting raw data and processing it:
    interim_data_file = os.path.join(project_dir,'data','interim','interim_iris.csv')


    Logger.info("Processing interim data")
    df = pd.read_csv(interim_data_file, index_col='Id')\
    .assign(Species = lambda x: LabelEncoder().fit_transform(x.Species))

    Logger.info("Saving processed data")
    destination_path = os.path.join(project_dir,'data','processed','processed_iris.csv')
    df.to_csv(destination_path)

if __name__ == '__main__':

    project_dir = os.path.join(os.path.dirname(__file__),os.pardir,os.pardir)

    #Setting up logger:
    logging.basicConfig(filename = 'file.log', \
    level = logging.INFO, \
    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    #call the main method:
    main(project_dir)
