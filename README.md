# LearningDjangoWebProject
https://docs.djangoproject.com/zh-hans/2.2/intro/whatsnext/
# 基本操作

```python
 python -m django --version

 django-admin startproject project_nams

 python manage.py runserver
 python manage.py runserver 192.168.1.50:8080
 python manage.py startapp App_name

 python manage.py createsuperuser
 # 助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作
 python manage.py check 

 # 进入交互式 Python 命令行，尝试一下 Django 为你创建的各种 API
  python manage.py shell
```


# modles

sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：
```python
python manage.py sqlmigrate App_name 0001
```



# javascript
##  快速入门
### 数据类型
#### number
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示  eg:0/0
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity  eg:2/0
#### bool
true; // 这是一个true值
false; // 这是一个false值
2 > 1; // 这是一个true值
2 >= 3; // 这是一个false值
NaN === NaN; // false
isNaN(NaN); // true
要特别注意相等运算符==。JavaScript在设计时，有两种比较运算符：

第一种是==比较，它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果；

第二种是===比较，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较。

#### null和undefined
null表示一个“空”的值，它和0以及空字符串''不同，0是一个数值，''表示长度为0的字符串，而null表示“空”。
var arr = [1, 2, 3.14, 'Hello', null, true];
arr[6]; // 索引超出了范围，返回undefined
#### 对象
```javascript
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
person.name; // 'Bob'
person.zipcode; // null
```
#### 变量
```javascript
var a = 123; // a的值是整数123
a = 'ABC'; // a变为字符串
```
在strict模式下运行的JavaScript代码，强制通过var申明变量，未使用var申明变量就使用的，将导致运行错误。
启用strict模式的方法是在JavaScript代码的第一行写上：
```javascript
'use strict';
```
####  string
```javascript
console.log(`多行
字符串
测试`);//多行字符串


var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);

var s = 'Test';
s[0] = 'X';
alert(s); // s仍然为'Test' 字符串不可变
```
toUpperCase()把一个字符串全部变为大写：
toLowerCase()把一个字符串全部变为小写：
indexOf()会搜索指定字符串出现的位置：
```javascript
var s = 'hello, world';
s.indexOf('world'); // 返回7
s.indexOf('World'); // 没有找到指定的子串，返回-1
```
substring()返回指定索引区间的子串
```javascript
var s = 'hello, world'
s.substring(0, 5); // 从索引0开始到5（不包括5），返回'hello'
s.substring(7); // 从索引7开始到结束，返回'world'
```
### array
```javascript
var arr = [1, 2, 3];
arr.length; // 3
arr.length = 6;
arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr; // arr变为[1, 2]
```
```javascript
var arr = [1, 2, 3];
arr[5] = 'x';
arr; // arr变为[1, 2, 3, undefined, undefined, 'x']
```
#### indexof()



```javascript
var arr = [10, 20, '30', 'xyz'];
arr.indexOf(10); // 元素10的索引为0
arr.indexOf(20); // 元素20的索引为1
arr.indexOf(30); // 元素30没有找到，返回-1
arr.indexOf('30'); // 元素'30'的索引为2
```

#### slice
slice()就是对应String的substring()版本，它截取Array的部分元素，然后返回一个新的Array：
```javascript
var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
arr.slice(0, 3); // 从索引0开始，到索引3结束，但不包括索引3: ['A', 'B', 'C']
arr.slice(3); // 从索引3开始到结束: ['D', 'E', 'F', 'G']

var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
var aCopy = arr.slice();
aCopy; // ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aCopy === arr; // false
```
#### push和pop
push()向Array的末尾添加若干元素，pop()则把Array的最后一个元素删除掉：
```javascript
var arr = [1, 2];
arr.push('A', 'B'); // 返回Array新的长度: 4
arr; // [1, 2, 'A', 'B']
arr.pop(); // pop()返回'B'
arr; // [1, 2, 'A']
arr.pop(); arr.pop(); arr.pop(); // 连续pop 3次
arr; // []
arr.pop(); // 空数组继续pop不会报错，而是返回undefined
arr; // []
```
#### unshift和shift
如果要往Array的头部添加若干元素，使用unshift()方法，shift()方法则把Array的第一个元素删掉：

#### sort()
#### reverse()
#### splice()

```javascript
var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 从索引2开始删除3个元素,然后再添加两个元素:
arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
// 只删除,不添加:
arr.splice(2, 2); // ['Google', 'Facebook']
arr; // ['Microsoft', 'Apple', 'Oracle']
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
```
#### contact
```javascript
var arr = ['A', 'B', 'C'];
var added = arr.concat([1, 2, 3]);
added; // ['A', 'B', 'C', 1, 2, 3]
arr; // ['A', 'B', 'C']



var arr = ['A', 'B', 'C'];
arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]
```
#### join

