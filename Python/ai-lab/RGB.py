from PIL import Image

# 打开图片文件（请将'input.jpg'替换为你的图片路径）
image = Image.open('input.png').convert('RGB')
width, height = image.size

print(f"图像尺寸：{width}x{height}")

# 遍历每个像素
for y in range(height):
    for x in range(width):
        # 获取像素的RGB值
        r, g, b = image.getpixel((x, y))
        # 输出坐标和对应的RGB值
        print(f"坐标({x}, {y}) - R:{r:3d} G:{g:3d} B:{b:3d}")

# 可选：显示图像基本信息
print("\n图像基本信息：")
print(f"格式：{image.format}")
print(f"模式：{image.mode}")
print(f"尺寸：{image.size}")