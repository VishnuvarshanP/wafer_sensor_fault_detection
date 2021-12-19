from datetime import datetime

class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now() #current date and time
        self.date = self.now.date() #taking only the date
        self.current_time = self.now.strftime("%H:%M:%S") #taking only the time
        file_object.write( #writing the log in the txt file
            str(self.date)+"/"+str(self.current_time)+"\t\t"+log_message+"\n"
        )




