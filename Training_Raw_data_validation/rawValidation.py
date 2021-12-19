from application_logging.logger import App_Logger
import json
import os
from os import listdir
import shutil

class Raw_Data_validation:
    """
    This class shall be used for handling all the validation done on the Raw Training Data!!.
    """
    def __init__(self,path):
        self.Batch_Directory = path
        self.schema_path = "schema_training.json"
        self.logger = App_Logger()

    def valuesFromSchema(self):
        """
        This method extracts all the relevant information from the pre-defined "Schema" file.
        Output: LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, Number of Columns
        On Failure: Raise ValueError,KeyError,Exception
        """
        try:
            with open(self.schema_path,'r') as f:
                dic = json.load(f) #key value data
                f.close()
            pattern = dic['SampleFileName']
            LengthOfDateStampInFile = dic['LengthOfDateStampInFile']
            LengthOfTimeStampInFile = dic['lengthOfTimeStampInFile']
            column_names = dic['columns']
            NumberOfColumns = dic['NumberofColumns']

            file = open("Training_Logs/valuesfromSchemavalidationLog.txt",'a+')
            message = "LengthOfDateStampInFile:: %s" %LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile +"\t " + "NumberofColumns:: %s" %NumberOfColumns + "\n"
            self.logger.log(file,message)
            file.close()

        except ValueError:
            file = open("Training_logs/valuesfromSchemavalidationLog.txt",'a+')
            self.logger.log(file,"valueError: Value not found inside schema_training.json")
            file.close()
            raise ValueError
        except KeyError:
            file = open("Training_Logs/valuesfromSchemaValidationLog.txt", 'a+')
            self.logger.log(file, "KeyError:Key value error incorrect key passed")
            file.close()
            raise KeyError

        except Exception as e:
            file = open("Training_Logs/valuesfromSchemaValidationLog.txt", 'a+')
            self.logger.log(file, str(e))
            file.close()
            raise e

        return LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,NumberOfColumns

    def manualRegexCreation(self):
        """
        Description: This method contains a manually defined regex based on the "FileName" given in "Schema" file.
                                            This Regex is used to validate the filename of the training data.
                                Output: Regex pattern
                                On Failure: None
        """
        regex = "['wafer']+['\_'']+[\d_]+[\d]+\.csv"
        return regex

    def createDirectoryForGoodBadRawData(self):
        """
        Method Name: createDirectoryForGoodBadRawData
        Description: This method creates directories to store the Good Data and Bad Data
        after validating the training data.
        Output: None
        On Failure: OSError
        """
        try:
            path = os.path.join("Training_Raw_files_validated/","Good_Raw/")
            if not os.path.isdir(path):
                os.makedirs(path)
            path = os.path.join("Training_Raw_files_validated/","Bad_Raw/")
            if not os.path.isdir(path):
                os.makedirs(path)
        except OSError:
            file = open("Training_Logs/GeneralLog.txt",'a+')
            self.logger.log(file,"Error while creating Directory %s"%OSError)
            file.close()
            raise OSError


    def deleteExistingGoodDataTrainingFolder(self):
        """
         Method Name: deleteExistingGoodDataTrainingFolder
         Description: This method deletes the directory made  to store the Good Data
         after loading the data in the table. Once the good files are
         loaded in the DB,deleting the directory ensures space optimization.
         Output: None
         On Failure: OSError
        """
        try:
            path = 'Training_Raw_files_validated/'
            if os.path.isdir(path+'Good_Raw/'):
                shutil.rmtree(path+'Good_Raw') #shutil. rmtree() is used to delete an entire directory tree
                file = open('Training_Logs/GeneralLog.txt','a+')
                self.logger.log(file,"Goodraw directory deleted successfully!!!")
                file.close()
        except OSError:
            file = open('Training_Logs/GeneralLog.txt','a+')
            self.logger.log(file,"Error while Deleting Directory : %s"%OSError)
            file.close()
            raise OSError


    def deleteExistingBadDataTrainingFolder(self):

        """
        Method Name: deleteExistingBadDataTrainingFolder
        Description: This method deletes the directory made to store the bad Data.
        Output: None
        On Failure: OSError
        """

        try:
            path = 'Training_Raw_files_validated/'
            if os.path.isdir(path + 'Bad_Raw/'):
                shutil.rmtree(path + 'Bad_Raw/')
                file = open("Training_Logs/GeneralLog.txt", 'a+')
                self.logger.log(file,"BadRaw directory deleted before starting validation!!!")
                file.close()
        except OSError:
            file = open("Training_Logs/GeneralLog.txt", 'a+')
            self.logger.log(file,"Error while Deleting Directory : %s" %OSError)
            file.close()
            raise OSError







