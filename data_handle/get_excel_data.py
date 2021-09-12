# 获取excel中的值

from API_practice.util.OperateExcel import OperateExcel
from API_practice.data_handle.get_excel_column import GetExcelTitle
from API_practice.util.OperateJSON import OperateJSON


class GetExcelData:
    def __init__(self):
        self.opera_excel = OperateExcel()

    # 获取行数，也就是case数
    def get_case_count(self):
        return self.opera_excel.get_sheet_rows()

    # 获取是否执行
    def get_is_run(self, row):
        column = GetExcelTitle.RUN_STATUS
        is_run = self.opera_excel.get_cell_value(row, column)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

        # 是否携带header
    def is_header(self, row):
        col = GetExcelTitle.IS_HEADER
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = GetExcelTitle.REQUEST_METHOD
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = GetExcelTitle.URL
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = GetExcelTitle.REQUEST_DATA
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, key):
        opera_json = OperateJSON()
        request_data = opera_json.get_json(key)
        return request_data
    # def get_data_for_json(self, row):
    #     opera_json = OperetionJson()
    #     request_data = opera_json.get_data(self.get_request_data(row))
    #     return request_data

    # 获取预期结果
    def get_expected_data(self, row):
        col = GetExcelTitle.EXPECTED_RESULT
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 通过sql获取预期结果
    # def get_expcet_data_for_mysql(self, row):
    #     op_mysql = OperationMysql()
    #     sql = self.get_expcet_data(row)
    #     res = op_mysql.search_one(sql)
    #     return res.decode('unicode-escape')

    def write_result(self, row, value):
        col = GetExcelTitle.ACTUAL_RESULT
        self.opera_excel.write_result(row, col, value)

    # 获取依赖数据的key
    # def get_depend_field(self, row):
    #     col = GetExcelTitle.DEPENDENT_FIELD
    #     depend_field = self.opera_excel.get_cell_value(row, col)
    #     if depend_field == "":
    #         return None
    #     else:
    #         return depend_field
    #
    # # 判断是否有case依赖
    # def is_depend(self, row):
    #     col = GetExcelTitle.
    #     depend_case_id = self.opera_excel.get_cell_value(row, col)
    #     if depend_case_id == "":
    #         return None
    #     else:
    #         return depend_case_id
    #
    # # 获取数据依赖字段
    # def get_depend_field(self, row):
    #     col = int(data_config.get_field_depend())
    #     data = self.opera_excel.get_cell_value(row, col)
    #     if data == "":
    #         return None
    #     else:
    #         return data
