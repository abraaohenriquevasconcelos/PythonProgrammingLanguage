

import cookielib, urllib2

cj = cookielib.CookieJar()

'''
build_opener([handler, ...]) -> Return an OpenerDirector instance (The OpenerDirector class opens
URLs via BaseHandler. It manages the chaining of handlers, and recovery from errors), which
chains the handlers in the order given. handlers can be either  instances of BaseHandler, or
subclasses of BaseHandler
'''
#class HTTPCookieProcessor([cookiejar]) -> a class to handle HTTP cookies
opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

var1 = opener.open('https://www.idcourts.us/repository/start.do')
print cj


'''
Links:

1) http://www.portugal-a-programar.pt/forums/topic/66771-resolvido-login-webpage-com-python/
2) http://www.ibm.com/developerworks/br/linux/library/l-python-mechanize-beautiful-soup/
3) https://pythonhelp.wordpress.com/2013/03/21/acessando-conteudo-via-apis-web-baseadas-em-json/
4) https://pythonhelp.wordpress.com/2013/03/21/acessando-conteudo-via-apis-web-baseadas-em-json/
5) https://www.palpitedigital.com/acessar-paginas-via-codigo-python/
6) http://pt.slideshare.net/fmasanori/hackeando-o-facebook-com-python

7) http://stackoverflow.com/questions/13925983/login-to-website-using-urllib2-python-2-7 && https://translate.googleusercontent.com/translate_c?depth=1&hl=pt-BR&prev=search&rurl=translate.google.com.br&sl=en&u=http://stackoverflow.com/questions/13925983/login-to-website-using-urllib2-python-2-7&usg=ALkJrhjfMMFxADMWnv4toipY3UuPpqfyqg

8)http://douglasmiranda.com/artigo/requests-modulo-para-requisicoes-http-em-python/
9) https://pythonhelp.wordpress.com/tag/requests/
10) https://pythonhelp.wordpress.com/2013/03/12/acessando-recursos-na-web-com-python/
11)http://www.nacaolivre.com.br/python/python-usando-urllib2/

12)https://pythonr2.wordpress.com/2008/09/04/navegando-con-python-urllib2/

13) https://translate.googleusercontent.com/translate_c?depth=1&hl=pt-BR&prev=search&rurl=translate.google.com.br&sl=en&u=http://www.python-requests.org/en/latest/user/advanced/&usg=ALkJrhiHZD25pR3ptCo5Scxw1Kh0N3inJw#session-objects

'''
