OK_FORMAT = True

test = {   'name': 'q3e',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> important_attribute_business_df = pd.read_csv('results/result_3e.csv')\n"
                                               '>>> len(important_attribute_business_df) == 1000 and len(important_attribute_business_df.columns) != 58\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
