OK_FORMAT = True

test = {   'name': 'q0',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_0.csv').shape[0] == 69\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_0.csv').iloc[0, 0] == 'information_schema_catalog_name'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
