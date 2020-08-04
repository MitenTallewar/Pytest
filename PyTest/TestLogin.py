

db_user = 'admin'
db_password = 'Admmin123'

def login_func(username,password):
    if username and password:
        if username == db_user and password == db_password:
            return "Login success"
        else:
            return "Invalid Credentials"
    else:
        return "Empty Username and Password"


def test_valid_username_password():
    assert login_func(db_user,db_password) == "Login success"


def test_invalid_username():
    assert login_func('aaaa',db_password) == "Invalid Credentials"


def test_invalid_password():
    assert login_func(db_user,"hjsaka") == "Invalid Credentials"


def tets_invalid_username_password():
    assert login_func('aaaa','hjasak') == 'invalid Credentials'


def test_empty_username_password():
    assert login_func(None,None)=='Empty Username and Password'

