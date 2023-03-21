// 获取元素
var needle = document.querySelector('.needle');
var board = document.querySelector('.board');
var score = document.querySelector('.score');
var audio = document.querySelector('audio');
var circle = document.querySelector('div:nth-child(1)');
var triangle = document.querySelector('div:nth-child(2)');

// 初始化分数
var count = 0;

// 监听点击事件
circle.addEventListener('click', function() {
  // 播放音效
  audio.play();
  // 判断针是否在缝隙中
  if (needle.classList.contains('rotate')) {
    return;
  }
  // 添加旋转动画
  needle.classList.add('rotate');
  // 延时移除旋转动画
  setTimeout(function() {
    needle.classList.remove('rotate');
  }, 1000);
  // 判断针是否插入到缝隙中
  if (Math.abs(board.offsetLeft - needle.offsetLeft) < 20) {
    count++;
    score.innerHTML = count;
  } else {
    count = 0;
    score.innerHTML = count;
  }
});

triangle.addEventListener('click', function() {
  // 播放音效
  audio.play();
  // 判断针是否在缝隙中
  if (needle.classList.contains('rotate')) {
    return;
  }
  // 添加旋转动画
  needle.classList.add('rotate');
  // 延时移除旋转动画
  setTimeout(function() {
    needle.classList.remove('rotate');
  }, 1000);
  // 判断针是否插入到缝隙中
  if (Math.abs(board.offsetLeft - needle.offsetLeft) < 20) {
    count++;
    score.innerHTML = count;
  } else {
    count = 0;
    score.innerHTML = count;
  }
});

// 添加图形元素
var circle = document.createElement('div');
circle.style.width = '100px';
circle.style.height = '100px';
circle.style.borderRadius = '50%';
circle.style.backgroundColor = 'red';
circle.style.position = 'absolute';
circle.style.top = '20%';
circle.style.left = '50%';
circle.style.transform = 'translate(-50%, -50%)';
circle.style.pointerEvents = 'none';
document.body.appendChild(circle);

var triangle = document.createElement('div');
triangle.style.width = '0';
triangle.style.height = '0';
triangle.style.borderLeft = '25px solid transparent';
triangle.style.borderRight = '25px solid transparent';
triangle.style.borderBottom = '50px solid blue';
triangle.style.position = 'absolute';
triangle.style.top = '50%';
triangle.style.left = '50%';
triangle.style.transform = 'translate(-50%, -50%)';
triangle.style.pointerEvents = 'none';
document.body.appendChild(triangle);
