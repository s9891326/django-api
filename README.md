## Heroku部屬
- [參考](https://github.com/s9891326/django-tutorial-for-programmers-uranusjr/blob/1.8/24-deploy-to-heroku.md)
- heroku git:remote -a <your_app_name>
- heroku config:set DISABLE_COLLECTSTATIC=1
- heroku run python manage.py showmigrations  -> 用來確認每個app是否都有正常

## 重新上板步驟
- `git add -u`(把更新的東西都加進來) 
- `git commit -m "message"`
- `heroku login`: 會跳出一個UI介面讓你登入
- `git push heroku master`
- `heroku open`

## JWT Token
- 為登入驗證機制。保存期限為1天，提供token刷新功能。
- 登入成功後要在Header內帶入`Authorization: Bearer <token>`，才能順利完成後續API呼叫

<details>
<summary>api-token-auth/</summary>

- 登入token驗證接口

    | 項目 | 說明 |
    |------|-----|
    | API URL | {server_domain}/api-token-auth/ |
    | method | POST(階層資料) |
    
</details>

- `api-token-auth/`: 登入token驗證接口，需輸入username、password
    - example: `{server_domain}/api-token-auth`
- `api-token-refresh/`: token刷新接口

## 第三方登入
- [流程](https://blog.hanklu.tw/post/2020/spa-api-social-loign/)
- [教學2](https://www.section.io/engineering-education/django-google-oauth/)
- [FB developer](https://developers.facebook.com/apps/1001993363887699/settings/basic/)
- [Google developer GCP](https://console.cloud.google.com/apis/credentials/oauthclient/122455133186-drprmpo7inpbpdp8j9fdnodn46hqslct.apps.googleusercontent.com?project=solar-haven-320806)
- [Google Sign-in文件](https://developers.google.com/identity/sign-in/web/sign-in)

## GIT
- 刪除已存在的檔案
    - $ git rm --cached <file>         # 單一檔案
    - $ git rm -r --cached <folder>    # 指定資料夾下的所有檔案

## Celery send email
- [Celery](https://tw511.com/a/01/33541.html)

## API 說明文件
- [coreapi](https://blog.csdn.net/weixin_42289273/article/details/110273877)
- HTTP Method
> - POST: 新增(/user)
> - GET：讀取全部(/users)
> - GET：讀取部分(/user/1)
> - PUT：修改（修改整份文件）(/user/1)
> - DELETE：刪除(/user/1)

## 欄位定義
### 店家
- 名稱
- 店家類型(日式、西式餐廳)
- 聯絡電話
- 簡介
- 地點(=> google map)
- 評論
- 菜單
- 創建時間(=> 最新店家)
- 創建者

### 評論
- 評價分數
- 評價文字
- 評價者

### 菜單
- 菜單名稱
- 菜單價格
- 菜單內容物說明
- 類型(套餐、主食、小菜...)
- 菜單圖片

### 使用者
- 名字
- 密碼
- 電話
- 信箱 
 
### 訂單事件
- 店家(FK)

### 訂單
- 訂購資訊(FK 使用者)
- 取餐時間
- 取餐地點
- 付款方式
- 付款是否成功
- 餐點狀況(等待店家回應 -> 店家接受 -> 處理中 -> 配送中 -> 完成)

## 功能
### 店家
- CRUD
- 評論功能
- 最新店家
- 心心數最高的店家

### 評論
- CRUD

### 菜單
- CRUD

### 使用者
- 註冊
- 登入

### 訂單事件
- CRUD

### 訂單
- CRUD
- 金流串接
- 更新物流狀態

## 遇到的問題
1. 安装cryptography报错：Failed building wheel for cryptography
> - 根據套件安裝錯誤提示先更新pip(`pip install -U pip`)，但無法順利更新。
> - 改用`easy_install -U pip`來進行更新，再重新安裝djoser(`pip install djoser`)
2. 理解Django aggregate()、annotate()的運用方式 [Ref](https://docs.djangoproject.com/zh-hans/3.2/topics/db/aggregation/)
> - 兩者之間的差異: aggregate()是終端子句、annotate()不是終端子句。
> - annotate()子句的輸出是QuerySet。這個QuerySet可以被其他QuerySet進行操作和修改(filter()、order_by())