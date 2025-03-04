import pytest
from src.yatzy1 import Yatzy


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

# Changed test: Yatzy.chance arguments now depend from Yatzy's class instance
@pytest.mark.chance
def test_chance_scores_sum_of_all_dice():
    assert Yatzy(2, 3, 4, 5, 1).chance() == 15
    assert Yatzy(3, 3, 4, 5, 1).chance() == 16

# Removed 50 from name
@pytest.mark.yatzy
def test_yatzy_scores():
    assert Yatzy(4, 4, 4, 4, 4).yatzy() == 50
    assert Yatzy(6, 6, 6, 6, 6).yatzy() == 50
    assert Yatzy(6, 6, 6, 6, 3).yatzy() == 0

# Changed test: Yatzy.chance arguments now depend from Yatzy's class instance
@pytest.mark.ones
def test_ones():
    assert Yatzy(1, 2, 3, 4, 5).ones() == 1
    assert Yatzy(1, 2, 1, 4, 5).ones() == 2
    assert Yatzy(6, 2, 2, 4, 5).ones() == 0
    assert Yatzy(1, 2, 1, 1, 1).ones() == 4

# Changed test: Yatzy.chance arguments now depend from Yatzy's class instance
@pytest.mark.twos
def test_twos():
    assert Yatzy(1, 2, 3, 2, 6).twos() == 4
    assert Yatzy(2, 2, 2, 2, 2).twos() == 10

# Changed test: Yatzy.chance arguments now depend from Yatzy's class instance
@pytest.mark.threes
def test_threes():
    assert Yatzy(1, 2, 3, 2, 3).threes() == 6
    assert Yatzy(2, 3, 3, 3, 3).threes() == 12

@pytest.mark.fours
def test_fours_test():
    assert Yatzy(4, 4, 4, 5, 5).fours() == 12
    assert Yatzy(4, 4, 5, 5, 5).fours() == 8
    assert Yatzy(4, 5, 5, 5, 5).fours() == 4

@pytest.mark.fives
def test_fives():
    assert Yatzy(4, 4, 4, 5, 5).fives() == 10
    assert Yatzy(4, 4, 5, 5, 5).fives() == 15
    assert Yatzy(4, 5, 5, 5, 5).fives() == 20

@pytest.mark.sixes
def test_sixes_test():
    assert Yatzy(4, 4, 4, 5, 5).sixes() == 0
    assert Yatzy(4, 4, 6, 5, 5).sixes() == 6
    assert Yatzy(6, 5, 6, 6, 5).sixes() == 18

# Now the arguments must be given to the class
@pytest.mark.score_pair
def test_one_pair():
    assert Yatzy(3, 4, 3, 5, 6).score_pair() == 6
    assert Yatzy(5, 3, 3, 3, 5).score_pair() == 10
    assert Yatzy(5, 3, 6, 6, 5).score_pair() == 12

@pytest.mark.two_pair
def test_two_pair():
    assert Yatzy(3, 3, 5, 4, 5).two_pair() == 16
    assert Yatzy(3, 3, 6, 6, 6).two_pair() == 18
    assert Yatzy(3, 3, 6, 5, 4).two_pair() == 0

@pytest.mark.three_of_a_kind
def test_three_of_a_kind():
    assert Yatzy(3, 3, 3, 4, 5).three_of_a_kind() == 9
    assert Yatzy(5, 3, 5, 4, 5).three_of_a_kind() == 15
    assert Yatzy(3, 3, 3, 3, 5).three_of_a_kind() == 9

@pytest.mark.four_of_a_kind
def test_four_of_a_knd():
    assert Yatzy(3, 3, 3, 3, 5).four_of_a_kind() == 12
    assert Yatzy(5, 5, 5, 4, 5).four_of_a_kind() == 20
    assert Yatzy(3, 3, 3, 3, 3).four_of_a_kind() == 12
    assert Yatzy(3, 3, 3, 2, 1).four_of_a_kind() == 0

@pytest.mark.small_straight
def test_small_straight():
    assert Yatzy(1, 2, 3, 4, 5).small_straight() == 15
    assert Yatzy(2, 3, 4, 5, 1).small_straight() == 15
    assert Yatzy(1, 2, 2, 4, 5).small_straight() == 0

@pytest.mark.large_straight
def test_large_straight():
    assert Yatzy(6, 2, 3, 4, 5).large_straight() == 20
    assert Yatzy(2, 3, 4, 5, 6).large_straight() == 20
    assert Yatzy(1, 2, 2, 4, 5).large_straight() == 0

@pytest.mark.full_house
def test_full_house():
    assert Yatzy(6, 2, 2, 2, 6).full_house() == 18
    assert Yatzy(2, 3, 4, 5, 6).full_house() == 0
    #gelpitests
    assert 0 == Yatzy(2, 2, 3, 3, 4).full_house()
    assert 0 == Yatzy(4, 4, 4, 4, 4).full_house()
    assert 0 == Yatzy(4, 4, 4, 1, 2).full_house()
