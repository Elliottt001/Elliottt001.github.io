# (づ￣ ³￣)づ Welcome !


Hi！这里是 张瑞喆的个人网站 [CosHub](https://r-z-zhang-ai.github.io/)


!!! note "" 
    <br><br>
    <div align="center" style="font-size:32px;font-weight:bold">
        ~「Miracles happen every day」~
    </div>
    <div align="center" style="font-size:12px">
        只有疯狂到相信自己能改变世界的人才能改变世界。  ———— Steven Paul Jobs
    </div>
    <br><br>

<!-- HTML Snippet -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plan Input</title>
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

我的计划是……

!!! success ""

    Date：2025-03-07

    - [ ] 之前所有课程作业
    - [ ] 学会verilog和vivado使用
    - [ ] 补上离散/微积分
        - [ ] 离散看书，微积分自学 + 智云

    - [ ] 这周看看离散/微积分可否自学！
    - [ ] 我真的想给自己的人生规划一下啊



!!! danger "努力更新中"

    - [ ] 《山茶文具店》
    - [ ] 2024年终总结

!!! info "正在学习的内容"

    - [ ] Python：[Python-100-days](https://github.com/jackfrued/Python-100-Days/tree/master)，[Python-50-days](https://github.com/jackfrued/Python-Core-50-Courses/)


!!! inline warning "施工中！" 

    惊喜多多，速来围观 ~

!!! success "推荐阅读"

    目前还没有……

---
