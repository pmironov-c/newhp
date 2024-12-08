import os
import pytest


class BaseTest:
    user_name = os.environ.get("CUSTOMER_LOGIN")
