""" Here we have helper functions.
Helper functions will perform calculations that we may need"""
def scaleRpmToGauge(rpm=0):
    ''' Will scale the RPM to fit the gauge.
        We will take 0 - 8K RPM and make it match the min of 0 to Max of 125. '''
    max_RPM = 8000
    max_gauge = 125
    answer = (rpm * max_gauge) / max_RPM
    return answer


