OK_FORMAT = True

test = {   'name': 'q1di',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_1di_view.csv').shape == (13, 3)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_1di_no_view.csv').shape == (13, 3)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.sum(pd.read_csv('results/result_1di_view.csv') == pd.read_csv('results/result_1di_no_view.csv')).sum() == 39\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
