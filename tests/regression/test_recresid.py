""" Tests for yatsm.regression.recresid
"""
import numpy as np
import xarray as xr
import patsy

from yatsm.regression import recresid


def test_regression_recresid_recresid(airquality):
    """ Test against strucchange R package using airquality data

    R code:
    > R.version
                   _
    platform       x86_64-unknown-linux-gnu
    arch           x86_64
    os             linux-gnu
    system         x86_64, linux-gnu
    status
    major          3
    minor          2.1
    year           2015
    month          06
    day            18
    svn rev        68531
    language       R
    version.string R version 3.2.1 (2015-06-18)
    nickname       World-Famous Astronaut
    > library(strucchange)
    > data('airquality')
    > lm <- lm(Ozone ~ Solar.R + Wind + Temp, data=airquality)
    > rr <- recresid(lm)
    > cat(paste(rr, collapse=', '))
    """
    strucchange_rr = np.array([
        -1.70903937865941, -5.70262862100494, 6.60058663304715,
        -4.84066470078687, -9.61248575241643, 1.22166340836876,
        -9.36237672204679, 3.82041988937251, 21.2202286297367,
        -2.40767376507925, 13.0309632080141, -13.9398122014138,
        -16.2029244910195, -7.72958699626936, -11.6283169957354,
        17.6408339399752, 6.55065388308375, 16.6714666991652,
        64.0654005409762, -13.3454372144415, -25.3623740751964,
        13.7809180271227, -17.6731418418553, -28.3835646695026,
        -10.032312216991, 18.8583862175622, -1.47379402730503,
        -17.981483478909, -21.2139670778193, 73.6763909248311,
        -8.56701113146189, -18.315097880498, 2.94831087378935,
        -10.6994007950455, 7.30225082337986, 22.5973384761887,
        18.275043254397, 15.6018836565117, -17.5303135258411,
        -9.74580210959132, -24.8754321115095, -11.4987235752952,
        -16.0051888513877, -4.38295812383965, 8.23315105331898,
        12.3625362518307, -24.3451078177118, 16.8302442707546,
        46.0832959249389, -29.9822578153195, 5.9927321222946,
        13.7996047183179, -17.6339316511468, 2.36382561737491,
        5.30006070666721, -13.3815998096361, -20.4629900052523,
        -33.6463967653763, 41.4991693964953, 25.3635108460443,
        39.5002714240528, -9.52165469079163, -23.3335897003711,
        18.4343901071501, -12.9188628355704, 9.91295551833012,
        -21.4816340778195, -13.5155949341234, 0.966119266589024,
        -8.62510628674869, -3.00794346768842, -2.58301039970212,
        93.1847641179631, 6.42385051040252, -0.294037879512774,
        15.9399129088867, -6.68532625795045, 0.699550784712069,
        19.6168910430843, -9.09283712184529, -22.8661685960126,
        2.23644540782301, -15.5698178767363, 5.01821309340935,
        -28.5510298040051, -22.3236818310892, -17.7542788195006,
        -17.6153222403174, 10.8703536500043, -3.51339507921876,
        -30.7483018343845, -10.6016989469021, -9.24222318622196,
        -11.4586102655371, 4.08099238771835, -16.2201117976377,
        -4.93377968777668, -41.3922225601194, -0.902543450360464,
        -0.466709711450799, -7.5186145325449, -11.1763927025224,
        28.8236627073026, -10.5175372637295, -9.48699874178777,
        -24.6182062947431, -3.04044885384074
    ])
    # Python implementation
    # np.ndarray
    y = airquality['Ozone'].values
    X = patsy.dmatrix('1 + SolarR + Wind + Temp', data=airquality)

    rr = recresid(X, y)
    np.testing.assert_allclose(rr, strucchange_rr)

    # pd.DataFrame
    y = airquality['Ozone']
    X = patsy.dmatrix('1 + SolarR + Wind + Temp', data=airquality,
                      return_type='dataframe')

    rr = recresid(X, y)
    np.testing.assert_allclose(rr, strucchange_rr)

    # xarray
    y = xr.DataArray(y.squeeze(), coords={'time': y.index}, dims=['time'])
    rr = recresid(X, y)
    np.testing.assert_allclose(rr, strucchange_rr)