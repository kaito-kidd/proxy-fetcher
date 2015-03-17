# 描述
用来采集代理网站的代理IP。

## config.py
相关配置，例如采集网站列表、超时时间、校验参数的等。

## fetcher.py
代理采集器主程序，采集网站IP代理，输出目录见配置文件。

## tester.py
代理IP检查器，也叫测试过滤器，采集器采集的代理过多，但很多都不可用，用该程序检测可用的代理。

## 依赖
依赖[thread_pool](https://github.com/kaito-kidd/thread_pool)。

## 使用
    git clone https://github.com/kaito-kidd/proxy-fetcher.git

    cd proxy-fetcher

    git submodule init
    git submodule update

    # 获取代理列表,其中可能包含不可用的
    python fetcher.py

    # 测试代理列表,找出可用的代理IP
    python tester.py

## 说明
测试可用代理可根据需要调整`Pool`的大小,详情见`tester.py`。
