Feature: field

  Scenario: one argument
    Given data: "goods" and argument: "title"
    When running field function with one argument
    Then the result is: "Ковер", "Диван для отдыха"

  Scenario: many arguments
    Given data: "goods" and argument: "title", "price"
    When running field function with many arguments
    Then the result is: {"title": "Ковер", "price": 2000}, {"title": "Диван для отдыха", "price": 5300}