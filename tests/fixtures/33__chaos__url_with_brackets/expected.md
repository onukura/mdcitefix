# URLs with Brackets Test

This document tests handling of URLs that contain bracket characters.

## URLs Containing Brackets

Some APIs use brackets in URLs for array parameters.
Check the documentation at https://api.example.com/docs[v2]/endpoints.html

Another example: https://example.com/page[1].html
And this one: https://server.com/data[index].json

## Citations vs URLs

Valid citation [1] pointing to a URL.
Not a citation: https://example.com/array[2]/item
Also not a citation: https://site.com/ref[3]

Another valid citation [3] here.

## Reference Definitions with Brackets in URLs

Citation [4] points to URL with brackets.
Citation [5] points to another URL with brackets.

## Inline Links with Brackets

This is an inline link: [documentation](https://docs.example.com/api[v3]/guide.html)
Another inline link: [array syntax](https://learn.example.com/arrays[index])

These inline links should NOT be treated as citations!

## Mixed Context

Visit https://example.com/page[draft] for more info [1].
The endpoint https://api.example.com/users[id]/profile [3] is documented.
Array access like arr[4] should not interfere with citation [4].

## References
<!-- mdcitefix:refs -->
[1]: https://api.example.com/docs[v2]/endpoints.html
[2]: MISSING_URL
[3]: https://server.com/data[index].json
[4]: https://example.com/page[1].html
[5]: https://site.com/ref[special]/content
