import kalah

# def test_create_kalah_instance():
#     """This is an example test. Please delete me."""
#     game = kalah.Kalah()


def test_initial_status():
    game1 = kalah.Kalah(6, 4)
    assert game1.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)


def test_illegal_hole():
    game1 = kalah.Kalah(6, 4)
    if game1.current_player == 0:
        assert game1.play(7) == "Hole number too large"
        assert game1.play(8) == "Hole number too large"
        assert game1.play(9) == "Hole number too large"
        assert game1.play(10) == "Hole number too large"
        assert game1.play(11) == "Hole number too large"
        assert game1.play(12) == "Hole number too large"
    # ----------
    if game1.current_player == 1:
        assert game1.play(0) == "Hole number too small"
        assert game1.play(1) == "Hole number too small"
        assert game1.play(2) == "Hole number too small"
        assert game1.play(3) == "Hole number too small"
        assert game1.play(4) == "Hole number too small"
        assert game1.play(5) == "Hole number too small"


def test_simple_move():
    game1 = kalah.Kalah(6, 4)
    assert game1.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
    game1.play(0)
    assert game1.status() == (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0)
    # -----------------
    game2 = kalah.Kalah(6, 4)
    assert game2.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
    game2.play(1)
    assert game2.status() == (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0)
    # -----------------
    game1.play(7)
    assert game1.status() == (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0)
    # -----------------
    game2.play(8)
    assert game2.status() == (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0)
