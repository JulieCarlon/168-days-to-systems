# 从算法到工程 · 168 天系统底层补完计划

> 为 AI 算法工程师量身打造。6 个月 / 168 天，把「只懂模型」的算法工程师，淬炼成「懂硬件、懂网络、懂分布式」的系统型高级工程师。

每天一份 HTML 教材级密度内容，覆盖操作系统、网络、硬件、容器、服务化、数据库、分布式 6 大主题，外加贯穿全程的 AI 安全主线。

## 👥 这份内容适合谁

- **AI / ML 算法工程师**：模型训练、推理、优化都熟，但碰到 OS / 网络 / 容器 / 数据库就抓瞎，开会听同事说话像加密通信
- **AI 安全 / Agent 工程师**：理解大模型攻防，但对沙箱、容器逃逸、内网渗透这类基础设施安全话题不够熟练
- **从学界转工业界的学生 / 转码者**：技术栈以 Python + 算法为主，需要一份「工程系统」的体系化补课
- **想搞懂 LLM 服务化背后的工程底层**：知道 vLLM 跑得快，但说不清「为什么快」

## 💡 卖点

**站在 AI / Agent 工作场景讲底层。** 不是把 OS 教材抄一遍——为什么 LLM 推理是 memory-bound？为什么 PagedAttention 借鉴 OS 虚拟内存？vLLM 为什么必须用多进程而不是多线程？每个底层概念都映射到 AI 工程师的真实场景。

**安全主线贯穿全程。** 不是末尾蜻蜓点水一章「安全」——每周六固定 4 小时安全专题（共 24 个），从 Linux 提权、eBPF、反弹 shell，到容器逃逸、检索投毒、LLM 越狱攻击，AI 安全方向特别契合。

**教材级密度 + 每日 HTML。** 不是「5 分钟看一遍就忘」的碎片笔记——单日 30-50KB / 4000-8000 字密集材料，配大量命令实操，能坐下来扎实学 1.5-4 小时。

## ⏱ 时间分配

| 时段 | 时长 | 内容 |
|---|---|---|
| 周一 – 周四 | 4 × 2h | 主线技术概念 |
| 周五 | 2h | 动手 lab |
| **周六** | **4h** | **🔐 安全主线专题** |
| 周日 | 4h | 周复盘 + 与 Agent 安全的连结 + 下周预告 |
| **周累计** | **18h** | |

## 🗂 6 个阶段总览

| 阶段 | 周次 | 主题 |
|---|---|---|
| 1 | W01 – W04 | 操作系统 + 网络 |
| 2 | W05 – W08 | 硬件 + LLM 推理 |
| 3 | W09 – W12 | 容器 + Kubernetes |
| 4 | W13 – W16 | Go + 服务化 |
| 5 | W17 – W20 | 数据库与存储 |
| 6 | W21 – W24 | 分布式 + 综合实战 |

## 📅 完整课程表

### Phase 1 · 操作系统 + 网络（Week 01 – 04）

| 周 | 主线 | 周六安全主线 |
|---|---|---|
| **W01** | 操作系统 Part 1：进程、线程、调度 | Linux 权限与提权 |
| **W02** | 操作系统 Part 2：内存、I/O、文件系统 | 系统调用追踪 & eBPF 入门 |
| **W03** | TCP/IP + HTTP/2/3 + TLS | 网络抓包：tcpdump + Wireshark |
| **W04** | 服务通信：REST/gRPC/WebSocket + Nginx + LB | 反弹 shell & C2 框架概念 |

### Phase 2 · 硬件 + LLM 推理（Week 05 – 08）

| 周 | 主线 | 周六安全主线 |
|---|---|---|
| **W05** | CPU 架构：流水线、缓存、SIMD | 侧信道攻击：Spectre / Meltdown |
| **W06** | 内存层级 + NUMA + LLM memory-bound 分析 | 内存安全攻防：栈溢出、ASLR、ROP |
| **W07** | GPU 架构：SM、warp、HBM、NVLink | GPU 多租户安全：MIG / MPS |
| **W08** | LLM 推理工程：KV cache、量化、vLLM | AI 推理服务攻击面 |

### Phase 3 · 容器 + K8s（Week 09 – 12）

| 周 | 主线 | 周六安全主线 |
|---|---|---|
| **W09** | Linux 进阶 + 容器原理（cgroups / namespaces） | namespace / cgroup 滥用 |
| **W10** | Docker 深入：镜像、网络、存储 | 容器逃逸技术综述（CVE 复盘） |
| **W11** | K8s 核心：Pod / Service / 调度 | K8s 安全：RBAC + SA token 滥用 |
| **W12** | K8s 生态 + 可观测性 | 运行时检测：Falco / Tetragon |

