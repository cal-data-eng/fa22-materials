OK_FORMAT = True

test = {   'name': 'q3e',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_3e.csv').shape == (528, 4)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_3e.csv')['clean_location'].iloc[-1] == 'SYSTEMWIDE'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_3e.csv')['clean_location'].iloc[50] == 'BERKELEY'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
