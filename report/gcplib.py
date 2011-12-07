#!/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         report/gcplib.py
# Author:       Fabio Cassini <fabio.cassini@gmail.com>
# Copyright:    (C) 2011 Astra S.r.l. C.so Cavallotti, 122 18038 Sanremo (IM)
# ------------------------------------------------------------------------------
# This file is part of X4GA
# 
# X4GA is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# X4GA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with X4GA.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

import mimetools, mimetypes
import urllib
import urllib2
import httplib
import time
import string
import base64

CRLF = '\r\n'
BOUNDARY = mimetools.choose_boundary()

# The following are used for authentication functions.
FOLLOWUP_HOST = 'www.google.com/cloudprint'
FOLLOWUP_URI = 'select%2Fgaiaauth'
GAIA_HOST = 'www.google.com'
LOGIN_URI = '/accounts/ServiceLoginAuth'
LOGIN_URL = 'https://www.google.com/accounts/ClientLogin'
SERVICE = 'cloudprint'
OAUTH = 'This_should_contain_oauth_string_for_your_username'

# The following are used for general backend access.
CLOUDPRINT_URL = 'http://www.google.com/cloudprint'
# CLIENT_NAME should be some string identifier for the client you are writing.
CLIENT_NAME = 'Cloud Print API Client'

class TestLogger(object):
    
    def debug(self, msg, *args):
        self.output(msg, 'debug', *args)
    
    def info(self, msg, *args):
        self.output(msg, 'info', *args)
    
    def error(self, msg, *args):
        self.output(msg, 'error', *args)
    
    def output(self, msg, tipo, *args):
        if False:
            print '%s: %s' % (tipo, msg % args)

# The following object are used in the sample code, but not necessary.
logger = TestLogger()


## All of the calls to GetUrl assume you've run something like this:
#tokens = GetAuthTokens(email, password)


AUTH_TOKENS = None
def SetAuthTokens(tokens):
    global AUTH_TOKENS
    AUTH_TOKENS = tokens

def InitAuthTokens(user, pswd):
    tokens = GetAuthTokens(user, pswd)
    SetAuthTokens(tokens)


def EncodeMultiPart(fields, files, file_type='application/xml'):
    """Encodes list of parameters and files for HTTP multipart format.

    Args:
      fields: list of tuples containing name and value of parameters.
      files: list of tuples containing param name, filename, and file contents.
      file_type: string if file type different than application/xml.
    Returns:
      A string to be sent as data for the HTTP post request.
    """
    lines = []
    for (key, value) in fields:
        lines.append('--' + BOUNDARY)
        lines.append('Content-Disposition: form-data; name="%s"' % key)
        lines.append('')  # blank line
        lines.append(value)
    for (key, filename, value) in files:
        lines.append('--' + BOUNDARY)
        lines.append(
          'Content-Disposition: form-data; name="%s"; filename="%s"'
          % (key, filename))
        lines.append('Content-Type: %s' % file_type)
        lines.append('')  # blank line
        lines.append(value)
    lines.append('--' + BOUNDARY + '--')
    lines.append('')  # blank line
    return CRLF.join(lines)


def GetUrl(url, tokens, data=None, cookies=False, anonymous=False):
    """Get URL, with GET or POST depending data, adds Authorization header.
    
    Args:
      url: Url to access.
      tokens: dictionary of authentication tokens for specific user.
      data: If a POST request, data to be sent with the request.
      cookies: boolean, True = send authentication tokens in cookie headers.
      anonymous: boolean, True = do not send login credentials.
    Returns:
      String: response to the HTTP request.
    """
    request = urllib2.Request(url)
    if not anonymous:
        if cookies:
            logger.debug('Adding authentication credentials to cookie header')
            request.add_header('Cookie', 'SID=%s; HSID=%s; SSID=%s' % (
                tokens['SID'], tokens['HSID'], tokens['SSID']))
        else:  # Don't add Auth headers when using Cookie header with auth tokens.   
            request.add_header('Authorization', 'GoogleLogin auth=%s' % tokens['Auth'])
    request.add_header('X-CloudPrint-Proxy', 'api-prober')
    if data:
        request.add_data(data)
        request.add_header('Content-Length', str(len(data)))
        request.add_header('Content-Type', 'multipart/form-data;boundary=%s' % BOUNDARY)
    
    # In case the gateway is not responding, we'll retry.
    retry_count = 0
    while retry_count < 5:
        try:
            result = urllib2.urlopen(request).read()
            return result
        except urllib2.HTTPError, e:
            # We see this error if the site goes down. We need to pause and retry.
            err_msg = 'Error accessing %s\n%s' % (url, e)
            logger.error(err_msg)
            logger.info('Pausing %d seconds', 60)
            time.sleep(60)
            retry_count += 1
            if retry_count == 5:
                return err_msg



