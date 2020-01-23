import pytest
import kalah

# def test_create_kalah_instance():
#     """This is an example test. Please delete me."""
#     game = kalah.Kalah()


@pytest.fixture()
def game():
    return kalah.Kalah(6, 4)


def test_initial_status(game):
    assert game.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)


def test_illegal_hole(game):
    if game.current_player == 0:
        with pytest.raises(IndexError) as index_error:
            game.play(7)
            game.play(8)
            game.play(9)
            game.play(10)
            game.play(11)
            game.play(12)
        # assert "maximum recursion" in str(index_error.value)
    # ----------
    if game.current_player == 1:
        with pytest.raises(IndexError):
            game.play(0)
            game.play(1)
            game.play(2)
            game.play(3)
            game.play(4)
            game.play(5)


def test_simple_move(game):
    if game.current_player == 0:
        assert game.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
        game.play(0)
        assert game.status() == (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0)
    # -----------------
    game2 = kalah.Kalah(6, 4)
    if game2.current_player == 0:
        assert game2.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
        game2.play(1)
        assert game2.status() == (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0)
    # -----------------
