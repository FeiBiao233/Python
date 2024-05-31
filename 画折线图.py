import matplotlib.pyplot as plt

# 假设这些是您的扭矩和应变数据
torques = [10, 20, 30, 40, 50]  # 扭矩数据
strains = [0.1, 0.2, 0.3, 0.4, 0.5]  # 应变数据

plt.plot(torques, strains, marker='o')  # 绘制折线图
plt.xlabel('施加扭矩 (Nm)')  # 横坐标标题
plt.ylabel('应变')  # 纵坐标标题
plt.title('扭矩 vs 应变 折线图')  # 图表标题
plt.grid(True)  # 显示网格
plt.show()  # 显示图表
