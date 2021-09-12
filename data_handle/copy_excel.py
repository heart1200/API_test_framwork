# 复制一份excel，以防将原始文件覆盖
import datetime

import openpyxl


def copy_excel(source_file_path=None):
    now_time = datetime.datetime.now()
    str_now = now_time.strftime('%Y%m%d%H%M%S')
    if source_file_path:
        wb = openpyxl.load_workbook(f'{source_file_path}/case1.xlsx')
        wb.save(f'../testdata/{str_now}.xlsx')
        file_path = f'../testdata/{str_now}.xlsx'
    else:
        wb = openpyxl.load_workbook('../testdata/case1.xlsx')
        wb.save(f'../testdata/{str_now}.xlsx')
        file_path = f'../testdata/{str_now}.xlsx'
    return file_path


