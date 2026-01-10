# URL Edge Cases

Very long URL [1] and data URL [2].

International domain [3] and localhost [4].

Port numbers [5] and [6] should be different.

IP addresses [7] and [8].

Case sensitivity [9] and [10] should merge.

Trailing slash variations [11], [12], [13].

[1]: https://example.com/very/long/path/that/goes/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on/and/on?param1=value1&param2=value2&param3=value3&param4=value4&param5=value5
[2]: data:text/html,<h1>Hello</h1>
[3]: https://例え.jp/path
[4]: http://localhost:3000/api
[5]: https://example.com:443/path
[6]: https://example.com:8080/path
[7]: https://192.168.1.1/admin
[8]: https://192.168.1.1:8080/admin
[9]: https://EXAMPLE.COM/PATH
[10]: https://example.com/PATH
[11]: https://example.com/path
[12]: https://example.com/path/
[13]: https://example.com/path//
