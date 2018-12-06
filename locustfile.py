from locusts.key_value import KeyValueLocust
# from locusts.transit import TransitLocust
from locusts.pki import PkiLocust
# from locusts.dyn_mongodb import MongoDbLocust
# from locusts.dyn_mysql import MysqlLocust
# from locusts.totp import TotpLocust
from locusts.auth_userpass import UserPassAuthLocust
from locusts.auth_approle import AppRoleLocust

__static__ = [KeyValueLocust, PkiLocust]
__dynamic__ = []
__auth__ = [AppRoleLocust, UserPassAuthLocust]

__all__ = __static__ + __dynamic__ + __auth__

# import logging
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True
#
# import http.client
# http.client.HTTPConnection.debuglevel = 1
