OK_FORMAT = True

test = {   'name': 'q2c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> cur_test_2c = pickle.load(open("results/result_2c.p", "rb"))\n>>> len(cur_test_2c) == 5\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> cur_test_2c = pickle.load(open("results/result_2c.p", "rb"))\n>>> \'business_info\' in list(cur_test_2c[0].keys())\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
