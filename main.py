from MLFlowProject import logger
from MLFlowProject.pipeline.stage_01_data_ingestions import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
# to test data ingestion stage delete the data folder and run this file
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e