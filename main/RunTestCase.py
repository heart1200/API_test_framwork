# 根据excel执行测试
from API_practice.util.OperateJSON import OperateJSON
from API_practice.util.OperateExcel import OperateExcel
from API_practice.data_handle.get_excel_data import GetExcelData
from API_practice.base.request_method import RunMethod
from API_practice.data_handle.get_excel_column import GetExcelTitle
from API_practice.util.assert_result import assert_result


class RunTest:
    def __init__(self):
        self.operate_json = OperateJSON()
        self.operate_excel = OperateExcel()
        self.get_excel_data = GetExcelData()
        self.run_method = RunMethod()
        self.column = GetExcelTitle()

    def run_test_case(self):
        case_count = self.get_excel_data.get_case_count()
        for i in range(2, case_count+1):
            url = self.get_excel_data.get_request_url(i)
            method = self.get_excel_data.get_request_method(i)
            is_run = self.get_excel_data.get_is_run(i)
            req_data = self.get_excel_data.get_request_data(i)
            header = self.get_excel_data.is_header(i)
            expect_result = self.get_excel_data.get_expected_data(i)
            if is_run:
                result = self.run_method.test_api(url, method, req_data, header)
                self.operate_excel.write_result(i, self.column.ACTUAL_RESULT, result)
                if assert_result(expect_result, result):
                    self.operate_excel.write_result(i, self.column.IS_PASS, 'PASSED')
                else:
                    self.operate_excel.write_result(i, self.column.IS_PASS, 'FAILED')
                # print(result)
        # return result


if __name__ == '__main__':
    run = RunTest()
    run.run_test_case()
