from odin_control.adapters.adapter import ApiAdapter
from .controller import TemplateTestController, TemplateTestError
._version import __version__


class TemplateTestAdapter(ApiAdapter):
    """TemplateTest Adapter class inheriting base adapter functionality."""

    controller_cls = TemplateTestController
    error_cls = TemplateTestError
    version = __version__
