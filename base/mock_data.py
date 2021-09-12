from unittest import mock


def mock_data_func(mock_method, req_url, req_method, req_data, resp_data):
    mock_method = mock.Mock(return_value=resp_data)
    res = mock_method(req_url, req_method, req_data)
    return res
