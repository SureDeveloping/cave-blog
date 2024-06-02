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


### Lighthouse test
Performance, accessibility, best practices and seo were tested using [lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) <br>
Overall, good values were achieved in the lighthouse test. However, it can be seen that the performance of the pages where Summernode was used is significantly worse than the pages without Summernode. On the pages with Summernode the value is between 68 and 71, on the other pages the worst value is 88. For this reason it is worth testing a different text editor in the future. <br>
With a blog, I don't have much influence on the content and therefore on the SEO value. The worst value is 83, which is still good, but it is difficult to improve it if you have little influence on the content. 
The values for accessibility and best practices are all in the very good range. 


| page                     | performance | accessibility | best practices | seo | screenshot                                                                                                                             | result |
| ------------------------ | ----------- | ------------- | -------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Homepage - index.html    | 90          | 97            | 96             | 92  | <details><summary>Homepage - index.html</summary><img src="./docs/readme_images/lighthouse/index-html.png"></details>                  | pass   |
| register.html            | 96          | 95            | 96             | 92  | <details><summary>register.html</summary><img src="./docs/readme_images/lighthouse/register-html.png"></details>                       | pass   |
| login.html               | 94          | 94            | 96             | 92  | <details><summary>login.html</summary><img src="./docs/readme_images/lighthouse/login-html.png"></details>                             | pass   |
| blog_post_create.html    | 70          | 94            | 96             | 83  | <details><summary>blog_post_create.html</summary><img src="./docs/readme_images/lighthouse/blog-post-create-html.png"></details>       | pass   |
| blog_post_update.html    | 71          | 94            | 96             | 83  | <details><summary>blog_post_update.html</summary><img src="./docs/readme_images/lighthouse/blog-post-update-html.png"></details>       | pass   |
| blog_post_detail.html    | 88          | 100           | 96             | 83  | <details><summary>blog_post_detail.html</summary><img src="./docs/readme_images/lighthouse/blog-post-detail-html.png"></details>       | pass   |
| blog_post_delete.html    | 97          | 100           | 96             | 83  | <details><summary>blog_post_delete.html</summary><img src="./docs/readme_images/v/blog-post-delete-html.png"></details>                | pass   |
| user_profile_create.html | 68          | 94            | 96             | 83  | <details><summary>user_profile_create.html</summary><img src="./docs/readme_images/lighthouse/user-profile-create-html.png"></details> | pass   |
| user_profile_update.html | 69          | 94            | 96             | 83  | <details><summary>user_profile_update.html</summary><img src="./docs/readme_images/lighthouse/user-profile-update-html.png"></details> | pass   |
| user_profile_detail.html | 95          | 97            | 96             | 83  | <details><summary>user_profile_detail.html</summary><img src="./docs/readme_images/lighthouse/user-profile-detail-html.png"></details> | pass   |
| user_profile_delete.html | 94          | 100           | 96             | 83  | <details><summary>user_profile_delete.html</summary><img src="./docs/readme_images/lighthouse/user-profile-delete-html.png"></details> | pass   |
| comment_create.html      | 95          | 100           | 96             | 83  | <details><summary>comment_create.html</summary><img src="./docs/readme_images/lighthouse/comment-create-html.png"></details>           | pass   |
| comment_update.html      | 96          | 100           | 96             | 83  | <details><summary>comment_update.html</summary><img src="./docs/readme_images/lighthouse/comment-update-html.png"></details>           | pass   |
| comment_delete.html      | 88          | 100           | 96             | 83  | <details><summary>comment_delete.html</summary><img src="./docs/readme_images/lighthouse/comment-delete-html.png"></details>           | pass   |


### Wave accessibility evaluation
WAVE® is a test to ensure that web content is more accessible to individuals with disabilities.
The website passes the test, no errors appear. [Link to Wave](https://wave.webaim.org/) <br>

Here is the test result:
[Wave - test result](docs/readme_images/wave/wave-test.png)


## Manual testing
### User input Validation

#### Forms
The formulas on the website have been tested to ensure that they work properly. Function of forwarding and notifications.

| Feature               | Action               | Expected Outcome                                                                                                                                                 | Screenshots                                                                                                               | result |
| --------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------ |
| Registration Form     | Submit form          |   User receives confirmation message and is redirected to the login page.Warnings are issued accordingly for unauthorized entries.                               | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/register1.png"></details>           | pass   |
|                       |                      |                                                                                                                                                                  | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/register2.png"></details>           |        |
|                       |                      |                                                                                                                                                                  | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/register3.png"></details>           |        |
| Login Form            | Login with user data | User can log in and is redirected to the homepage. Warnings are issued accordingly for unauthorized entries.                                                     | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/login1.png"></details>              | pass   |
|                       |                      |                                                                                                                                                                  | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/login2.png"></details>              |        |
| Create Blog Post Form | Create post          | User can create a Blog Post and re redirected to the deatil view of the post. Warnings are issued accordingly for empty field                                    | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/create-blog-post1.png"></details>   | pass   |
| Update Blog Post Form | Update post          | User can update a Blog Post and is redirected to the deatil view of the post. Warnings are issued accordingly for empty field                                    | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/update-blog-post1.png"></details>   | pass   |
| Create Comment Form   | Create comment       | User can create a comment and is redirected to the deatil view of the post. Warnings are issued accordingly for empty field                                      | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/update-blog-post1.png"></details>   | pass   |
| Update Comment Form   | Update comment       | User can update a comment and is redirected to the deatil view of the post. Warnings are issued accordingly for empty field                                      | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/update-comment1.png"></details>     | pass   |
| Create Userprofile    | Create userprofile   | User can create a userprofile and is redirected to the deatil view of the profile. Warnings are issued if the about me field is empty. The rest are not required | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/create-userprofile1.png"></details> | pass   |
| Update Userprofile    | Update userprofile   | User can update a userprofile and is redirected to the deatil view of the profile. Warnings are issued if the about me field is empty. The rest are not required | <details><summary>Registration Form</summary><img src="./docs/readme_images/form-test/update-userprofile1.png"></details> | pass   |

#### Buttons and links

