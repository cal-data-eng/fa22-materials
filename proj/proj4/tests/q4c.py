OK_FORMAT = True

test = {   'name': 'q4c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> cur_test_4c = pickle.load(open("results/result_4c.p", "rb"))\n'
                                               ">>> cur_test_4c[0]['name'] == 'Asian Fusion Bowl' and cur_test_4c[0]['category'] == 'Street Vendors'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
