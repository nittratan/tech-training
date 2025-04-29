import logging

# Configure logging
logging.basicConfig(
    filename='data.log',
    filemode='a',  # append mode
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
    level=logging.INFO
)

# Create logger instance
logger = logging.getLogger(__name__)
