Link back to [README.md](/README.md)
  
# Testing

- [Code validation](#code-validation)
    - [HTML validation](#html-validation)
    - [CSS validation](#css-validation)
    - [Python validation](#python-validation)
    - [Lighthouse test](#lighthouse-test)
    - [Wave accessibility evaluation](#wave-accessibility-evaluation)
- [Manual testing](#manual-testing)
    - [User input Validation](#user-input-validation)
    - [Browser compatibility](#browser-compatibility)  
    - [User story testing](#user-story-testing)
    - [Responsiveness test](#responsiveness-test)
    
  - [Bugs](#bugs)
    - [Solved bugs](#solved-bugs)
    - [Known bugs](#known-bugs)
    - [Unknown bugs](#unknown-bugs)

- [Browser compatibility](#browser-compatibility)
   * [Intended appearance on different browsers](#intended-appearance-on-different-browsers)
   * [Intended responsiveness on different browsers](#intended-responsiveness-on-different-browsers)

   - [Django Messages Implementation Testing](#django-messages-implementation-testing)  ???




## CSS Validator:
The base.cc file was tested using W3C Validator. No errors occurred.
[W3C validator](https://validator.w3.org/) <br>
Here is the test result: [](https://validator.w3.org/)
[W3C validator - test result](docs/readme_images/css-validator/css-validation.png)



## Python Validation
All python files created were tested with the CI Python Linter. The errors detected have been eliminated, so that all files are now error-free.
[CI Python Linter](https://pep8ci.herokuapp.com/)

| page                     | validator                                                                                                                       | errors | result |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------ | ------ |
| account app - admin.py   | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/accounts-admin.png"></details>   | 0      | pass   |
| account  app - forms.py  | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/accounts-forms2.png"></details>  | 0      | pass   |
| account  app - models.py | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/accounts-models2.png"></details> | 0      | pass   |
| account  app - urls.py   | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/accounts-urls2.png"></details>   | 0      | pass   |
| account  app - view.py   | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/accounts-views2.png"></details>  | 0      | pass   |
| blog app -admin.py       | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/blog-admin.png"></details>       | 0      | pass   |
| blog app -forms.py       | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/blog-forms2.png"></details>      | 0      | pass   |
| blog app - models.py     | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/blog-models2.png"></details>     | 0      | pass   |
| blog app -urls.py        | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/blog-urls2.png"></details>       | 0      | pass   |
| blog app -view.py        | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/blog-views2.png"></details>      | 0      | pass   |
| caveblog - settings.py   | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/settings2.png"></details>        | 0      | pass   |
| caveblog - urls.py       | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/urls.png"></details>             | 0      | pass   |

## Lighthouse Scores

## Lighthouse

Performance, accessibility, best practices and seo were tested using [lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) in Chro