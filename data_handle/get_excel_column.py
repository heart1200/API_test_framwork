# 获取excel的标题栏

class GetExcelTitle:
    ID = 1
    MODULE = 2
    URL = 3
    RUN_STATUS = 4
    REQUEST_METHOD = 5
    COOKIE = 6
    CASE_DEPENDENT = 7
    RETURN_DEPENDENT = 8
    DEPENDENT_FIELD = 9
    REQUEST_DATA = 10
    EXPECTED_RESULT = 11
    ACTUAL_RESULT = 12
    IS_HEADER = 13
    IS_PASS = 14

    def get_id(self):
        return GetExcelTitle.ID

    def get_module(self):
        return GetExcelTitle.MODULE

    def get_url(self):
        return GetExcelTitle.URL

    def get_run_status(self):
        return GetExcelTitle.RUN_STATUS

    def get_request_method(self):
        return GetExcelTitle.REQUEST_METHOD

    def get_cookie(self):
        return GetExcelTitle.COOKIE

    def get_case_dependent(self):
        return GetExcelTitle.CASE_DEPENDENT

    def get_dependent_field(self):
        return GetExcelTitle.DEPENDENT_FIELD

    def get_request_data(self):
        return GetExcelTitle.REQUEST_DATA

    def get_expected_result(self):
        return GetExcelTitle.EXPECTED_RESULT

    def get_actual_result(self):
        return GetExcelTitle.ACTUAL_RESULT

    def get_is_header(self):
        return GetExcelTitle.IS_HEADER

    def get_is_pass(self):
        return GetExcelTitle.IS_PASS