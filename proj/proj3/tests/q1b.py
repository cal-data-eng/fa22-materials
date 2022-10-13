OK_FORMAT = True

test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_1b.csv').shape == (5, 2)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> len(pd.read_csv('results/result_1b.csv').iloc[0, 1]) == 889\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
