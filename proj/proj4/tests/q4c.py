OK_FORMAT = True

test = {   'name': 'q4c',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> cur_test_4c = pickle.load(open("results/result_4c.p", "rb"))\n'
                                               '>>> any([doc["name"] == "Talat Market" and "Thai" in doc for doc in cur_test_4c])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
