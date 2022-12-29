from logger import setup_logger
import os
import time
log_path = '/var/log/cron_reminder'
log_file = os.path.join(log_path, 'cron_reminder.log')
logger = setup_logger('cron_reminder', log_file)

while 1:
    
    logger.info('Running reminder emails')
    time.sleep(600)