def GetCookie(cookie_key, cookie_string):
    """Extract the cookie value from a set-cookie string.

    Args:
      cookie_key: string, cookie identifier.
      cookie_string: string, from a set-cookie command.
    Returns:
      string, value of cookie.
    """
    logger.debug('Getting cookie from %s', cookie_string)
    id_string = cookie_key + '='
    cookie_crumbs = cookie_string.split(';')
    for c in cookie_crumbs:
        if id_string in c:
            cookie = c.split(id_string)
            return cookie[1]
    return None



#def ConvertJson(json_str):    
#    """Convert json string to a python object.
#    
#    Args:
#      json_str: string, json response.
#    Returns:
#      dictionary of deserialized json string.
#    """
#    j = {}
#    try:
#        j = json.loads(json_str)
#        j['json'] = True
#    except ValueError, e:
#        # This means the format from json_str is probably bad.
#        logger.error('Error parsing json string %s\n%s', json_str, e)
#        j['json'] = False
#        j['error'] = e
#    
#    return j

def GetKeyValue(line, sep=':'):
    """Return value from a key value pair string.

    Args:
      line: string containing key value pair.
      sep: separator of key and value.
    Returns:
      string: value from key value string.
    """
    s = line.split(sep)
    return StripPunc(s[1])

def StripPunc(s):
    """Strip puncuation from string, except for - sign.
    
    Args:
        s: string.
    Returns:
        string with puncuation removed.
    """
    for c in string.punctuation:
        if c == '-':  # Could be negative number, so don't remove '-'.
            continue
        else:
            s = s.replace(c, '')
    return s.strip()

def Validate(response):
    """Determine if JSON response indicated success."""
    if response.find('"success": true') > 0:
        return True
    else:
        return False

def GetMessage(response):
    """Extract the API message from a Cloud Print API json response.
    
    Args:
        response: json response from API request.
    Returns:
        string: message content in json response.
    """
    lines = response.split('\n')
    for line in lines:
        if '"message":' in line:
            msg = line.split(':')
            return msg[1]
    return None

def ReadFile(pathname):
    """Read contents of a file and return content.
    
    Args:
        pathname: string, (path)name of file.
    Returns:
        string: contents of file.
    """
    try:
        f = open(pathname, 'rb')
        try:
            s = f.read()
        except IOError, e:
            logger('Error reading %s\n%s', pathname, e)
        finally:
            f.close()
            return s
    except IOError, e:
        logger.error('Error opening %s\n%s', pathname, e)
    return None

def WriteFile(file_name, data):
    """Write contents of data to a file_name.
    
    Args:
        file_name: string, (path)name of file.
        data: string, contents to write to file.
    Returns:
        boolean: True = success, False = errors.
    """
    status = True
    
    try:
        f = open(file_name, 'wb')
        try:
            f.write(data)
        except IOError, e:
            logger.error('Error writing %s\n%s', file_name, e)
            status = False
        finally:
            f.close()
    except IOError, e:
        logger.error('Error opening %s\n%s', file_name, e)
        status = False
    
    return status

def Base64Encode(pathname):
    """Convert a file to a base64 encoded file.
    
    Args:
        pathname: path name of file to base64 encode..
    Returns:
        string, name of base64 encoded file.
    For more info on data urls, see:
        http://en.wikipedia.org/wiki/Data_URI_scheme
    """
    b64_pathname = pathname + '.b64'
    file_type = mimetypes.guess_type(pathname)[0] or 'application/octet-stream'
    data = ReadFile(pathname)
    
    # Convert binary data to base64 encoded data.
    header = 'data:%s;base64,' % file_type
    b64data = header + base64.b64encode(data)
    
    if WriteFile(b64_pathname, b64data):
        return b64_pathname
    else:
        return None

def Base64EncodeString(pathname):
    """Convert a file to a base64 encoded file.
    
    Args:
        pathname: path name of file to base64 encode..
    Returns:
        string, name of base64 encoded file.
    For more info on data urls, see:
        http://en.wikipedia.org/wiki/Data_URI_scheme
    """
    file_type = mimetypes.guess_type(pathname)[0] or 'application/octet-stream'
    data = ReadFile(pathname)
    
    # Convert binary data to base64 encoded data.
    header = 'data:%s;base64,' % file_type
    return header + base64.b64encode(data)



