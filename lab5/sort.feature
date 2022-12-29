Feature: sorting

  Scenario: sorting without lambda
    Given data: [4, -30, 100, -100, 123, 1, 0, -1, -4]
    When running sort_without_lambda function
    Then the result is sorted data: [123, 100, -100, -30, 4, -4, 1, -1, 0]

  Scenario: sorting with lambda
    Given data: [4, -30, 100, -100, 123, 1, 0, -1, -4]
    When running sort_with_lambda function
    Then the result is sorted data: [123, 100, -100, -30, 4, -4, 1, -1, 0]

