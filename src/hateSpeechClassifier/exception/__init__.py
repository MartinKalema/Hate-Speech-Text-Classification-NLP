import sys as system


def generate_error_message(error, error_detail: system):
    try:
        exc_type, exc_value, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = "Error occurred in file [{0}] at line number [{1}]: {2}".format(
            file_name, line_number, str(error))
        error_message += f"\nException type: {exc_type.__name__}"

        error_message += f"\nException value: {str(exc_value)}"
    except AttributeError:
        error_message = "An error occurred hence could not retrieve traceback information."

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = generate_error_message(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message