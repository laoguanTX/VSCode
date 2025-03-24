% 定义二元函数
f = @(x, y) x.^2 + y.^2;

% 定义自变量范围
[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);

% 计算函数值
z = f(x, y);

% 计算导数
[fx, fy] = gradient(z, 0.1, 0.1);

% 绘制函数图像
figure;
surf(x, y, z);
title('二元函数图像');
xlabel('x');
ylabel('y');
zlabel('z');
shading interp;
colorbar;

% 绘制导数图像
figure;
quiver3(x, y, z, fx, fy, zeros(size(fx)));
title('二元函数导数图像');
xlabel('x');
ylabel('y');
zlabel('z');