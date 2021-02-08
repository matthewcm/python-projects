import unittest
import skin_classifier

import numpy as np
import pandas as pd

corbyn_data = np.array([[13, 10], [15, 12], [14, 11], [15, 11]])
corbyn = pd.DataFrame(data=corbyn_data, columns=["Area", "Weight"])

boris_data = np.array([
    [18, 13],
    [17, 13],
    [16, 12],
    [18, 14]
])
boris = pd.DataFrame(data=boris_data, columns=["Area", "Weight"])
class NBTest(unittest.TestCase):


    def test_bayesian_classifier(self):
        self.assertEqual(skin_classifier.bayesian_classifier([16, 11], corbyn, boris),
                         True
        )


if __name__ == '__main__':
    unittest.main()

