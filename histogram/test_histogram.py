import unittest
import histogram


example_figure = {
    "0": 790,
    "1": 1023,
    "2": 850,
    "3": 656,
    "4": 329,
    "5": 245,
    "6": 122,
    "7": 81
}

example_cum_figure = {

    "0": 790,
    "1": 1813,
    "2": 2663,
    "3": 3319,
    "4": 3648,
    "5": 3893,
    "6": 4015,
    "7": 4096
}
example_equalised_figure = {

    "0": 1,
    "1": 3,
    "2": 5,
    "3": 6,
    "4": 6,
    "5": 7,
    "6": 7,
    "7": 7
}


class HistogramTests(unittest.TestCase):

    def test_cum_frequency(self):

        print('Testing Cum frequency')
        self.assertEqual(
            histogram.cumulative_freq_figure(example_figure),
            example_cum_figure
        )


    def test_apply_histogram(self):

        print('Checking histogram equalisation applied to example is correct')
        self.assertEqual(histogram.apply_histogram(example_cum_figure, max_g=8, n=64, m=3),
            example_equalised_figure

       )


if __name__ == '__main__':
    unittest.main()