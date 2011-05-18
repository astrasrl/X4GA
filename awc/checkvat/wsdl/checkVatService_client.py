##################################################
# file: checkVatService_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     C:\python25\scripts\wsdl2py.py -b checkVatService.wsdl
# 
##################################################

from checkVatService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class checkVatServiceLocator:
    checkVatPort_address = "http://ec.europa.eu/taxation_customs/vies/services/checkVatService"
    def getcheckVatPortAddress(self):
        return checkVatServiceLocator.checkVatPort_address
    def getcheckVatPort(self, url=None, **kw):
        return checkVatBindingSOAP(url or checkVatServiceLocator.checkVatPort_address, **kw)

# Methods
class checkVatBindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: checkVat
    def checkVat(self, request, **kw):
        if isinstance(request, checkVatRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(checkVatResponse.typecode)
        return response

    # op: checkVatApprox
    def checkVatApprox(self, request, **kw):
        if isinstance(request, checkVatApproxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(checkVatApproxResponse.typecode)
        return response

checkVatRequest = GED("urn:ec.europa.eu:taxud:vies:services:checkVat:types", "checkVat").pyclass

checkVatResponse = GED("urn:ec.europa.eu:taxud:vies:services:checkVat:types", "checkVatResponse").pyclass

checkVatApproxRequest = GED("urn:ec.europa.eu:taxud:vies:services:checkVat:types", "checkVatApprox").pyclass

checkVatApproxResponse = GED("urn:ec.europa.eu:taxud:vies:services:checkVat:types", "checkVatApproxResponse").pyclass
