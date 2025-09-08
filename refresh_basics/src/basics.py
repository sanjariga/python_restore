#!/usr/bin/env python3.12

import sys
import requests
import argparse as vl


__author__ = 'Kostin Aleksandr'

# This script has been created to develop weather app, that will reach up location specific \n
# weather API in specific time intervals. Location at this point will be loading based on \n
# inital user input (could be defined also in config file that will be updated by another app).
# Additional input parameter- selection of measurement system- Imperial or Metric.

class weatherApiReacher(object):

    def __init__(self, region=None, measurement_system=None, city=None):

        if region:
            self.region = region
            self.measurement_system = measurement_system
            self.city = city

        else:
            pass_variables = vl.ArgumentParser(prog=__file__, formatter_class=vl.RawDescriptionHelpFormatter, 
                                            description="Please input your location and what measurement \n" \
                                            "system should be used in output", epilog='''
                                                Example of usage:
                                                    python3.13 %{prog}% -r region -s measurement_system -c city
                                                ''')
            pass_variables.add_argument('r', '--region', choices=['Europe', 'North America', 'South America', 'Asia', 'Pacific', 'Russia'],
                                         help='Region from where you should pick up API', default='Europe')
            pass_variables.add_argument('s', '--measurement_system', choices=['imperial', 'metric'], 
                                        help='2 options: Imperial (Farenheit) and Metric (Celsius)', default='metric')
            pass_variables.add_argument('-c', '--city', type=str, help='Define City and country, which temp you need', required=True)

            self.arguments = pass_variables.parse_args()

            self.region = self.arguments.region
            self.measurement = self.arguments.measurement_system
            self.city = self.arguments.city

    def define_api_endpoint(self):
        pass

    def define_locations_coordinates(self):
        pass

    def define_measurement_units(self):
        pass

    def execute_api_call(self):
        pass

if __name__ == '__main__':
    pass