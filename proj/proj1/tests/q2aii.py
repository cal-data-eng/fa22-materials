OK_FORMAT = True

test = {   'name': 'q2aii',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2aii.csv').shape[0] == 20\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_2aii.csv')['movie_id'].iloc[:10].sum() == 16333796\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
