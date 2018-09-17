# Go REST :o: {#s-go-rest}

## REST

Representational State Transfer (REST) is an architectural style that defines a set of constraints to be used for creating web services. Web Services that conform to the REST architectural style, or RESTful web services, provide interoperability between computer systems on the Internet. REST-compliant web services allow the requesting systems to access and manipulate textual representations of web resources by using a uniform and predefined set of stateless operations. Other kinds of web services, such as SOAP web services, expose their own arbitrary sets of operations.

# RESTful architectures and implementations bring the following characteristics/benefits to organizations:

* Ease of integration - RESTful applications can be easily integrated in the web as they use HTTP methods explicitly
* Increased Scalability - RESTful interactions are stateless and caching semantics are built into the protocol). 
* Evolvability - All resources are identified by URIs which provides a simple way to deal with the evolution of a system. 
* Reliability - RESTful systems typically achieve reliability through idempotent operations.
* Security - RESTful systems can achieve security through both the transport layer (SSL) and a variety of message-level mechanisms.
* Transfer XML, JavaScript Object Notation (JSON)











Gorilla is a web toolkit for the Go programming language. Currently these packages are available:

* gorilla/context stores global request variables.
* gorilla/mux is a powerful URL router and dispatcher.
* gorilla/reverse produces reversible regular expressions for regexp-based muxes.
* gorilla/rpc implements RPC over HTTP with codec for JSON-RPC.
* gorilla/schema converts form values to a struct.
* gorilla/securecookie encodes and decodes authenticated and optionally encrypted cookie values.
* gorilla/sessions saves cookie and filesystem sessions and allows custom session backends.
* gorilla/websocket implements the WebSocket protocol defined in RFC 6455.


