import kalah


# def test_create_kalah_instance():
#     """This is an example test. Please delete me."""
#     game = kalah.Kalah()

def test_initial_status():
    game1 = kalah.Kalah()
    assert game1.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
