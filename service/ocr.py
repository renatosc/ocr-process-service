__author__ = 'paulo.rodenas'

from PIL import Image
import pyocr
import pyocr.builders


class PyOCRIntegration(object):

    def __init__(self, lang):
        self.tools = pyocr.get_available_tools()
        self.lang = lang

    def image_to_string(self, filename):
        if len(self.tools) == 0:
            raise PyOCRIntegrationNoOCRFound('No OCR tool has been found on '
                                             'this system. Make sure it\'s on'
                                             'PATH variable of your system')
        result = []
        for tool in self.tools:
            txt = tool.image_to_string(
                Image.open(filename),
                lang=self.lang,
                builder=pyocr.builders.TextBuilder()
            )

            result.append(txt)
        return result


class PyOCRIntegrationNoOCRFound(Exception):

    def __init__(self, message):
        super(Exception, self).__init__(message)