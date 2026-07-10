## RESTful API 架构

### 核心原则

1. 面向资源：一切皆资源，每个资源都有统一身份标识（URI，通常就是 URL）
2. 接口统一：统一四种 HTTP 方法来操作资源（`GET`, `POST`, `PUT`, `DELETE`）
3. 无状态：请求必须带 Token，不存储客户端状态信息
4. 表现层：信息二进制存储，json 格式表现出来给客户端

### HTTP 操作方法
```plaintext
┌──────────────────────────────────────────────────────┐
│ ① 请求行:  POST /api/retrieval/repos/search HTTP/1.1 │
│                                                      │
│ ② 请求头 (Headers):                                  │
│    Content-Type: application/json                    │
│    Host: localhost:9000                              │
│                                                      │
│ ③ 空行 (表示请求头结束)                               │
│                                                      │
│ ④ 请求体 (Body):                                     │
│    {                                                 │
│      "natural_language_query": "做一个图片社区",       │
│      "top_n": 3                                      │
│    }                                                 │
└──────────────────────────────────────────────────────┘
```

## FastAPI

是一个用于构建 API 的 Python Web 框架，且满足 RESTful API 的设计思想