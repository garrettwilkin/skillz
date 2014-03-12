"""urltools.py - parse and format web URLs.
 
HINT:
 
>>> "http://google.com".split("://")
["http", "google"]
 
>>> "google.com/hangout/parsely.com/am".split("/")
["google.com", "hangout", "parsely.com", "am"]
 
>>> ["google.com/hangout/parsely.com/am".split("/", 1)
['google.com', 'hangout/parsely.com/am']
 
This is basically all you need to implement the parser.
 
For formatting / rejoining:
 
>>> "{host}/{path}".format(host="google.com", path="plus")
"google.com/plus"
 
You can do the whole thing without a single import!
"""
 
 
def url_parse(url):
    """Takes a string URL and returns a dictionary of its various parts."""
    result = {}
    one = url.split("://")
    result["scheme"] = one[0]+"://"
    two = one[1].split("/",1)
    fragment_index = one[1].find("#")
    result["fragment"] = None
    if fragment_index > 0:
        result["fragment"] = one[1][fragment_index:]
    query_index = one[1].find("?")
    result["query"] = None
    if query_index > 0:
        if fragment_index > 0:
            result["query"] = one[1][query_index:fragment_index]
        else:
            result["query"] = one[1][query_index:]
    path_start = one[1].find("/")
    path_end = -1
    if query_index > path_end:
        path_end = query_index
    elif fragment_index > path_end:
        path_end = fragment_index
    else:
        path_end = len(one[1])
    result["port"] = 80
    port_start = one[1].find(":")
    if port_start > -1:
      port_end = one[1].find("/")
      result["port"] = one[1][port_start:port_end]
    result["host"] = two[0]
    result["path"] = one[1][path_start:path_end]
    print result
    return result
 
 
def url_join(parsed_url):
    """Takes a dictionary of URL parts and returns a valid URL."""
    port = ""
    if parsed_url["port"] != 80 and parsed_url["port"] != 443:
        port = ":{}".format(parsed_url["port"])
    result = "{}{}{}{}{}{}".format(parsed_url["scheme"],parsed_url["host"],port,parsed_url["path"],parsed_url["query"],parsed_url["fragment"])
    print result
    return result
 
 
def test_basic_url():
  url = "http://www.linkedin.com/in/andrewmontalenti"
  parsed_url = url_parse(url)
  assert parsed_url["scheme"] == "http://"
  assert parsed_url["host"] == "www.linkedin.com"
  assert parsed_url["path"] == "/in/andrewmontalenti"
  assert parsed_url["port"] == 80
  assert parsed_url["fragment"] is None
  assert parsed_url["query"] is None
 
  
def test_advanced_url():
  url = "http://www.linkedin.com/profile/view?id=13836198&trk=ppro_viewmore#more-123"
  parsed_url = url_parse(url)
  assert parsed_url["fragment"] == "#more-123"
  assert parsed_url["query"] == "?id=13836198&trk=ppro_viewmore"
 
 
def test_joining_url():
  url_parts = {
    "scheme": "http://",
    "host": "www.linkedin.com",
    "path": "/profile/view",
    "fragment": "#more-123",
    "query": "?id=13836198&trk=ppro_viewmore",
    "port": 80
  }
  url = "http://www.linkedin.com/profile/view?id=13836198&trk=ppro_viewmore#more-123"
  assert url_join(url_parts) == url
  url_parts["port"] = 8080
  url = "http://www.linkedin.com:8080/profile/view?id=13836198&trk=ppro_viewmore#more-123"
  assert url_join(url_parts) == url
  url_parts["scheme"] = "https://"
  url_parts["port"] = 443
  url = "https://www.linkedin.com/profile/view?id=13836198&trk=ppro_viewmore#more-123"
  assert url_join(url_parts) == url
  
  
def main():
  test_basic_url()
  test_advanced_url()
  test_joining_url()
  
 
if __name__ == "__main__":
  main()
