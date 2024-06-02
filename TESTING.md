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


## Code validation
### HTML validation
The individual pages have been checked with the W3C validar. All errors could be fixed except for the pages where Sommernode was used. On these pages 11 errors were found that Sommernode causes. It is an external source over which I have no control. To fix these errors in the future it would be possible to find another text editor that does not cause errors.

| page                     | validator                                                                                                                                              | errors | result |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ------ |
| Homepage - index.html    | <details><summary>Homepage - index.html</summary><img src="./docs/readme_images/html-validator/index-html.png"></details>                              | 0      | pass   |
| register.html            | <details><summary>register.html</summary><img src="./docs/readme_images/html-validator/register-html.png"></details>                                   | 0      | pass   |
| login.html               | <details><summary>login.html</summary><img src="./docs/readme_images/html-validator/login-html.png"></details>                                         | 0      | pass   |
| blog_post_create.html    | <details><summary>blog_post_create.html</summary><img src="./docs/readme_images/html-validator/blog-post-create-html.png"></details>                   | 11     | pass   |
|                          | <details><summary>blog_post_create.html-error</summary><img src="./docs/readme_images/html-validator/blog-post-create-html-error.png"></details>       |        |        |
| blog_post_update.html    | <details><summary>blog_post_update.html</summary><img src="./docs/readme_images/html-validator/blog-post-update-html.png"></details>                   | 11     | pass   |
|                          | <details><summary>blog_post_update.html-error</summary><img src="./docs/readme_images/html-validator/blog-post-update-html-error.png"></details>       |        |        |
| blog_post_detail.html    | <details><summary>blog_post_detail.html</summary><img src="./docs/readme_images/html-validator/blog-post-detail-html.png"></details>                   | 0      | pass   |
| blog_post_delete.html    | <details><summary>blog_post_delete.html</summary><img src="./docs/readme_images/html-validator/blog-post-delete-html.png"></details>                   | 0      | pass   |
| user_profile_create.html | <details><summary>user_profile_create.html</summary><img src="./docs/readme_images/html-validator/user-profile-create-html.png"></details>             | 11     | pass   |
|                          | <details><summary>user_profile_create.html-error</summary><img src="./docs/readme_images/html-validator/user-profile-create-html-error.png"></details> |        |        |
| user_profile_update.html | <details><summary>user_profile_update.html</summary><img src="./docs/readme_images/html-validator/user-profile-update-html.png"></details>             | 11     | pass   |
|                          | <details><summary>user_profile_update.html-error</summary><img src="./docs/readme_images/html-validator/user-profile-update-html.png-error"></details> |        |        |
| user_profile_detail.html | <details><summary>user_profile_detail.html</summary><img src="./docs/readme_images/html-validator/user-profile-detail-html.png"></details>             | 0      | pass   |
| user_profile_delete.html | <details><summary>user_profile_delete.html</summary><img src="./docs/readme_images/html-validator/user-profile-delete-html.png"></details>             | 0      | pass   |
| comment_create.html      | <details><summary>comment_create.html</summary><img src="./docs/readme_images/html-validator/comment-create-html.png"></details>                       | 0      | pass   |
| comment_update.html      | <details><summary>comment_update.html</summary><img src="./docs/readme_images/html-validator/comment-update-html.png"></details>                       | 0      | pass   |
| comment_delete.html      | <details><summary>comment_delete.html</summary><img src="./docs/readme_images/html-validator/comment-delete-html.png"></details>                       | 0      | pass   |

### CSS Validator:
The base.cc file was tested using W3C Validator. No errors occurred.
[W3C validator](https://validator.w3.org/) <br>
Here is the test result: [](https://validator.w3.org/)
[W3C validator - test result](docs/readme_images/css-validator/css-validation.png)


### Python Validation
All python files created were tested with the CI Python Linter. The errors detected have been eliminated, so that all files are now error-free.
[CI Python Linter](https://pep8ci.herokuapp.com/)

| page                     | validator                                                                                                                         | errors | result |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------ | ------ |
| account app - admin.py   | <details><summary>account app - admin.py</summary><img src="./docs/readme_images/python-linter/accounts-admin.png"></details>     | 0      | pass   |
| account  app - forms.py  | <details><summary>account  app - forms.py</summary><img src="./docs/readme_images/python-linter/accounts-forms2.png"></details>   | 0      | pass   |
| account  app - models.py | <details><summary>account  app - models.py</summary><img src="./docs/readme_images/python-linter/accounts-models2.png"></details> | 0      | pass   |
| account  app - urls.py   | <details><summary>account  app - urls.py</summary><img src="./docs/readme_images/python-linter/accounts-urls2.png"></details>     | 0      | pass   |
| account  app - view.py   | <details><summary>account  app - view.py</summary><img src="./docs/readme_images/python-linter/accounts-views2.png"></details>    | 0      | pass   |
| blog app -admin.py       | <details><summary>blog app -admin.py</summary><img src="./docs/readme_images/python-linter/blog-admin.png"></details>             | 0      | pass   |
| blog app -forms.py       | <details><summary>blog app -forms.py</summary><img src="./docs/readme_images/python-linter/blog-forms2.png"></details>            | 0      | pass   |
| blog app - models.py     | <details><summary>blog app - models.py</summary><img src="./docs/readme_images/python-linter/blog-models2.png"></details>         | 0      | pass   |
| blog app -urls.py        | <details><summary>blog app -urls.py</summary><img src="./docs/readme_images/python-linter/blog-urls2.png"></details>              | 0      | pass   |
| blog app -view.py        | <details><summary>blog app -view.py</summary><img src="./docs/readme_images/python-linter/blog-views2.png"></details>             | 0      | pass   |
| caveblog - settings.py   | <details><summary>caveblog - settings.py</summary><img src="./docs/readme_images/python-linter/settings2.png"></details>          | 0      | pass   |
| caveblog - urls.py       | <details><summary>caveblog - urls.py</summary><img src="./docs/readme_images/python-linter/urls.png"></details>                   | 0      | pass   |

## Lighthouse Scores

## Lighthouse

Performance, accessibility, best practices and seo were tested using [lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) in Chro