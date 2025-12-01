from lib.check_codeword import check_codeword

def test_correct_codeword():
    assert check_codeword("horse") == "Correct. Come in."

def test_close_codeword():
    assert check_codeword("house") == "Close, but not quite."

def test_wrong_codeword():
    assert check_codeword("banana") == "WRONG!"