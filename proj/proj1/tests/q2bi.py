OK_FORMAT = True

test = {   'name': 'q2bi',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2bi.csv').iloc[0, 2] == 'Avatar'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_2bi.csv')['gross'].iloc[:5].sum() == 3038331946.0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