join()方法是一个非常实用的方法，它把当前Array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串：
```javascript
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
```
### 对象
xiaohong的属性名middle-school不是一个有效的变量，就需要用''括起来。访问这个属性也无法使用.操作符，必须用['xxx']来访问：
```javascript
var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};
xiaohong['middle-school']; // 'No.1 Middle School'
xiaohong['name']; // '小红'
xiaohong.name; // '小红'
console.log(xiaoming.age); // undefined
xiaoming.age = 18; // 新增一个age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
'name' in xiaoming; // true
'grade' in xiaoming; // false
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除一个不存在的school属性也不会报错
//因为toString定义在object对象中，而所有对象最终都会在原型链上指向object，所以xiaoming也拥有toString属性。
要判断一个属性是否是xiaoming自身拥有的，而不是继承得到的，可以用hasOwnProperty()方法：
'toString' in xiaoming; // true
xiaoming.hasOwnProperty('toString'); // false
```
### 条件判断
在多个if...else...语句中，如果某个条件成立，则后续就不再继续判断了。
```javascript
var age = 20;
if (age >= 6) {
    console.log('teenager');
} else if (age >= 18) {
    console.log('adult');
} else {
    console.log('kid');
}
//输出teenager
```
### 循环
```jacascript
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    console.log(key); // 'name', 'age', 'city'
}
```
### map和set
```javascrtpt
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
```

```javascript
var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3

var s = new Set([1, 2, 3, 3, '3']);
s; // Set {1, 2, 3, "3"}


var s = new Set([1, 2, 3]);
s; // Set {1, 2, 3}
s.delete(3);
s; // Set {1, 2}
```
### iterable
S6标准引入了新的iterable类型，Array、Map和Set都属于iterable类型。
```javascript
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});

```
## 函数
赠送函数arguments
vaScript还有一个免费赠送的关键字arguments，它只在函数内部起作用，并且永远指向当前函数的调用者传入的所有参数。arguments类似Array但它不是一个Array：
```javascript
function foo(x) {
    console.log('x = ' + x); // 10
    for (var i=0; i<arguments.length; i++) {
        console.log('arg ' + i + ' = ' + arguments[i]); // 10, 20, 30
    }
}
foo(10, 20, 30);
```
结构肤质，同时对多个变量赋值

```javscript
var [x, y, z] = ['hello', 'JavaScript', 'ES6'];

var x=1, y=2;
[x, y] = [y, x]//交换x,y的值

var {hostname:domain, pathname:path} = location;
//使用场景


function buildDate({year, month, day, hour=0, minute=0, second=0}) {
    return new Date(year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second);
}
buildDate({ year: 2017, month: 1, day: 1 });
// Sun Jan 01 2017 00:00:00 GMT+0800 (CST)
buildDate({ year: 2017, month: 1, day: 1, hour: 20, minute: 15 });
// Sun Jan 01 2017 20:15:00 GMT+0800 (CST)
```
###方法
```javascript
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var that = this; // 在方法内部一开始就捕获this
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - that.birth; // 用that而不是this
        }
        return getAgeFromBirth();
    }
};
xiaoming.age(); // 25
```
### 装饰器
```javascript
'use strict';

var count = 0;
var oldParseInt = parseInt; // 保存原函数

window.parseInt = function () {
    count += 1;
    return oldParseInt.apply(null, arguments); // 调用原函数
};
```
### map and reduce
```javascript
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(String); // ['1', '2', '3', '4', '5', '6', '7', '8', '9']

var arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
    return x + y;
}); // 25  求array的和

function(arr){//['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
	return arr.map(x=>{return x[0].toUpperCase()+x.substr(1).toLowerCase()});
}
```
### filter
```javascript
var arr = [1, 2, 4, 5, 6, 9, 10, 15];
var r = arr.filter(function (x) {
    return x % 2 !== 0;
});
r; // [1, 5, 9, 15]

arr = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];
r = arr.filter(function (element, index, self) {
    return self.indexOf(element) === index;
});//出去重复元素，indexof总是返回一个元素的位置

return arr.filter(function(x){for(var i=2;i<x;i++){if(x%i===0){return false;}}if(i===x){return true;}});
//筛选出素数
```
### sort
```javascript
var arr = [10, 20, 1, 2];
arr.sort(function (x, y) {
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
});
console.log(arr); // [1, 2, 10, 20]

//排序应该忽略大小写，按照字母序排序
var arr = ['Google', 'apple', 'Microsoft'];
arr.sort(function (s1, s2) {
    x1 = s1.toUpperCase();
    x2 = s2.toUpperCase();
    if (x1 < x2) {
        return -1;
    }
    if (x1 > x2) {
        return 1;
    }
    return 0;
}); // ['apple', 'Google', 'Microsoft']

```
### every and find
every()方法可以判断数组的所有元素是否满足测试条件。
```javascript
var arr = ['Apple', 'pear', 'orange'];
console.log(arr.every(function (s) {
    return s.length > 0;
})); // true, 因为每个元素都满足s.length>0

console.log(arr.every(function (s) {
    return s.toLowerCase() === s;
})); // false, 因为不是每个元素都全部是小写

//find()方法用于查找符合条件的第一个元素，如果找到了，返回这个元素，否则，返回undefined：
//findIndex()和find()类似，也是查找符合条件的第一个元素，不同之处在于findIndex()会返回这个元素的索引，如果没有找到，返回-1：
var arr = ['Apple', 'pear', 'orange'];
console.log(arr.find(function (s) {
    return s.toLowerCase() === s;
})); // 'pear', 因为pear全部是小写

console.log(arr.find(function (s) {
    return s.toUpperCase() === s;
})); // undefined, 因为没有全部是大写的元素

//forEach()和map()类似，它也把每个元素依次作用于传入的函数，但不会返回新的数组。forEach()常用于遍历数组，因此，传入的函数不需要返回值：
var arr = ['Apple', 'pear', 'orange'];
arr.forEach(console.log); // 依次打印每个元素

```
### 闭包//没看懂，以后有时间看
### 箭头函数
```javascript
x => x * x;
//等价于以下函数
function (x) {
    return x * x;
}

// 两个参数:
(x, y) => x * x + y * y

// 无参数:
() => 3.14

// 可变参数:
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}




x => ({ foo: x })

```
## 面向对象
```javascript
class Student {
    constructor(name) {
        this.name = name;
    }

    hello() {
        alert('Hello, ' + this.name + '!');
    }
}


class PrimaryStudent extends Student {
    constructor(name, grade) {
        super(name); // 记得用super调用父类的构造方法!
        this.grade = grade;
    }

    myGrade() {
        alert('I am at grade ' + this.grade);
    }
}

```
## 浏览器
### 浏览器对象
#### window
window对象有innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高。
对应的，还有一个outerWidth和outerHeight属性，可以获取浏览器窗口的整个宽高。
#### navigator
navigator对象表示浏览器的信息，最常用的属性包括：

