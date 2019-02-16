def pv_efficiency(area, expected, measured):
    """
    :param area: area covered by the pv in m^2
    :param expected: list of expected kWh/m^2 ordered by month
    :param measured: list of measured kWh values ordered by months the same way as expected
    :return: true if there is a malfunction
    """

    ex = [value * area for value in expected]
    me = measured

    return float(sum(me))/float(ex)