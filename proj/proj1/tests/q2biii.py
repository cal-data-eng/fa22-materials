OK_FORMAT = True

test = {   'name': 'q2biii',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2biii.csv').iloc[4, 1] == 'The Avengers'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_2biii.csv')['profit'].iloc[:5].sum() == 2260084056.0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
