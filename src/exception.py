import sys
import logging
def Error_Message_Details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    
    error_message="Error Occured in Python Script Named [{0}] at line[{1}] Error Message [{2}]".format(
        file_name,line_no,str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=Error_Message_Details(error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
    
if __name__ == "__main__":
    try:
        1/0
    except Exception as e:
        logging.info("Divide By Zero")
        raise CustomException(e,sys)

