from path_finder import get_paths


class TestPath:
    def test_empty_available(self):
        assert get_paths((0,), []) == [(0,)]

    def test_oneitem_available(self):
        assert get_paths((0,), [1]) == [(0, 1)]

    def test_simple_paths(self):
        assert get_paths((), [0, 1]) == [(0, 1), (1, 0)]

    def test_more_paths(self):
        assert get_paths((), [0, 1, 2]) == [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
