# 本仓库包含了课程小组作业的所有代码资源。

# 安装

执行以下命令克隆代码至本地仓库：

```bash
git clone https://github.com/Staudinger0325/-.git
```

执行以下命令安装依赖：

```bash
pip install -r requirements.txt
```

# **功能简介**

本仓库中的代码用于生成作业报告中的所有图片和分析结果。包含：

`fourier.py`：傅立叶变换

`laplace.py`：拉普拉斯变换

`z.py`：Z变换

`hartley.py`：赫尔曼（哈特莱）变换

`db6.py`：绘制小波变换依赖库`pywt`中小波函数`db6`的尺度函数、小波函数图像

`wavelet.py`：小波变换

`ftfr.py`：分数傅立叶变换

要单独执行以上python文件，请使用以下命令：

```bash
python3 <file_name>
```

此外，我们提供一个一键执行所有代码文件的脚本`exec.py`，要执行它，请使用以下命令：

```bash
python3 exec.py
```