def GaiaLogin(email, password):
    """Login to gaia using HTTP post to the gaia login page.

    Args:
      email: string,
      password: string
    Returns:
      dictionary of authentication tokens.
    """
    tokens = {}
    cookie_keys = ['SID', 'LSID', 'HSID', 'SSID']
    email = email.replace('+', '%2B')
    # Needs to be some random string.
    galx_cookie = base64.b64encode('%s%s' % (email, time.time()))

    # Simulate submitting a gaia login form.
    form = ('ltmpl=login&fpui=1&rm=hide&hl=en-US&alwf=true'
            '&continue=https%%3A%%2F%%2F%s%%2F%s'
            '&followup=https%%3A%%2F%%2F%s%%2F%s'
            '&service=%s&Email=%s&Passwd=%s&GALX=%s' % (FOLLOWUP_HOST,
            FOLLOWUP_URI, FOLLOWUP_HOST, FOLLOWUP_URI, SERVICE, email,
            password, galx_cookie))
    login = httplib.HTTPS(GAIA_HOST, 443)
    login.putrequest('POST', LOGIN_URI)
    login.putheader('Host', GAIA_HOST)
    login.putheader('content-type', 'application/x-www-form-urlencoded')
    login.putheader('content-length', str(len(form)))
    login.putheader('Cookie', 'GALX=%s' % galx_cookie)
    logger.debug('Sent POST content: %s', form)
    login.endheaders()
    logger.info('HTTP POST to https://%s%s', GAIA_HOST, LOGIN_URI)
    login.send(form)

    (errcode, errmsg, headers) = login.getreply()
    login_output = login.getfile()
    login_output.close()
    login.close()
    logger.info('Login complete.')

    if errcode != 302:
        logger.error('Gaia HTTP post returned %d, expected 302', errcode)
        logger.error('Message: %s', errmsg)

    for line in str(headers).split('\r\n'):
        if not line: continue
        (name, content) = line.split(':', 1)
        if name.lower() == 'set-cookie':
            for k in cookie_keys:
                if content.strip().startswith(k):
                    tokens[k] = GetCookie(k, content)

    if not tokens:
        logger.error('No cookies received, check post parameters.')
        return None
    else:
        logger.debug('Received the following authorization tokens.')
        for t in tokens:
            logger.debug(t)
        return tokens


def GetAuthTokens(email, password):
    """Assign login credentials from GAIA accounts service.

    Args:
      email: Email address of the Google account to use.
      password: Cleartext password of the email account.
    Returns:
      dictionary containing Auth token.
    """
    # First get GAIA login credentials using our GaiaLogin method.
    tokens = GaiaLogin(email, password)

    # We still need to get the Auth token.    
    params = {'accountType': 'GOOGLE',
              'Email': email,
              'Passwd': password,
              'service': SERVICE,
              'source': CLIENT_NAME}
    stream = urllib.urlopen(LOGIN_URL, urllib.urlencode(params))

    for line in stream:
        if line.strip().startswith('Auth='):
            tokens['Auth'] = line.strip().replace('Auth=', '')
    
    return tokens



def GetPrinters(proxy=None):
    """Get a list of all printers, including name, id, and proxy.
    
    Args:
        proxy: name of proxy to filter by.
    Returns:
        dictionary, keys = printer id, values = printer name, and proxy.
    """
    printers = {}
    values = {}
    _tokens = ['"id"', '"name"', '"proxy"']
    for t in _tokens:
        values[t] = ''
    
    if proxy:
        response = GetUrl('%s/list?proxy=%s' % (CLOUDPRINT_URL, proxy), _tokens)
    else:
        response = GetUrl('%s/search' % CLOUDPRINT_URL, AUTH_TOKENS)
    
    sections = response.split('{')
    for printer in sections:
        lines = printer.split(',')
        for line in lines:
            for t in _tokens:
                if t in line:
                    values[t] = GetKeyValue(line)
        if values['"id"']:
            printers[values['"id"']] = {}
            printers[values['"id"']]['name'] = values['"name"']
            printers[values['"id"']]['proxy'] = values['"proxy"']

    return printers    



