OK_FORMAT = True

test = {   'name': 'q3b',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_3b.csv').iloc[0, 0] == 30.0\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_3b.csv').iloc[0, 2] == 2317091.0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
