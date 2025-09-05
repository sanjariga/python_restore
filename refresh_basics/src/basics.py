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
        pass_variables = vl.ArgumentParser(prog=__file__, formatter_class=vl.RawDescriptionHelpFormatter, 
                                           description="Please input your location and what measurement \n" \
                                           "system should be used in output", epilog='''
                                            Example of usage:
                                                python3.13 %{prog}% -r region -s measurement_system -c city
                                            ''')
        pass_variables.add_argument('r', '--region', type=str, help='Region from where you should pick up API',
                                    required=True)
        pass_variables.add_argument('s', '--measurement_system', choices=['imperial', 'metric'], 
                                    help='2 options: Imperial (Farenheit) and Metric (Celsius)', default='metric')
        pass_variables.add_argument('-c', '--city', type=str, help='Define City, which temp you need', required=True)