def Query(printer, proxy=None):
    """Query for a printer by name.
    
    Args:
      printer: string, name of printer.
      proxy: string, id of proxy to filter by.
    Returns:
      string: the printer_id or None if not found.
    """
    if proxy:
        printers = GetPrinters(proxy=proxy)
        for p in printers:
            if printers[p]['name'] == printer:
                return p
    else:
        printer_id = None
        response = GetUrl('%s/search?q=%s' % (CLOUDPRINT_URL, printer), AUTH_TOKENS)
        sections = response.split('"printers": [')
        lines = sections[1].split(',')
        for line in lines:
            if '"id"' in line:
                printer_id = GetKeyValue(line)
            elif '"name"' in line:
                printer_name = GetKeyValue(line)
                if printer_name == printer:
                    logger.debug('Printer %s is registered', printer)
                    if printer_id:
                        return printer_id
                    else:
                        logger.error('Malformed api response.')
                        return None
    
    return None



#def RegisterAnonPrinter(printer):
#    """Make a Printer Registration call as anonymous user.
#
#    Args:
#        printer: string, name of printer.
#    Returns:
#        dictionary: this will contain a boolean status and a json string.
#    """
#    result = {}
#    data = EncodeMultiPart([('printer', printer),
#                            ('proxy', 'SelfRegProxy')],
#                            [('capabilities', 'capabilities',
#                             Constants.CAPS)])
#    response = GetUrl('%s/register' % CLOUDPRINT_URL, data, anonymous=True)
#
#    return response



#def SelfRegister():
#    """A function to initiate and complete the entire self registration process.
#    
#    Returns:
#      boolean: True = Success, False = errors.
#    """
#    pname = 'SelfRegPrinterName'
#    response = RegisterAnonPrinter(pname)
#    if Validate(response):
#        reg = ConvertJson(response)
#        printer_id = reg['printers'][0]['id']
#        if not reg['json']:
#            logger.error(reg['error'])
#            return False
#        else:
#            poll_url = '%s%s' % (reg['polling_url'], OAUTH)
#            # This is manual step to go and claim your printer.
#            print 'Go claim your printer at this url:'
#            print 'http://www.google.com/cloudprint/claimprinter.html'
#            print 'Use token: %s' % reg['registration_token']
#            raw_input('Press Enter to continue once you\'ve claimed your printer...')
#            res = GetUrl(poll_url, anonymous=True)
#            if Validate(res):
#                poll = ConvertJson(res)
#                if not poll['json']:
#                    logger.error(poll['error'])
#                    return False
#                else:
#                    logger.info('Self Registration Authorization Code: %s',
#                                poll['authorization_code'])
#                    reg_id = Query(pname)
#                    if reg_id == printer_id:
#                        return True
#                    else:
#                        logger.error('Registered id doesn\'t match printer id.')
#                        return False
#            else:  # poll_url wasn't successful.
#                logger.error(GetMessage(res))
#                return False
#    else:  # RegisterAnonPrinter() was not successful.
#        logger.error(GetMessage(response))
#        return False



#def RegisterPrinter(printer, print_cap):
#    """Make a Printer Registration Call.
#    
#    Args:
#        printer: string, name of printer, also used as id and proxy name.
#        print_cap: string, XML formatted string of printer capabilities.
#    Returns:
#        boolean: True = success, False = errors.
#    """
#    edata = EncodeMultiPart([('printer', printer),
#                             ('printerid', printer),
#                             ('proxy', printer)],
#                             [('capabilities', 'capabilities',
#                              print_cap)])
#    response = GetUrl('%s/register' % CLOUDPRINT_URL, tokens, data=edata)
#    return Validate(response)
#
#
#def DeletePrinter(printerid):
#    """Delete the specified printerid from the cloud printer service.
#    
#    Args:
#        printerid: string, unique id registered on back end.
#    Returns:
#        boolean: True = deleted, False = errors.
#    """
#    results = {}
#    msg_tokens = ['"success"', '"message"']
#    response = GetUrl('%s/delete?printerid=%s' % (CLOUDPRINT_URL, printerid), tokens)
#    lines = response.split(',')
#    for line in lines:
#        for t in msg_tokens:
#            if t in line:
#                results[t] = GetKeyValue(line)
#    if results['"success"'] == 'true':
#        logger.debug('Printer id %s removed.', printerid)
#        return True
#    else:
#        logger.info('Error removing printer id %s', printerid)
#        logger.info('%s', results['"message"'])
#        return False
#
#def DeletePrinters(proxy_id=None, wildcard=None):
#    """Delete all printers, filtering by proxy_id or printer name.
#    
#    Args:
#        proxy_id: string, proxy id to filter by.
#        wildcard: string, only delete printers containing this string.
#    Returns:
#        integer: number of errors encountered during entire delete cycle.
#    """
#    errors = 0
#    if proxy_id:
#        printers = GetPrinters(proxy=proxy_id)
#    else:
#        printers = GetPrinters()
#    
#    for p in printers:  # This should be the printer id.
#        if wildcard:
#            if wildcard in printers[p]['name']:
#                status = DeletePrinter(p)
#            else:
#                status = None
#        else:
#            status = DeletePrinter(p)
#        if not status:
#            errors += 1
#    
#    return errors



