import pytest

db_user = 'admin'
db_password = 'Admin123'


def login_func(username,password):
    if username and password:
        if username == db_user and password == db_password:
            return "Login success"
        else:
            return "Invalid Credentials"
    else:
        return "Empty Username and Password"

login_success = "Login success"
invlalid_cred = "Invalid Credentials" 
empty_user_pass = "Empty Username and Password"


@pytest.mark.parametrize('user,pwd,expected',
                                      [('admin','Admin123',login_success),
                                       ('Admin123','admin',invlalid_cred), #swap user and password
                                       ('aaaa','Admin123',invlalid_cred), #username wrong
                                       ('admin','dad53',invlalid_cred), #password wrong
                                       (None,None,empty_user_pass),  #username and password empty
                                       (None,"Admin",empty_user_pass), #Username empty
                                       ('admin',None,empty_user_pass)])  #password empty
def test_login_functionality(user,pwd,expected):
    print("Input-->",user,pwd,'Expect-->',expected)
    assert login_func(user,pwd) == expected