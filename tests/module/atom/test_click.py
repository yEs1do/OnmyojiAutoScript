import pytest

from module.atom.click import RuleClick, RuleClickExclude


def test_exclude_click_string_contains_excluded_click_names():
    first = RuleClick((0, 0, 1, 1), (100, 100, 20, 20), name='first')
    second = RuleClick((0, 0, 1, 1), (200, 200, 20, 20), name='second')
    click = RuleClickExclude([first, second], strategy='complement', distribution='uniform')

    assert 'first' in str(click)
    assert 'second' in str(click)
    assert repr(click) == str(click)


@pytest.mark.parametrize('strategy', ['rejection', 'complement'])
@pytest.mark.parametrize('distribution', ['uniform', 'normal'])
def test_exclude_click_strategies_and_distributions(strategy, distribution):
    excluded = RuleClick((0, 0, 1, 1), (100, 100, 200, 150))
    click = RuleClickExclude(excluded, strategy=strategy, distribution=distribution)

    assert isinstance(click, RuleClick)
    for _ in range(200):
        x, y = click.coord()
        assert 0 <= x < 1280
        assert 0 <= y < 720
        assert not (100 <= x < 300 and 100 <= y < 250)


def test_exclude_click_uses_union_of_overlapping_roi_back_regions():
    clicks = [
        RuleClick((0, 0, 1, 1), (100, 100, 200, 150)),
        RuleClick((0, 0, 1, 1), (250, 150, 200, 150)),
    ]
    click = RuleClickExclude(clicks, strategy='complement', distribution='uniform')

    for _ in range(200):
        x, y = click.coord()
        assert not (
            (100 <= x < 300 and 100 <= y < 250)
            or (250 <= x < 450 and 150 <= y < 300)
        )


def test_exclude_click_clips_roi_back_to_screen():
    excluded = RuleClick((0, 0, 1, 1), (-100, -100, 200, 200))
    click = RuleClickExclude(excluded, strategy='complement', distribution='uniform')

    for _ in range(100):
        x, y = click.coord()
        assert x >= 100 or y >= 100


def test_rejection_sampling_falls_back_to_complement(monkeypatch):
    excluded = RuleClick((0, 0, 1, 1), (0, 0, 1279, 720))
    click = RuleClickExclude(excluded, strategy='rejection', distribution='uniform', max_attempts=1)
    sample_point = click._sample_point
    monkeypatch.setattr(
        click,
        '_sample_point',
        lambda rect, distribution: (1, 1)
        if rect == (0, 0, 1280, 720) else sample_point(rect, distribution),
    )

    x, y = click.coord()
    assert x == 1279
    assert 0 <= y < 720


def test_strategy_and_distribution_are_selected_once_at_initialization(monkeypatch):
    choices = iter(['rejection', 'normal'])
    monkeypatch.setattr('module.atom.click.random.choice', lambda values: next(choices))
    click = RuleClickExclude([])

    assert click.strategy == 'rejection'
    assert click.distribution == 'normal'


def test_excluded_regions_covering_screen_are_rejected():
    excluded = RuleClick((0, 0, 1, 1), (0, 0, 1280, 720))
    with pytest.raises(ValueError, match='cover the whole screen'):
        RuleClickExclude(excluded)
