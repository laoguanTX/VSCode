from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from PIL import Image
import numpy as np

# 加载手写数字数据集
digits = datasets.load_digits()

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.5, random_state=42)

# 创建支持向量分类器
classifier = svm.SVC(gamma=0.001)

# 训练分类器
classifier.fit(X_train, y_train)

# 预测测试集
predicted = classifier.predict(X_test)

# 打印分类报告
print(metrics.classification_report(y_test, predicted))

# 打印混淆矩阵
print(metrics.confusion_matrix(y_test, predicted))

def load_image(image_path):
    # 打开图像并转换为灰度图像
    image = Image.open(image_path).convert('L')
    # 调整图像大小为8x8
    image = image.resize((8, 8), Image.LANCZOS)
    # 将图像转换为numpy数组
    image_data = np.array(image)
    # 反转颜色：黑色背景，白色数字
    image_data = np.invert(image_data)
    # 将像素值缩放到0-16之间
    image_data = (16 * image_data / 255.0).astype(int)
    # 展平数组
    image_data = image_data.flatten()
    return image_data

# 读取手写图片并进行预测
image_path = 'test.jpg'  # 替换为你的图像路径
image_data = load_image(image_path)
prediction = classifier.predict([image_data])
print(f'Predicted digit: {prediction[0]}')