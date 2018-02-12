""""""

import logging
import xml.etree.cElementTree as ET

logger = logging.getLogger(__name__)

class JUnitReport(object):
    """Class representing a JUnit report"""

    def __init__(self, report_data):
        """"""
        self.report_data = ET.fromstring(report_data)
        self.test_suites = []
        self.parse_report()

    def parse_report(self):
        """"""
        for test_suite in self.report_data.iter('testsuite'):
            suite = {
                'name': test_suite.attrib['name'],
                'timestamp': test_suite.attrib['timestamp'],
                'time': test_suite.attrib['time'],
                'successes': [],
                'failures': [],
                'errors': []
            }
            for test_case in test_suite.iter('testcase'):
                if test_case.attrib['name'] == 'success':
                    suite['successes'].append({
                        'classname': test_case.attrib['classname'],
                        'time': test_case.attrib['time']
                    })
                elif test_case.attrib['name'] == 'error':
                    error = test_case.find('error')
                    suite['errors'].append({
                        'classname': test_case.attrib['classname'],
                        'time': test_case.attrib['time'],
                        'type': error.attrib['type'],
                        'content': error.text
                    })
                elif test_case.attrib['name'] == 'fail':
                    failure = test_case.find('failure')
                    suite['failures'].append({
                        'classname': test_case.attrib['classname'],
                        'time': test_case.attrib['time'],
                        'type': failure.attrib['type'],
                        'content': failure.text
                    })
                else:
                    logger.warn('Attribute "{}" not handled properly'.format(test_case.attrib['name']))
            self.test_suites.append(test_suite)

    @classmethod
    def load_report(cls, filename):
        """"""
        with open(filename) as report:
            return cls(report.read())
