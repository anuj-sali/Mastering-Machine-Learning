import os
import pandas as pd
import logging

def main(project_dir):
    
    """main method to get the process the data data and store it as processed_iris.csv
    """
    
    #Initializing logger:
    Logger=logging.getLogger(__name__)

    Logger.info("Getting raw data from local")
    #Getting raw data and processing it:
    raw_data_file = os.path.join(project_dir,'data','raw','Iris.csv')



    Logger.info("Processing raw data")
    df = pd.read_csv(raw_data_file,index_col='Id') \
    .assign(Species = lambda x: x.Species.str.slice(5,)) \
    .rename(columns=dict(zip(['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'],["SL","SW","PL","PW"])))

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
