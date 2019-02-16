from statdiagnostics_core import pv_has_malfunction
from statdiagnostics_core import pv_has_malfunction_with_correction
from statdiagnostics_core import pv_correct_expected
from statdiagnostics_core import pv_compute_efficiency
from matplotlib import pyplot as plt

import pandas as pd

def test_statdiagnostics(area, peak_power, expected_data, measured_data, months):

    #normalize data
    expected_data_normalized = [float(i)/sum(expected_data) for i in expected_data]
    measured_data_normalized = [float(i)/sum(measured_data) for i in measured_data]

    pv_efficiency = pv_compute_efficiency(area, peak_power)
    print('computed pv_efficiency 0', pv_efficiency)

    corrected_expected_data = pv_correct_expected(pv_efficiency, expected_data)
    print('expected =', expected_data)
    print('corrected_expected =', corrected_expected_data)
    
    #plot expected data and measured data
    df_rearanged = pd.DataFrame({
        'expected' : [area * value for value in expected_data],
        'expected_with_correction' : [area * value for value in corrected_expected_data],
        'measured' : measured_data

        },index = months
    )
    df_rearanged.plot(kind='bar')
    plt.show()
    print('output =', pv_has_malfunction(area, expected_data, measured_data))
    print('output with correction =', pv_has_malfunction_with_correction(area, peak_power, expected_data, measured_data))

    
    #plot normalized expected data and normalizde measured data
    #df_rearanged = pd.DataFrame({
    #    'reference normalized' : expected_data_normalized,
    #    'measured normalized' : measured_data_normalized
    #    },index = months
    #)
    #df_rearanged.plot(kind='bar')
    #plt.show()
    print('normalized data: output =', pv_has_malfunction(1, expected_data_normalized, measured_data_normalized))
    
    #plot normalized expected data and perturbed normalizde measured data
    #perturb data:
    #measured_data_normalized[5] /= 2
    #measured_data_normalized[6] /= 2
    
    #df_rearanged = pd.DataFrame({
    #    'reference normalized + perturbation' : expected_data_normalized,
    #    'measured normalized + perturbation' : measured_data_normalized
    #    },index = months
    #)
    #df_rearanged.plot(kind='bar')
    #plt.show()
    #print('normalized data + perturbation: output =', pv_has_malfunction(1, expected_data_normalized, measured_data_normalized))
    return