### Phase 4 · Go + 服务化（Week 13 – 16）

| 周 | 主线 | 周六安全主线 |
|---|---|---|
| **W13** | Go 语言基础 + 并发模型 | Go 安全编码：SSRF / 反序列化 |
| **W14** | Go 微服务 + 服务发现 | 内网渗透概览：frp / Stowaway |
| **W15** | 消息中间件：Kafka / RabbitMQ / Redis | API 安全：JWT / OAuth / IDOR / SSRF |
| **W16** | API 网关 + Service Mesh + Istio | 零信任 + mTLS + SPIFFE |

### Phase 5 · 数据库与存储（Week 17 – 20）

| 周 | 主线 | 周六安全主线 |
|---|---|---|
| **W17** | PostgreSQL：索引、事务、MVCC、EXPLAIN | SQL 注入深入 |
| **W18** | Redis：数据结构、集群、缓存陷阱 | Redis 未授权访问 + 缓存投毒 |
| **W19** | 向量数据库 + RAG（FAISS / pgvector / Milvus） | 检索投毒 + indirect prompt injection ⭐ |
| **W20** | 对象存储 + 时序数据库 + 大数据格式 | 数据脱敏 + 密钥管理（Vault / KMS） |

### Phase 6 · 分布式 + 综合实战（Week 21 – 24）

| 周 | 主线 | 周六安全主线 |
|---|---|---|
| **W21** | 分布式系统理论：CAP / 一致性 / Raft | 分布式系统攻击面 |
| **W22** | 高可用 + 混沌工程 + SRE | 供应链攻击：log4shell 复盘 |
| **W23** | LLM 服务化深入 + Agent 系统架构 | LLM / Agent 攻击面综述 ⭐ |
| **W24** | **毕业项目**：设计 10 万用户 Agent 安全平台 | 威胁建模 + 红蓝对抗演练 |

> ⭐ 标记的两个主题与我本职工作强相关，是整套计划的"压舱石"。

## 📁 文件结构

```
.
├── index.html              # 24 周总览（landing page）
├── curriculum.html         # 168 天详细目录（每天 3-6 个核心概念点）
├── week-01/
│   ├── day-01.html
│   ├── day-02.html
│   └── ...
├── week-02/
└── ...
```

## ✅ 进度追踪

- [x] **Week 01** · 操作系统 Part 1（Day 01-05 完成）
- [ ] Week 02 · 操作系统 Part 2
- [ ] Week 03 · TCP/IP + HTTP
- [ ] Week 04 · 服务通信
- [ ] Week 05 · CPU 架构
- [ ] Week 06 · 内存层级 + NUMA
- [ ] Week 07 · GPU 架构
- [ ] Week 08 · LLM 推理工程
- [ ] Week 09 · Linux 进阶 + 容器原理
- [ ] Week 10 · Docker 深入
- [ ] Week 11 · K8s 核心
- [ ] Week 12 · K8s 生态 + 可观测性
- [ ] Week 13 · Go 语言 i
- [ ] Week 14 · Go 语言 ii + 微服务
- [ ] Week 15 · 消息中间件
- [ ] Week 16 · API 网关 + Service Mesh
- [ ] Week 17 · PostgreSQL
- [ ] Week 18 · Redis
- [ ] Week 19 · 向量数据库 + RAG
- [ ] Week 20 · 对象存储 + 时序数据库
- [ ] Week 21 · 分布式系统理论
- [ ] Week 22 · 高可用 + 混沌工程
- [ ] Week 23 · LLM 服务化 + Agent 架构
- [ ] Week 24 · 毕业项目

## 🤖 关于自动化

每天的 HTML 由 Claude Code 的定时任务自动生成。任务读 SKILL.md 里的 prompt（包含完整 168 天课程表、每日字数要求、风格规范），独立运行无需人工介入。

文件命名规则：`week-{WW}/day-{DD}.html`，DD 从 01 到 168，WW = ceil(DD/7)。

## 📜 内容说明

内容由 AI 辅助生成，按结构化 prompt 控制每日产出。已尽力保证准确性，但仍可能存在事实错误或表述偏差，涉及生产决策时请独立验证。

如果对你有帮助，欢迎 Star ⭐ / Fork 改成自己的版本。

Generated with [Claude Code](https://claude.com/claude-code).
