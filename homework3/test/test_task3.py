from Task03 import Filter, make_filter, sample_data


def test_filter_class_with_multiple_args():
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(10)) == [2, 4, 6, 8]


def test_filter_class_with_single_arg():
    positive_even = Filter(lambda a: a > 0)
    assert positive_even.apply(range(-4, 4)) == [1, 2, 3]


def test_filter_class_without_arg():
    positive_even = Filter()
    assert positive_even.apply(range(5)) == [0, 1, 2, 3, 4]


def test_make_filter_with_plural_args():
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]


def test_make_filter_with_one_ar():
    assert make_filter(type="person").apply(sample_data) == [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        }
    ]


def test_make_filter_without_args():
    assert make_filter().apply(sample_data) == [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
