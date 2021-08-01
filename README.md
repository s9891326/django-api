

### 第三方登入
- [流程](https://blog.hanklu.tw/post/2020/spa-api-social-loign/)
- [教學2](https://www.section.io/engineering-education/django-google-oauth/)
- [FB developer](https://developers.facebook.com/apps/1001993363887699/settings/basic/)
- [Google developer GCP](https://console.cloud.google.com/apis/credentials/oauthclient/122455133186-drprmpo7inpbpdp8j9fdnodn46hqslct.apps.googleusercontent.com?project=solar-haven-320806)
- [Google Sign-in文件](https://developers.google.com/identity/sign-in/web/sign-in)

### Celery send email
- [Celery](https://tw511.com/a/01/33541.html)

### 遇到的問題
1. 安装cryptography报错：Failed building wheel for cryptography
> - 根據套件安裝錯誤提示先更新pip(`pip install -U pip`)，但無法順利更新。
> - 改用`easy_install -U pip`來進行更新，再重新安裝djoser(`pip install djoser`)