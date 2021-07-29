


### 遇到的問題
1. 安装cryptography报错：Failed building wheel for cryptography
> - 根據套件安裝錯誤提示先更新pip(`pip install -U pip`)，但無法順利更新。
> - 改用`easy_install -U pip`來進行更新，再重新安裝djoser(`pip install djoser`)