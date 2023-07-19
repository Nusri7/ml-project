import sys

def error_message_detail(error,error_detail):
    _,_exc_tb=error_detail.exc_info()
    file_name=_exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in Python script name [{0}] at line number [{1}] with error message [{2}]".format(file_name,_exc_tb.tb_lineno,error)

    return error_message

class CustomException(Exception):
    def __init__(self,error,error_detail):
        super().__init__(error)
        self.error=error
        self.error_detail=error_detail
        self.error_message= error_message_detail(self.error,self.error_detail)
        sys.exit(1) 

    def __str__(self):
        return self.error_message