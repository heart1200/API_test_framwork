# 将excel中的预期结果与返回的实际结果进行对比

def assert_result(expect_result, actual_result):
    if expect_result in actual_result:
        flag = True
    else:
        flag = False
    return flag