def GetJobs(printerid=None, jobid=None):
    """Get a list of printer jobs.
    
    Args:
        printerid: if specified, filter by printer id.
        jobid: if specified, filter by job id.
    Returns:
        dictionary of job id's (key) and printer id's (value).
    """
    job_tokens = {'k': '"id"',
                  'v': '"printerid"',
                 }
    values = {}
    jobs = {}
    
    if printerid:
        response = GetUrl('%s/fetch?printerid=%s' % (CLOUDPRINT_URL, printerid), AUTH_TOKENS)
    elif jobid:
        response = GetUrl('%s/fetch?jobid=%s' % (CLOUDPRINT_URL, jobid), AUTH_TOKENS)
    else:
        response = GetUrl('%s/jobs' % CLOUDPRINT_URL, AUTH_TOKENS)
    sections = response.split('{')
    for job in sections:
        lines = job.split(',')
        for line in lines:
            for t in job_tokens:
                if job_tokens[t] in line:
                    values[t] = GetKeyValue(line)
        if values:
            jobs[values['k']] = values['v']
            values = {}
    
    return jobs


def SubmitJob(printerid, jobtype, jobsrc):
    """Submit a job to printerid with content of dataUrl.
    
    Args:
      printerid: string, the printer id to submit the job to.
      jobtype: string, must match the dictionary keys in content and content_type.
      jobsrc: string, points to source for job. Could be a pathname or id string.
    Returns:
      boolean: True = submitted, False = errors.
    """
    if jobtype == 'pdf':
#        b64file = Base64Encode(jobsrc)
#        fdata = ReadFile(b64file)
        fdata = Base64EncodeString(jobsrc)
    elif jobtype in ['png', 'jpeg']:
        fdata = ReadFile(jobsrc)
    else:
        fdata = None
    
    # Make the title unique for each job, since the printer by default will name
    # the print job file the same as the title.
    
    datehour = time.strftime('%b%d%H%M', time.localtime())
    title = '%s%s' % (datehour, jobsrc)
    """The following dictionaries expect a certain kind of data in jobsrc, depending on jobtype:
    jobtype               jobsrc
    ======================================
    pdf                     pathname to the pdf file
    png                    pathname to the png file
    jpeg                   pathname to the jpeg file
    =======================================    
    """
    content = {'pdf': fdata,
               'jpeg': jobsrc,
               'png': jobsrc,
              }
    content_type = {'pdf': 'dataUrl',
                    'jpeg': 'image/jpeg',
                    'png': 'image/png',
                   }
    headers = [('printerid', printerid),
               ('title', title),
               ('content', content[jobtype]),
               ('contentType', content_type[jobtype])]
    files = [('capabilities', 'capabilities', '{"capabilities":[]}')]
    if jobtype in ['pdf', 'jpeg', 'png']:
        files.append(('content', jobsrc, fdata))
        edata = EncodeMultiPart(headers, files, file_type=content_type[jobtype])
    else:
        edata = EncodeMultiPart(headers, files)
    
    response = GetUrl('%s/submit' % CLOUDPRINT_URL, AUTH_TOKENS, data=edata,
                      cookies=False)
    status = Validate(response)
    if not status:
        error_msg = GetMessage(response)
        logger.error('Print job %s failed with %s', jobtype, error_msg)
    
    return status



if __name__ == '__main__':
    
    
    user = raw_input('utente gmail:')
    if user:
        pswd = raw_input('password:')
    if user and pswd:
        
        InitAuthTokens(user, pswd)
                
        printers = GetPrinters()
        
        for p in printers:
            print p, printers[p]
            if 'HPDeskjetF2400series' in printers[p]['name']:
                printerid = p
        
        if printerid:
            jobtype = 'pdf'
            jobsrc = '/home/f4b10x/x4ga-profiles/niris/stampe/Documenti 2011/Fattura/Fattura immediata n. 43 - CLIENTE DI PROVA (20001).pdf'
            SubmitJob(printerid, jobtype, jobsrc)
        else:
            print 'stampante non trovata :('
