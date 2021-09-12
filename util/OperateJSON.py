import json


class OperateJSON:
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = '../testdata/user.json'
        with open(self.file_path) as self.fp:
            self.json_value = json.load(self.fp)

    def get_json(self, key):
        return self.json_value[key]


# if __name__ == '__main__':
#     json_file = OperateJSON()
#     con = json_file.get_json('user')
#     con1 = json_file.json_value
#     print(con1)
