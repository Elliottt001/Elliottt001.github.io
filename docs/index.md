<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" 
    content="CosHub是张瑞喆的个人全域网站，主要包含本人在浙江大学学习期间的课堂笔记、心得感悟等内容">
    <base target="_blank">
    <title>张瑞喆的全域小站</title>
    <style>
        input[type="text"] {
            width: 100%;
            font-size: 17px;
        }
        textarea {
            width: 100%;
            font-size: 17px;
        }
    </style>
</head>

<body>
    <h1>(づ￣ ³￣)づ Welcome !</h1>
    <p>欢迎光临张瑞喆的个人网站（笔记本）<a href="https://r-z-zhang-ai.github.io/"> CosHub</a></p>
    <br><br>
    <div align="center" style="font-size:32px;font-weight:bold">
        ~「Miracles happen every day」~
    </div>
    <div align="center" style="font-size:12px">
        只有疯狂到相信自己能改变世界的人才能改变世界。  ———— Steven Paul Jobs
    </div>
    <br><br>
    <h3>今日份计划：</h3>
    <textarea id="planInput" placeholder="请输入您的计划..." rows="5"></textarea>
    <u></u>
    <script>
        // 获取textarea元素
        const planInput = document.getElementById('planInput');
        // 页面加载时，从localStorage中读取之前保存的计划
        window.addEventListener('load', () => {
            const savedPlan = localStorage.getItem('savedPlan');
            if (savedPlan) {
                planInput.value = savedPlan;
            }
        });
        // 当用户输入时，实时保存到localStorage
        planInput.addEventListener('input', () => {
            localStorage.setItem('savedPlan', planInput.value);
        });
    </script>
</body>
</html>

<!-- 我的计划是……

!!! success ""

    Date：2025-03-07

    - [ ] 之前所有课程作业
    - [ ] 学会verilog和vivado使用
    - [ ] 补上离散/微积分
        - [ ] 离散看书，微积分自学 + 智云

    - [ ] 这周看看离散/微积分可否自学！
    - [ ] 我真的想给自己的人生规划一下啊 -->



!!! danger "努力更新中"

    敬请期待

!!! info "正在学习的内容"

    - [Advanced Data Structure and Algorithm Analysis](https://r-z-zhang-ai.github.io/CS/algorithm/ads/)
    - [Computer System Principles](https://r-z-zhang-ai.github.io/CS/system/priciples/)
    - [C++ Programming Language](https://r-z-zhang-ai.github.io/CS/pl/C_Cpp/cpp/)
    - [Microeconomics](https://r-z-zhang-ai.github.io/FINANCE/micro/)
    - [Macroeconomics](https://r-z-zhang-ai.github.io/FINANCE/macro/)


!!! inline warning "施工中！" 

    惊喜多多，速来围观 ~

!!! success "推荐阅读"

    [Microeconomics](https://r-z-zhang-ai.github.io/FINANCE/micro/)

---
