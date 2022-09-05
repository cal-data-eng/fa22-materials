OK_FORMAT = True

test = {   'name': 'q4',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_4.csv').iloc[3, 1] == 'Trebek, Alex'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_4.csv')['number'].iloc[:5].sum() == 26115\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
