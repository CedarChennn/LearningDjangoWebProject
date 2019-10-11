# LearningDjangoWebProject
https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial03/
# 基本操作

```python
 python -m django --version

 django-admin startproject mysite

 python manage.py runserver

  python manage.py startapp polls
```

# Bootstrap 
## 网格系统（Grid System）
 基本结构
```html
<div class="container">
   <div class="row">
      <div class="col-*-*"></div>  <!-- 内容应该放置在列内，且唯有列可以是行的直接子元素。 -->
      <div class="col-*-*"></div>      
   </div>
   <div class="row">...</div>
</div>
<div class="container">....
```
.col-xs-4表示列的宽度为4.总宽度为12，故一行排三个;

|        |	超小设备手机（<768px）| 小型设备平板电脑（≥768px）  | 中型设备台式电脑（≥992px）  | 大型设备台式电脑（≥1200px） |
|  ----  | ----  |----  |----  |----  |
|Class 前缀  | .col-xs- |.col-sm- | .col-md- | .col-lg-|



您可以很轻易地改变带有 .col-md-push-* 和 .col-md-pull-* 类的内置网格列的顺序，其中 * 范围是从 1 到 11,可以很容易地以一种顺序编写列，然后以另一种顺序显示列。

## 排版