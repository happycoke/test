#coding:utf-8
import numpy as np   
from matplotlib import pyplot as plt   
from matplotlib import animation

# first set up the figure, the axis, and the plot element
# 这里我们建立了一个figure窗口，然后建立了一个轴，接着建立了一个我们要在动画中不断被修改的line对象
fig = plt.figure() 
ax1 = fig.add_subplot(2,1,1,xlim=(0, 2), ylim=(-4, 4))
ax2 = fig.add_subplot(2,1,2,xlim=(0, 2), ylim=(-4, 4))

line, = ax1.plot([], [], lw=2)  #set up blank line
line2, = ax2.plot([], [], lw=2) # 我们现在仅仅是画了一个空白的线，我们将稍后添加数据

#创建动画发生时调用的函数了。Init()是我们的动画在在创建动画基础框架(base frame)时调用的函数。
#这里我们们用一个非常简单的对line什么都不做的函数。这个函数一定要返回line对象，这个很重要，
#因为这样就能告诉动画之后要更新的内容，也就是动作的内容是line。

def init():  # very important,return line type,the content of animation is line
  line.set_data([], [])  
  line2.set_data([], [])  
  return line,line2


# animation function.  this is called sequentially   
#下面是动画函数。这个函数需要一个参数i，就是帧数，并且一边位移一边根据i画出正弦函数图象。

def animate(i):

  x = np.linspace(0, 2, 100)   
  y = np.sin(2 * np.pi * (x - 0.01*i))  
  line.set_data(x, y)	  


  x2 = np.linspace(0, 2, 100)   
  y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))  
  line2.set_data(x2, y2)   
  return line,line2#这里我们返回了我们修改过的对象，这将告诉动画框架哪一部分是要有动作的


#display animation
#frames帧数，每秒由几帧，这里也不一定一定要是个数字，可以是个generator 或iterable，详见API说明
#这个程序生成了100帧的数据, 然后在animation.FuncAnimation中只生产100帧plot, 在调用animate()时,
#i会从1到100, 这样就画出了变化的图形,而且每100帧重复.
#interval帧与帧之间间隔（ms）
#blit是一个非常重要的关键字，它告诉动画只重绘修改的部分
anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=100, interval=10,blit=True)  
plt.show()
