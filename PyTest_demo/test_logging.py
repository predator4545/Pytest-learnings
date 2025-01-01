import logging


#don't memorise it, just understand


logger = logging.getLogger(__name__)  #logger object will be used to enter/print log details in the file

logFormatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")   #we can to set the format that we could use to add details eg., date,time, message etc. /it's user defined
#C(likly) codes above are used to set the format

# file handler means file location

Filehandler = logging.FileHandler("logfile.log")  #this object contains the file info. in which we need to imprint

Filehandler.setFormatter(logFormatter)    #logFormatter object is passed into File handler

logger.addHandler(Filehandler)  #file handler  object needs to be entered in the add handler

#the below details are in predefined order. so in the following order, details will be added to the sheet
logger.debug("a debug statement is executed")
logger.info("Information statement ")
logger.warning("something is in warning mode")
logger.error("A major has happened")
logger.critical("critival issue")

#if we need to skip some details such as debug from above and to list only remaining 4 in the report, then use below step
logger.setLevel(logging.INFO)

logger.debug("a debug statement is executed")
logger.info("Information statement ")
logger.warning("something is in warning mode")
logger.error("A major has happened")
logger.critical("critival issue")