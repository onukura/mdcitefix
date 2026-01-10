# Circular References

Paper A cites Paper B [1] which cites Paper C [2] which cites Paper A [3].

Self-referential citation [4] references itself.

Chain: [5] -> [6] -> [7] -> [5]
<!-- mdcitefix:refs -->
[1]: https://paper-a.example.com
[2]: https://paper-b.example.com
[3]: https://paper-c.example.com "This cites Paper A"
[4]: https://self.example.com "Self-referential"
[5]: https://chain-start.example.com
[6]: https://chain-middle.example.com
[7]: https://chain-end.example.com
