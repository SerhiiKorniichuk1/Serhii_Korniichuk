Feature: Basic Functionality of https://www.epam.com

  Scenario: Search
    Given we have the https://www.epam.com/search page opened
    When we type the search query into the search box
    And we press the Find button
    Then the search results are displayed

  Scenario: Localization
    Given we have the main page opened
    When we press the language switch button
    And we choose a language
    Then the website content is displayed in a chosen language

 Scenario: EPAM domain is working
    Given we have browser installed
    When we go to "https://www.epam.com/"
    Then EPAM load site for us

  Scenario: Contact Us
    Given we have the https://www.epam.com/about/who-we-are/contact page opened
    When we fill out a form
    And we press the Submit button
    Then the inquiry is submitted to the appropriate team

  Scenario: Social Networks
    Given we have the main page opened
    When we press the social network buttons
    Then the appropriate social network website opens

  Scenario: Careers
    Given we have the https://www.epam.com/careers page opened
    When we fill in the filter values
    And we press the Find button
    Then the resulting job openings are displayed

  Scenario: Image Carousel
    Given we have the https://www.epam.com/insights page opened
    When we drag the images
    Then the image is scrolled
    And the next image is displayed

  Scenario: Admin page is not accessible
    Given we are not admin
    When we go to "https://www.epam.com/admin"
    Then site will show that page not found