import inspect
import logging

class LoggerClass():

    def getLogger(self):
        # don't memorise it, just understand
        loggername = inspect.stack()[1][3]    #this will collect run-time tc name

        #inspect.stack()[1][3] in Python is a way to get the name of the calling function by inspecting the call stack. In the context of pytest, you can use this to dynamically capture the name of the current test function being executed.

        #However, using inspect.stack() in pytest may not always be necessary or recommended, as pytest provides cleaner, built-in mechanisms to handle such needs. But understanding how it works can be helpful in certain scenarios.

        #inspect.stack()[1] refers to the calling frame (the test function that called the test_name fixture).
        #[3] retrieves the function name of that frame.

        logger = logging.getLogger(loggername)  # logger object will be used to enter/print log details in the file

        logFormatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # we can to set the format that we could use to add details eg., date,time, message etc. /it's user defined
        # C(likly) codes above are used to set the format

        # file handler means file location

        Filehandler = logging.FileHandler("logfile.log")  # this object contains the file info. in which we need to imprint

        Filehandler.setFormatter(logFormatter)  # logFormatter object is passed into File handler

        logger.addHandler(Filehandler)  # file handler  object needs to be entered in the add handler

        logger.setLevel(logging.INFO)

        return logger