navigator.appName：浏览器名称；
navigator.appVersion：浏览器版本；
navigator.language：浏览器设置的语言；
navigator.platform：操作系统类型；
navigator.userAgent：浏览器设定的User-Agent字符串。
#### screen
screen对象表示屏幕的信息，常用的属性有：

screen.width：屏幕宽度，以像素为单位；
screen.height：屏幕高度，以像素为单位；
screen.colorDepth：返回颜色位数，如8、16、24。
#### location
可以用location.href获取。要获得URL各个部分的值，可以这么写：

location.protocol; // 'http'
location.host; // 'www.example.com'
location.port; // '8080'
location.pathname; // '/path/index.html'
location.search; // '?a=1&b=2'
location.hash; // 'TOP'
#### document
```javascript
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置文本为abc:
p.innerHTML = 'ABC'; // <p id="p-id">ABC</p>
p.style.fontSize = '20px';
list.appendChild(js);
//创建新节点
haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
//如果我们要把子节点插入到指定的位置怎么办？可以使用parentElement.insertBefore(newElement, referenceElement);，子节点会插入到referenceElement之前。

//删除DOM

/ 拿到待删除节点:
var self = document.getElementById('to-be-removed');
// 拿到父节点:
var parent = self.parentElement;
// 删除:
var removed = parent.removeChild(self);
removed === self; // true

//学习到了操作表单
```

# Bootstrap 
[菜鸟链接](https://www.runoob.com/bootstrap/bootstrap-tutorial.html)
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
### 内联子标题
如果需要向任何标题添加一个内联子标题，只需要简单地在元素两旁添加 <small>，或者添加 .small class，这样子您就能得到一个字号更小的颜色更浅的文本
### 引导主体副本
给段落添加强调文本，则可以添加 class="lead"，这将得到更大更粗、行高更高的文本
### 缩写
Bootstrap 定义 <abbr> 元素的样式为显示在文本底部的一条虚线边框，当鼠标悬停在上面时会显示完整的文本（只要您为 <abbr> title 属性添加了文本）。为了得到一个更小字体的文本，请添加 .initialism 到 <abbr>。
### 地址
使用 <address> 标签，您可以在网页上显示联系信息。
## 列表
有序列表，无序列表，定义列表
## 代码
Bootstrap 允许您以两种方式显示代码：
```html
	<p><code>&lt;header&gt;</code> 作为内联元素被包围。</p>
<p>如果需要把代码显示为一个独立的块元素，请使用 &lt;pre&gt; 标签：</p>
<pre>
    &lt;article&gt;
        &lt;h1&gt;Article Heading&lt;/h1&gt;
    &lt;/article&gt;
</pre>
```
## 表单
在本章中，我们将学习 Bootstrap 对图片的支持。Bootstrap 提供了三个可对图片应用简单样式的 class：
```
.img-rounded：添加 border-radius:6px 来获得图片圆角。
.img-circle：添加 border-radius:50% 来让整个图片变成圆形。
.img-thumbnail：添加一些内边距（padding）和一个灰色的边框。
```
通过在 <img> 标签添加 .img-responsive 类来让图片支持响应式设计。 图片将很好地扩展到父元素。

.img-responsive 类将 max-width: 100%; 和 height: auto; 样式应用在图片上：

## 什么是字体图标

## 下拉菜单

## Bootstrap 进度条