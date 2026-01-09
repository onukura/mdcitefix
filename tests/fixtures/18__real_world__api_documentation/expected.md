# REST API Reference

Complete API documentation for the User Management System.

## Overview

This API follows REST principles [1] and uses JSON for data exchange [2].
Authentication uses OAuth 2.0 [3] with bearer tokens.

All endpoints return standard HTTP status codes [1]:
- 200 OK for successful requests [1]
- 201 Created for successful resource creation [1]
- 400 Bad Request for invalid input [1]
- 401 Unauthorized for authentication failures [4]
- 404 Not Found for missing resources [1]
- 500 Internal Server Error for server errors [1]

## Authentication

The API requires authentication for all endpoints except the health check [3].
Use bearer token authentication [3] in the Authorization header.

Token format follows the OAuth 2.0 specification [3]. Tokens expire after 1 hour
and can be refreshed using the refresh token endpoint [3].

## User Endpoints

### List Users

GET /api/v1/users returns all users [1]. Supports pagination using query parameters [5].
Results are returned as JSON [2] following the JSON API specification [6].

### Get User

GET /api/v1/users/{id} retrieves a single user [1]. Returns 404 if not found [1].
Response includes all user fields as defined in the schema [6].

### Create User

POST /api/v1/users creates a new user [1]. Requires admin privileges [3].
The request body must be valid JSON [2] matching the user schema [6].

Returns 400 for validation errors [1] with details in RFC 7807 format [7].

### Update User

PUT /api/v1/users/{id} updates a user [1]. Requires ownership or admin [3].
Uses standard PUT semantics per HTTP specification [1].

Partial updates are not supported. Use PATCH for partial updates [8].

### Delete User

DELETE /api/v1/users/{id} removes a user [1]. Returns 204 on success [1].
Requires admin authentication [3]. Deletion is permanent and cannot be undone.

## Product Endpoints

### List Products

GET /api/v1/products returns products [1] with pagination [5].
Supports filtering by category using query parameters [5].

### Get Product

GET /api/v1/products/{id} retrieves product details [1].
Returns 404 for non-existent products [1].

### Create Product

POST /api/v1/products adds a product [1]. Requires seller privileges [3].
Product data must validate against the product schema [6].

### Update Product

PUT /api/v1/products/{id} modifies a product [1].
Only the product owner can update [3].

### Delete Product

DELETE /api/v1/products/{id} removes a product [1].
Admin or owner only [3].

## Order Endpoints

### List Orders

GET /api/v1/orders shows user orders [1]. Authentication required [3].
Returns only orders belonging to the authenticated user.

### Create Order

POST /api/v1/orders places an order [1]. Validates inventory availability.
Returns 400 if products are unavailable [1].

### Get Order

GET /api/v1/orders/{id} retrieves order details [1].
Users can only access their own orders [3].

### Cancel Order

DELETE /api/v1/orders/{id} cancels an order [1].
Only possible before shipping. Returns 400 if already shipped [1].

## Error Handling

All errors follow RFC 7807 problem details format [7].
Error responses include type, title, status, and detail fields [7].

Common errors:
- Invalid JSON returns 400 [1] with parse error details [7]
- Missing authentication returns 401 [4] with auth error [7]
- Insufficient permissions return 403 [1] with permission error [7]
- Resource not found returns 404 [1] with not found error [7]
- Server errors return 500 [1] with generic error message [7]

## Rate Limiting

API calls are limited to 1000 requests per hour per API key [9].
Rate limit information is included in response headers [9].

Exceeding limits returns 429 Too Many Requests [9] with retry information [9].
The Retry-After header indicates when to retry [9].

## Caching

Responses include Cache-Control headers per HTTP caching spec [10].
GET requests support conditional requests using ETags [10].

Use If-None-Match header to check for updates [10].
Returns 304 Not Modified if content unchanged [11].

## CORS

Cross-origin requests are supported via CORS [12].
Allowed origins are configurable per deployment [12].

Preflight requests use OPTIONS method [1].
CORS headers follow the W3C specification [12].

## Versioning

API version is included in the URL path [1].
Current version is v1. Future versions will be v2, v3, etc.

Version migration guides will be provided when new versions are released.
Old versions are supported for 12 months after deprecation [1].

## Response Format

All responses are JSON [2] following REST conventions [1].
Collections include total count and pagination links [5].

Success responses [1] include the requested data.
Error responses [1, 4, 7, 9] include problem details [7].

## Additional Resources

Complete API specification available as OpenAPI 3.0 document [13].
Interactive API explorer available at /api/docs [13].
SDK libraries available for Python, JavaScript, and Go [14].

## Standards Compliance

This API complies with:
- REST architectural style [1]
- HTTP/1.1 specification [1]
- JSON data format [2]
- OAuth 2.0 authentication [3]
- RFC 7807 problem details [7]
- OpenAPI 3.0 specification [13]
<!-- mdcitefix:refs -->
[1]: https://datatracker.ietf.org/doc/html/rfc7231 "HTTP Semantics"
[2]: https://datatracker.ietf.org/doc/html/rfc8259 "JSON Data Format"
[3]: https://datatracker.ietf.org/doc/html/rfc6749 "OAuth 2.0"
[4]: https://datatracker.ietf.org/doc/html/rfc7235#section-3.1 "401 Unauthorized"
[5]: https://datatracker.ietf.org/doc/html/rfc5988 "Web Linking (Pagination)"
[6]: https://jsonapi.org/format/ "JSON API Specification"
[7]: https://datatracker.ietf.org/doc/html/rfc7807 "Problem Details"
[8]: https://datatracker.ietf.org/doc/html/rfc5789 "PATCH Method"
[9]: https://datatracker.ietf.org/doc/html/rfc6585 "Additional HTTP Status Codes"
[10]: https://datatracker.ietf.org/doc/html/rfc7234 "HTTP Caching"
[11]: https://datatracker.ietf.org/doc/html/rfc7232#section-4.1 "304 Not Modified"
[12]: https://www.w3.org/TR/cors/ "CORS Specification"
[13]: https://spec.openapis.org/oas/v3.0.0 "OpenAPI Specification"
[14]: https://github.com/example/api-sdks "API Client SDKs"
