"""
tests.pytests.unit.utils.win_dacl.test_get_sid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test the get_sid function in the win_dacl utility module
"""
# Python libs
import pytest

# Salt libs
import salt.utils.win_dacl

# Third-party libs
try:
    import pywintypes
    import win32security

    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False

pytestmark = [
    pytest.mark.windows_whitelisted,
    pytest.mark.skip_unless_on_windows,
]


def test_get_sid_string():
    """
    Validate getting a pysid object from a name
    """
    sid_obj = salt.utils.win_dacl.get_sid("Administrators")
    assert isinstance(sid_obj, pywintypes.SIDType)
    assert win32security.LookupAccountSid(None, sid_obj)[0] == "Administrators"


def test_get_sid_sid_string():
    """
    Validate getting a pysid object from a SID string
    """
    sid_obj = salt.utils.win_dacl.get_sid("S-1-5-32-544")
    assert isinstance(sid_obj, pywintypes.SIDType)
    assert win32security.LookupAccountSid(None, sid_obj)[0] == "Administrators"
