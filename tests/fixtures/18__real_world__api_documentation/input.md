# REST API Reference

Complete API documentation for the User Management System.

## Overview

This API follows REST principles [1] and uses JSON for data exchange [2].
Authentication uses OAuth 2.0 [3] with bearer tokens.

All endpoints return standard HTTP status codes [1]:
- 200 OK for successful requests [4]
- 201 Created for successful resource creation [5]
- 400 Bad Request for invalid input [6]
- 401 Unauthorized for authentication failures [7]
- 404 Not Found for missing resources [8]
- 500 Internal Server Error for server errors [9]

## Authentication

The API requires authentication for all endpoints except the health check [3].
Use bearer token authentication [3] in the Authorization header.

Token format follows the OAuth 2.0 specification [3]. Tokens expire after 1 hour
and can be refreshed using the refresh token endpoint [10].

## User Endpoints

### List Users

GET /api/v1/users returns all users [4]. Supports pagination using query parameters [11].
Results are returned as JSON [2] following the JSON API specification [12].

### Get User

GET /api/v1/users/{id} retrieves a single user [4]. Returns 404 if not found [8].
Response includes all user fields as defined in the schema [12].

### Create User

POST /api/v1/users creates a new user [5]. Requires admin privileges [3].
The request body must be valid JSON [2] matching the user schema [12].

Returns 400 for validation errors [6] with details in RFC 7807 format [13].

### Update User

PUT /api/v1/users/{id} updates a user [4]. Requires ownership or admin [3].
Uses standard PUT semantics per HTTP specification [1].

Partial updates are not supported. Use PATCH for partial updates [14].

### Delete User

DELETE /api/v1/users/{id} removes a user [15]. Returns 204 on success [15].
Requires admin authentication [3]. Deletion is permanent and cannot be undone.

## Product Endpoints

### List Products

GET /api/v1/products returns products [4] with pagination [11].
Supports filtering by category using query parameters [11].

### Get Product

GET /api/v1/products/{id} retrieves product details [4].
Returns 404 for non-existent products [8].

### Create Product

POST /api/v1/products adds a product [5]. Requires seller privileges [3].
Product data must validate against the product schema [12].

### Update Product

PUT /api/v1/products/{id} modifies a product [4].
Only the product owner can update [3].

### Delete Product

DELETE /api/v1/products/{id} removes a product [15].
Admin or owner only [3].

## Order Endpoints

### List Orders

GET /api/v1/orders shows user orders [4]. Authentication required [3].
Returns only orders belonging to the authenticated user.

### Create Order

POST /api/v1/orders places an order [5]. Validates inventory availability.
Returns 400 if products are unavailable [6].

### Get Order

GET /api/v1/orders/{id} retrieves order details [4].
Users can only access their own orders [3].

### Cancel Order

DELETE /api/v1/orders/{id} cancels an order [15].
Only possible before shipping. Returns 400 if already shipped [6].

## Error Handling

All errors follow RFC 7807 problem details format [13].
Error responses include type, title, status, and detail fields [13].

Common errors:
- Invalid JSON returns 400 [6] with parse error details [13]
- Missing authentication returns 401 [7] with auth error [13]
- Insufficient permissions return 403 [16] with permission error [13]
- Resource not found returns 404 [8] with not found error [13]
- Server errors return 500 [9] with generic error message [13]

## Rate Limiting

API calls are limited to 1000 requests per hour per API key [17].
Rate limit information is included in response headers [17].

Exceeding limits returns 429 Too Many Requests [18] with retry information [17].
The Retry-After header indicates when to retry [18].

## Caching

Responses include Cache-Control headers per HTTP caching spec [19].
GET requests support conditional requests using ETags [19].

Use If-None-Match header to check for updates [19].
Returns 304 Not Modified if content unchanged [20].

## CORS

Cross-origin requests are supported via CORS [21].
Allowed origins are configurable per deployment [21].

Preflight requests use OPTIONS method [22].
CORS headers follow the W3C specification [21].

## Versioning

API version is included in the URL path [1].
Current version is v1. Future versions will be v2, v3, etc.

Version migration guides will be provided when new versions are released.
Old versions are supported for 12 months after deprecation [1].

## Response Format

All responses are JSON [2] following REST conventions [1].
Collections include total count and pagination links [11].

Success responses [4,5,15] include the requested data.
Error responses [6,7,8,9,13,16,18] include problem details [13].

## Additional Resources

Complete API specification available as OpenAPI 3.0 document [23].
Interactive API explorer available at /api/docs [23].
SDK libraries available for Python, JavaScript, and Go [24].

## Standards Compliance

This API complies with:
- REST architectural style [1]
- HTTP/1.1 specification [1]
- JSON data format [2]
- OAuth 2.0 authentication [3]
- RFC 7807 problem details [13]
- OpenAPI 3.0 specification [23]

[1]: https://datatracker.ietf.org/doc/html/rfc7231 "HTTP Semantics"
[2]: https://datatracker.ietf.org/doc/html/rfc8259 "JSON Data Format"
[3]: https://datatracker.ietf.org/doc/html/rfc6749 "OAuth 2.0"
[4]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.1 "200 OK"
[5]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.2 "201 Created"
[6]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.1 "400 Bad Request"
[7]: https://datatracker.ietf.org/doc/html/rfc7235#section-3.1 "401 Unauthorized"
[8]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.4 "404 Not Found"
[9]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.1 "500 Internal Server Error"
[10]: https://datatracker.ietf.org/doc/html/rfc6749#section-6 "Token Refresh"
[11]: https://datatracker.ietf.org/doc/html/rfc5988 "Web Linking (Pagination)"
[12]: https://jsonapi.org/format/ "JSON API Specification"
[13]: https://datatracker.ietf.org/doc/html/rfc7807 "Problem Details"
[14]: https://datatracker.ietf.org/doc/html/rfc5789 "PATCH Method"
[15]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.5 "204 No Content"
[16]: https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.3 "403 Forbidden"
[17]: https://datatracker.ietf.org/doc/html/rfc6585 "Additional HTTP Status Codes"
[18]: https://datatracker.ietf.org/doc/html/rfc6585#section-4 "429 Too Many Requests"
[19]: https://datatracker.ietf.org/doc/html/rfc7234 "HTTP Caching"
[20]: https://datatracker.ietf.org/doc/html/rfc7232#section-4.1 "304 Not Modified"
[21]: https://www.w3.org/TR/cors/ "CORS Specification"
[22]: https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.7 "OPTIONS Method"
[23]: https://spec.openapis.org/oas/v3.0.0 "OpenAPI Specification"
[24]: https://github.com/example/api-sdks "API Client SDKs"
