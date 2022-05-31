# define Python user-defined exceptions
NOT_FOUND_MESSAGE = "Question not found"
BAD_REQUEST_PASSWORD_MESSAGE = "Missing password field in JSON body"
WRONG_PASSWORD_MESSAGE = "Wrong password"
BAD_TOKEN_MESSAGE = "Wrong token, please reload it"
QUESTION_CREATED_MESSAGE = "Question successfully created"
QUESTION_DELETED_MESSAGE = "Question successfully deleted"
QUESTION_UPDATED_MESSAGE = "Question successfully updated"
INTERNAL_ERROR_MESSAGE = "Internal error : "

class Error(Exception):
    pass

class NotFound(Error):
    pass