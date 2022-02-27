<h1> ShortURL service </h1>
<h2>Daher Daher</h2>

<h3>Description</h3>
* Implemented in Python using Flask Framework

* short_url_service.py -> containing encode/decode APIs
* short_url_utils.py -> contains utilities for generating shortURL string
* memore_store.py -> wrapper for in memory store
  * note that this was implemented using a regular python hash dictionary
  * would have replaced it with Redis. 
  * this src file contains wrapper for in-memory-store so it makes it easier to replace with different DB implementations
* test/api_test.py -> API tests
  * 1x encode (POST) API test
  * 1x decode (GET) API test
  * 1x mixed test
  * with more time I would have created a stress test

<h3>Running</h3>
* Service: python short_url_service.py
  * 2 endpoints: /encode (POST) and /decode (GET)
  * You can now send HTTP requests
    * for example using "curl"
      * curl -X POST -H "Content-Type: application/json" -d '{"url": "www.daher.com"}' http://localhost:5000/encode
        then
      * curl http://localhost:5000/decode?short_url=http://shrt.url/0
      
      response: {"original_url":"www.daher.com"}

* You can also run the test in test/ directory (it runs the service so no need for manual service running before)
  * cd tests
  * pytest -rP api_test.py
