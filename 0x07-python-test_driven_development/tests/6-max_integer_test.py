#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_positives_and_negatives_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                    7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                    -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                    -8394, 9732, 1695, -4932, -2100, -6920, 2219, -7319,
                    -1193, -422, 9312, 9508, -2690, -9206, 4461, 2997, -6753,
                    -7824, 3097, 1681, 3401, 7221, 1758, -1990, 4958, 4347,
                    7054, 545, 3492, -7285, -1672, 2230, -4576, -3121,
                    -6736, -537, 9823, 4281, -8003, 327, 1824, -1973, -9844,
                    29, 3596, 1108, 6702, 4873, -9452, -5949, -9640, -2156,
                    -4104, 5772, 5121, -2186, -4870, -4116, 6443, -9381,
                    -9388, 8552, 3582, 3500, 7924, 211, -2976, 6346, -5405,
                    899, -3432, -2550, -3353, 6944, 9623]), 9823)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -6867266, -9073637, -6224732, -1080801, -1080228,
                    -6801278, -8351954, -1736432, -746131, -4376995,
                    -967891, -4663691, -71562, -7153670, -8038202,
                    -7893047, -9350883, -1132134, -3675971, -8495354,
                    -9158229, -9310087, -6319598, -8961209, -4906000,
                    -386471, -639929, -2676965, -6881679, -6258057,
                    -5490677, -1107298, -4199148, -5933601, -9917695,
                    -7759849, -7045734, -4885806, -9485075, -5119579,
                    -4147063, -7622811, -4671971, -5439539, -840414,
                    -3671742, -4400074, -3549343, -9146070, -6071672,
                    -7213213, -1307446, -3936098, -2415520, -9162654,
                    -6129976, -5791439, -3481890, -7828832, -6954726,
                    -5272933, -4952516, -6115545, -8333464, -7271456,
                    -4097027, -4342575, -8400559, -8235052, -4373818,
                    -8054214, -8565596, -639225, -2292452, -4269529,
                    -7202853, -6891036, -4379807, -7955196, -1536591,
                    -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_ints_and_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [199872.7619047619, 115249.8813559322, 37972.944444444445,
                    120549.90322580645, 30889.777777777777, 986136.4,
                    393382.5416666667, 15441.826086956522, 2503567,
                    176118.87179487178, 372359.4, 142747.61538461538,
                    383318.8181818182, 297732.2727272727, 104980.52702702703,
                    98409.27272727272, 617459.875, 56556.62162162162, 61958.8,
                    115000.59090909091, 240958.45714285714,
                    101071.85714285714, 77616.47692307692, 89029.64,
                    104941.96666666666, 31940.53846153846, 106652.10126582278,
                    686700.1538461539, 52758.709677419356, 348259.4285714286,
                    89457.28947368421, 58039.52702702703, 306427.53571428574,
                    64379.01176470588, 557699.5333333333, 18718.639344262294,
                    364967.55555555556, 129951.23404255319, 41683.82692307692,
                    139149.9818181818, 356782.86666666664, 100259.07692307692,
                    245204.75, 78972.5306122449, 404825.8888888889, 124364.25,
                    1065047.5, 42946.45614035088, 73670.8813559322,
                    83546.51351351352, 323098.3333333333, 88578.35294117648,
                    89471.0, 47745.197916666664, 17102.676767676767,
                    127735.80882352941, 110513.05882352941,
                    62214.055555555555, 6968.981481481482, 40691.34693877551,
                    69931.09677419355, 67024.44186046511, 112123.04,
                    1167186.0, 140392.05, 15814.362637362638,
                    88923.34444444445, 114726.20731707317, 143303.55,
                    38233.83516483517, 94065.72857142857, 42789.892857142855,
                    44182.47169811321, 41313.101265822785, 67705.18965517242,
                    1222423.5, 44966.55405405405, 37153.6, 82085.08,
                    559793.2857142857, 30031.58823529412, 126947.4262295082,
                    309222.3125, 125132.82089552238, 37276.27397260274,
                    99726.62903225806, 4270.788235294118, 490468.4375,
                    0.45132551361896317, 1.4643609109467473,
                    0.6904822043628014, 7.42850599670902, 0.8174242076055683,
                    0.6560986886071569, 0.6513016647379839, 0.7402037152516,
                    1.3480227709351067, 10.667222236398727,
                    1.1255361340134915, 0.3631658619504303,
                    0.8812949657884553, 1.1100323642668828,
                    5.0119643460188845, 2.8953551308720056,
                    2.5574324632368866, 9.169493642307119, 0.4175692708444569,
                    2.344748944605401, 1.1674261590629318, 0.6998588019912835,
                    0.42770576125452897, 1.7136005979522013,
                    8.877571036363525, 0.6825287480571863, 2.6834294650218338,
                    0.7504024417975861, 0.2762206358275793,
                    0.20607476376994402, 0.9497689034126077,
                    2.1498649449691807]), 29.496355326217376)

    def test_numeric_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
