import polars as pl

import tvtsplit


def main():

    test_tvtsplit()


def test_tvtsplit():

    params = {"shuffle": False, "seed": 0, "val_size": 0.25, "test_size": 0.25}
    sample_df = pl.DataFrame(
        data=["aaa", "bbb", "ccc", "ddd", "eee", "fff"],
        schema=[("txt", pl.String)],
    )

    actual = sample_df.tvtsplit.train(params)["txt"].to_list()  # type: ignore[unresolved-attribute]
    expected = ["aaa", "bbb", "ccc", "ddd"]

    assert actual == expected


# I put a dummy function because the formatter deletes "import tvtsplit".
def dummy():
    tvtsplit()  # type: ignore[call-non-callable]


if __name__ == "__main__":
    main()
