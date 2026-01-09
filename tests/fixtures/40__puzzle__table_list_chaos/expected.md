# Table and List Chaos

This tests citations in tables and complex list structures.

## Citations in Tables

| Study | Year | Citation |
|-------|------|----------|
| Smith | 2020 | [1] |
| Jones | 2021 | [2] |
| Davis | 2022 | [3, 4] |
| Chen  | 2023 | [5, 6, 7] |

| Method | Results | Reference |
|--------|---------|-----------|
| A | Positive [8] | [1, 8] |
| B | Negative [9] | [2, 9] |
| C | Mixed [10] | [3, 4, 10] |

## Citations in Nested Lists

- Level 1 [1]
  - Level 2 [2]
    - Level 3 [3]
      - Level 4 [4]
        - Level 5 [5]
          - Level 6 [6]
  - Back to Level 2 [2]
- Back to Level 1 [1, 2, 3]

1. First [7]
   1. Sub-first [8]
      1. Sub-sub-first [9]
   2. Sub-second [10]
2. Second [7, 8, 9, 10]

## Task Lists with Citations

- [x] Completed task [11]
- [ ] Pending task [12]
- [x] Another completed [13]
  - [ ] Sub-task [14]
  - [x] Completed sub-task [15]

## Mixed Bullet and Numbered Lists

- Bullet [16]
  1. Number [17]
     - Bullet [18]
        1. Number [19]
           - Bullet [20]

## List with Table

- Item 1 [21]
- Item 2 with table:

  | Col1 | Col2 |
  |------|------|
  | [22] | [23] |
  | [24] | [25] |

- Item 3 [26]

## Table with Lists

| Feature | Details |
|---------|---------|
| Citations | - First [27]<br>- Second [28]<br>- Third [29] |
| Methods | 1. Method A [30]<br>2. Method B [31] |

## Complex Nested Structure

1. Outer [1]
   - Inner bullet [2]
     1. Inner number [3]
        - Deep bullet [4]
          - [ ] Task [5]
          - [x] Done [6]
        - Back [7]
     2. Inner number 2 [8]
   - Inner bullet 2 [9]
2. Outer 2 [10, 11, 12]

All citations: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31].

## References
<!-- mdcitefix:refs -->
[1]: https://example.com/study-smith
[2]: https://example.com/study-jones
[3]: https://example.com/study-davis-1
[4]: https://example.com/study-davis-2
[5]: https://example.com/study-chen-1
[6]: https://example.com/study-chen-2
[7]: https://example.com/study-chen-3
[8]: https://example.com/method-a-results
[9]: https://example.com/method-b-results
[10]: https://example.com/method-c-results
[11]: https://example.com/task-completed
[12]: https://example.com/task-pending
[13]: https://example.com/task-another
[14]: https://example.com/subtask-1
[15]: https://example.com/subtask-completed
[16]: https://example.com/mixed-bullet-1
[17]: https://example.com/mixed-number-1
[18]: https://example.com/mixed-bullet-2
[19]: https://example.com/mixed-number-2
[20]: https://example.com/mixed-bullet-3
[21]: https://example.com/list-item-1
[22]: https://example.com/table-cell-1
[23]: https://example.com/table-cell-2
[24]: https://example.com/table-cell-3
[25]: https://example.com/table-cell-4
[26]: https://example.com/list-item-3
[27]: https://example.com/feature-1
[28]: https://example.com/feature-2
[29]: https://example.com/feature-3
[30]: https://example.com/method-1
[31]: https://example.com/method-2
