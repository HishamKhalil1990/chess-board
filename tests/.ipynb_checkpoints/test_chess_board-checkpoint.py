import pytest
from chess_board import Chess_Board

def test_same_row_attack(chess_row):
    expected = True
    actual = chess_row.is_under_attack()
    assert actual == expected
    
def test_same_column_attack(chess_col):
    expected = True
    actual = chess_col.is_under_attack()
    assert actual == expected
    
def test_same_diagonal_attack(chess_dia):
    expected = True
    actual = chess_dia.is_under_attack()
    assert actual == expected
    
def test_other_attack(chess_oth):
    expected = False
    actual = chess_oth.is_under_attack()
    assert actual == expected
    
@pytest.fixture
def chess_row():
    ch = Chess_Board()
    ch.add_red(1,4)
    ch.add_blue(1,7)
    return ch

@pytest.fixture
def chess_col():
    ch = Chess_Board()
    ch.add_red(2,5)
    ch.add_blue(4,5)
    return ch

@pytest.fixture
def chess_dia():
    ch = Chess_Board()
    ch.add_red(3,5)
    ch.add_blue(5,7)
    return ch

@pytest.fixture
def chess_oth():
    ch = Chess_Board()
    ch.add_red(1,3)
    ch.add_blue(3,6)
    return ch