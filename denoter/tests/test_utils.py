from denoter import utils


def test_slugify():
    assert utils.slugify("Reinout is a great name!") == "reinout-is-a-great-name"
