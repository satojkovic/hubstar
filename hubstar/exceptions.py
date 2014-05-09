#-*- coding: utf-8 -*-

ERROR_CODE_UNAUTHORIZED = 401
ERROR_CODE_UNKNOWN_OBJECTS = 404
ERROR_CODE_INTERNAL = 405


class HsErrorUnauthorized(Exception):
    error_code = ERROR_CODE_UNAUTHORIZED


class HsErrorInternal(Exception):
    error_code = ERROR_CODE_INTERNAL


class HsErrorUnknownObject(Exception):
    error_code = ERROR_CODE_UNKNOWN_OBJECTS
