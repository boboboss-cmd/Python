"""
    直方图:绘制连续性的数据,展示一组或者多组数据的分布状况(统计)
          只有原始数据能绘制成直方图
     应用场景:用户的年龄分布
             一段时间内用户点击次数的分布状态
             用户活跃时间的分布状态
    例:统计50部电影的时长
"""
# 导入
from matplotlib import pyplot as plt

# 输入数据
a = [121, 123, 145, 111, 132, 112, 145, 167, 134, 126,
     123, 154, 134, 200, 156, 124, 156, 123, 133, 127,
     128, 129, 128, 127, 126, 136, 129, 131, 132, 157,
     122, 133, 144, 167, 178, 190, 230, 211, 126, 123,
     124, 167, 90, 98, 189, 84, 70, 100, 167, 145, 112]

# 计算组数
d = 10  # 组距
num_bins = (max(a)-min(a))//d

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.hist(a, num_bins, normed=True)

# 设置X轴的刻度
plt.xticks(range(min(a), max(a)+d, d))

# 绘制网格
plt.grid(alpha=0.3)

# 展示
plt.show()
