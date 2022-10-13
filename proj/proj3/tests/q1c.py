OK_FORMAT = True

test = {   'name': 'q1c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_1c.csv').shape == (4, 2)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> len(pd.read_csv('results/result_1c.csv').iloc[0, 1]) == 122\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
