# Package Manager

# import webbrowser 
# url_list = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# #opens the above list of website in different taps
# for url in url_list:
#     webbrowser.open_new_tab(url)
    
    
# Uninstalling Packages
# pip uninstall packagename

# List of Packages
# To see the installed packages on our machine. We can use pip followed by list.

# pip list

# Reading from URL

#We will see get, status_code, headers, text and json methods in requests module:

import requests 
# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' 

# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)


#Let us read from an API.
# url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1]) 

#  c:/Users/pc/OneDrive/Desktop/python_code/day19/PackageManager.py
# Traceback (most recent call last):
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connection.py", line 196, in _new_conn
#     sock = connection.create_connection(
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
#     raise err
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
#     sock.connect(sa)
# TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connectionpool.py", line 789, in urlopen
#     response = self._make_request(
#                ^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connectionpool.py", line 490, in _make_request
#     raise new_e
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connectionpool.py", line 466, in _make_request
#     self._validate_conn(conn)
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connectionpool.py", line 1095, in _validate_conn
#     conn.connect()
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connection.py", line 615, in connect
#     self.sock = sock = self._new_conn()
#                        ^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connection.py", line 205, in _new_conn
#     raise ConnectTimeoutError(
# urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x000002219A391610>, 'Connection to restcountries.eu timed out. (connect timeout=None)')

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "C:\Users\pc\anaconda3\Lib\site-packages\requests\adapters.py", line 589, in send
#     resp = conn.urlopen(
#            ^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\connectionpool.py", line 843, in urlopen
#     retries = retries.increment(
#               ^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
#     raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='restcountries.eu', port=443): Max retries exceeded with url: /rest/v2/all (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000002219A391610>, 'Connection to restcountries.eu timed out. (connect timeout=None)'))

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "c:\Users\pc\OneDrive\Desktop\python_code\day19\PackageManager.py", line 40, in <module>
#     response = requests.get(url)  # opening a network and fetching a data      
#                ^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\requests\api.py", line 73, in get
#     return request("get", url, params=params, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\requests\api.py", line 59, in request
#     return session.request(method=method, url=url, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\requests\sessions.py", line 589, in request
#     resp = self.send(prep, **send_kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\requests\sessions.py", line 703, in send
#     r = adapter.send(request, **kwargs)
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pc\anaconda3\Lib\site-packages\requests\adapters.py", line 610, in send
#     raise ConnectTimeout(e, request=request)
# requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='restcountries.eu', port=443): Max retries exceeded with url: /rest/v2/all (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000002219A391610>, 'Connection to restcountries.eu timed out. (connect timeout=None)'))
# PS C:\Users\pc\OneDrive\Desktop\python_code> 


#Creating a Package

