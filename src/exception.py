import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename
    #this will give information about which file and line number has exception
    error_message=("Error Occured in Python Script Name [{0}] Line [{1}] Error Message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    )
        
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

    
##This code creates a custom exception framework that:
##Intercepts a Python exception
##Extracts low-level debugging metadata (file name, line number)
##Formats a human-readable, standardized error message
##Re-raises it as a custom exception that carries context
##❝ Turn raw Python errors into structured, traceable, production-grade error messages ❞