OK_FORMAT = True

test = {   'name': 'q2bii',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2bii.csv').iloc[0, 2] == 'Pirates of the Caribbean: At World\\'s End'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_2bii.csv')['budget'].iloc[:5].sum() == 1318000000.0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
