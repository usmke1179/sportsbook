def decimaltoamerican(decimalodds):
    if decimalodds > 2:
        return (decimalodds - 1.) * 100.
    else:
        return -100. / (decimalodds - 1.)


def americantodecimal(americanodds):
    if americanodds < 0:
        return 1. / (americanodds / -100.) + 1.
    else:
        return (americanodds / 100.) + 1.


def oddstowinpercent(odds):
    if odds < 0:
        return abs(odds) / (abs(odds) + 100.)
    else:
        return 100. / (abs(odds) + 100.)


def impliedwinpercent(resultside, otherside):
    if resultside < 0:
        return -resultside / (100. - resultside)
    else:
        return 100. / (100. + resultside)


def kellycriterion(expected, americanodds, multiplier):
    w = americantodecimal(americanodds) - 1.
    p = expected
    k = multiplier
    return ((w * p) ^ k - (1. - p) ^ k) / ((w * p) ^ k + w * (1. - p) ^ k)


def novig(resultside, otherside):
    return impliedwinpercent(resultside, otherside) / (impliedwinpercent(resultside, otherside) + impliedwinpercent(otherside, resultside))


def adjustedvig(resultside, otherside):
    adjusted = novig(resultside, otherside) + .025
    if adjusted <= .5:
        return (100. * (1. - adjusted)) / adjusted
    elif adjusted > .5:
        return -(adjusted * 100.) / (1. - adjusted)
