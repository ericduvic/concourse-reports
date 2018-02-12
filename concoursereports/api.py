""""""

import os

from .junit import JUnitReport

class Api(object):
    """"""

    def __init__(self, report_location):
        """"""
        self.report_location = report_location
        self.reports = []
        self.load_reports()

    def load_reports(self):
        """"""
        for filename in os.listdir(self.report_location):
            if os.path.splitext(filename)[1] == '.xml':
                self.reports.append(JUnitReport.load_report(filename).test_suites)
