from TM1py.Services import LoginService
from TM1py.Services import RESTService
from TM1py.Services import UserService

login = LoginService.native('admin', 'apple')

with RESTService(ip='', port=8001, login=login, ssl=False) as tm1_rest:
    user_service = UserService(tm1_rest)
    user_service.delete('Hodor Hodor')
