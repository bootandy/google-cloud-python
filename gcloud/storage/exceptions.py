class StorageError(Exception):
    pass


class ConnectionError(StorageError):

    def __init__(self, response, content):
        message = str(response) + content
        super(ConnectionError, self).__init__(message)


class NotFoundError(ConnectionError):

    def __init__(self, response, content):
        self.message = 'Request returned a 404. Headers: %s' % (response)


class StorageDataError(StorageError):
    pass
