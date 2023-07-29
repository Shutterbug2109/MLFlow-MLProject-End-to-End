from MLFlowProject.config.configuration import ConfigurationManager
from MLFlowProject.components.data_ingestion import DataIngestion
from MLFlowProject import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self): #this is the method from the MLFlowProject package
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") #this is the logger from the MLFlowProject package
        obj = DataIngestionTrainingPipeline() #this is the class from the MLFlowProject package
        obj.main() #this is the method from the MLFlowProject package
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

