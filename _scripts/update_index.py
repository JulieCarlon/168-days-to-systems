#!/usr/bin/env python3
"""
扫描 ~/Desktop/learning-plan/week-*/day-*.html，重建 index.html。
幂等：可以反复运行，输出始终基于当前文件系统的真实状态。

调用：python3 _scripts/update_index.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
INDEX = ROOT / "index.html"
TOTAL_DAYS = 168

# (week_num, day_within_week (1-7), day_label, topic, is_security_day)
CURRICULUM = [
    # Week 01 OS Part 1
    (1, 1, "Mon", "计算机系统大图 + 进程本质", False),
    (1, 2, "Tue", "进程深入：生命周期与状态机", False),
    (1, 3, "Wed", "线程模型与 Python GIL", False),
    (1, 4, "Thu", "CPU 调度", False),
    (1, 5, "Fri 🔧", "LAB：进程与调度动手", False),
    (1, 6, "Sat", "Linux 权限与提权基础", True),
    (1, 7, "Sun 🌐", "同步原语 + IPC + 周复盘", False),
    # Week 02 OS Part 2
    (2, 1, "Mon", "虚拟内存与页表", False),
    (2, 2, "Tue", "内存分配器", False),
    (2, 3, "Wed", "虚拟内存进阶", False),
    (2, 4, "Thu", "I/O 模型完整谱系", False),
    (2, 5, "Fri 🔧", "LAB：内存与 I/O 动手", False),
    (2, 6, "Sat", "系统调用追踪与 eBPF 入门", True),
    (2, 7, "Sun 🌐", "文件系统 + 零拷贝 + 周复盘", False),
    # Week 03 Network Part 1
    (3, 1, "Mon", "网络分层与 IP", False),
    (3, 2, "Tue", "TCP 深入", False),
    (3, 3, "Wed", "UDP + HTTP 协议演进", False),
    (3, 4, "Thu", "TLS / HTTPS", False),
    (3, 5, "Fri 🔧", "LAB：网络动手", False),
    (3, 6, "Sat", "网络抓包与协议分析", True),
    (3, 7, "Sun 🌐", "DNS + CDN + 周复盘", False),
    # Week 04 Network Part 2
    (4, 1, "Mon", "应用层协议全景", False),
    (4, 2, "Tue", "负载均衡", False),
    (4, 3, "Wed", "Nginx 深入", False),
    (4, 4, "Thu", "服务通信进阶", False),
    (4, 5, "Fri 🔧", "LAB：服务通信动手", False),
    (4, 6, "Sat", "反弹 shell 与 C2 框架", True),
    (4, 7, "Sun 🌐", "HTTP 请求完整旅程 + 周复盘", False),
    # Week 05 CPU
    (5, 1, "Mon", "CPU 工作原理", False),
    (5, 2, "Tue", "流水线、分支预测、乱序", False),
    (5, 3, "Wed", "缓存层级", False),
    (5, 4, "Thu", "SIMD + 多核 + 内存一致性", False),
    (5, 5, "Fri 🔧", "LAB：CPU 性能动手", False),
    (5, 6, "Sat", "侧信道攻击", True),
    (5, 7, "Sun 🌐", "CPU 与 LLM 推理关系 + 周复盘", False),
    # Week 06 Memory + NUMA
    (6, 1, "Mon", "内存系统全貌", False),
    (6, 2, "Tue", "NUMA 架构", False),
    (6, 3, "Wed", "为什么 LLM 推理是 memory-bound", False),
    (6, 4, "Thu", "内存优化技术", False),
    (6, 5, "Fri 🔧", "LAB：内存性能动手", False),
    (6, 6, "Sat", "内存安全攻防", True),
    (6, 7, "Sun 🌐", "PagedAttention + 周复盘", False),
    # Week 07 GPU
    (7, 1, "Mon", "GPU 基础", False),
    (7, 2, "Tue", "CUDA 编程模型", False),
    (7, 3, "Wed", "GPU 性能要点", False),
    (7, 4, "Thu", "GPU 互联", False),
    (7, 5, "Fri 🔧", "LAB：GPU 动手", False),
    (7, 6, "Sat", "GPU 多租户安全", True),
    (7, 7, "Sun 🌐", "GPU 选型与成本 + 周复盘", False),
    # Week 08 LLM Inference
    (8, 1, "Mon", "LLM 推理基础", False),
    (8, 2, "Tue", "KV cache 全解", False),
    (8, 3, "Wed", "量化技术", False),
    (8, 4, "Thu", "批处理、调度、解码加速", False),
    (8, 5, "Fri 🔧", "LAB：vLLM 部署", False),
    (8, 6, "Sat", "AI 推理服务攻击面", True),
    (8, 7, "Sun 🌐", "Phase 2 综合 + Phase 3 预告", False),
    # Week 09 Linux + Container
    (9, 1, "Mon", "cgroups", False),
    (9, 2, "Tue", "namespaces", False),
    (9, 3, "Wed", "capabilities + seccomp + LSM", False),
    (9, 4, "Thu", "容器 = ns + cgroups + 镜像", False),
    (9, 5, "Fri 🔧", "LAB：手搓容器", False),
    (9, 6, "Sat", "namespace / cgroup 滥用", True),
    (9, 7, "Sun 🌐", "容器同步与 IPC + 周复盘", False),
    # Week 10 Docker
    (10, 1, "Mon", "Docker 镜像", False),
    (10, 2, "Tue", "Docker 运行时", False),
    (10, 3, "Wed", "Docker 网络", False),
    (10, 4, "Thu", "Docker 存储", False),
    (10, 5, "Fri 🔧", "LAB：Docker 实战", False),
    (10, 6, "Sat", "容器逃逸", True),
    (10, 7, "Sun 🌐", "容器最佳实践 + 周复盘", False),
    # Week 11 K8s Core
    (11, 1, "Mon", "K8s 架构总览", False),
    (11, 2, "Tue", "Pod 与生命周期", False),
    (11, 3, "Wed", "控制器家族", False),
    (11, 4, "Thu", "网络与 Service", False),
    (11, 5, "Fri 🔧", "LAB：K8s 实战", False),
    (11, 6, "Sat", "K8s 安全", True),
    (11, 7, "Sun 🌐", "调度 + HPA + 周复盘", False),
    # Week 12 K8s Ecosystem
    (12, 1, "Mon", "GPU 调度", False),
    (12, 2, "Tue", "配置与密钥", False),
    (12, 3, "Wed", "存储", False),
    (12, 4, "Thu", "Operator + Helm", False),
    (12, 5, "Fri 🔧", "LAB：可观测性栈", False),
    (12, 6, "Sat", "运行时安全检测", True),
    (12, 7, "Sun 🌐", "Phase 3 综合 + Phase 4 预告", False),
    # Week 13 Go i
    (13, 1, "Mon", "为什么学 Go + 入门", False),
    (13, 2, "Tue", "Go 基础语法", False),
    (13, 3, "Wed", "struct + interface + 组合", False),
    (13, 4, "Thu", "goroutine + channel", False),
    (13, 5, "Fri 🔧", "LAB：Go 实战", False),
    (13, 6, "Sat", "Go 安全编码", True),
    (13, 7, "Sun 🌐", "sync + context + 周复盘", False),
    # Week 14 Go ii
    (14, 1, "Mon", "HTTP 服务", False),
    (14, 2, "Tue", "gRPC 服务", False),
    (14, 3, "Wed", "数据库访问", False),
    (14, 4, "Thu", "服务注册发现", False),
    (14, 5, "Fri 🔧", "LAB：完整微服务", False),
    (14, 6, "Sat", "内网渗透概览", True),
    (14, 7, "Sun 🌐", "Go + Python 协作 + 周复盘", False),
    # Week 15 MQ
    (15, 1, "Mon", "为什么用 MQ", False),
    (15, 2, "Tue", "Kafka 深入", False),
    (15, 3, "Wed", "RabbitMQ + Pulsar", False),
    (15, 4, "Thu", "Redis 作 MQ", False),
    (15, 5, "Fri 🔧", "LAB：Kafka 实战", False),
    (15, 6, "Sat", "API 安全", True),
    (15, 7, "Sun 🌐", "LLM 异步服务设计 + 周复盘", False),
    # Week 16 Gateway + Mesh
    (16, 1, "Mon", "API 网关", False),
    (16, 2, "Tue", "限流 + 熔断 + 降级", False),
    (16, 3, "Wed", "Service Mesh + Istio", False),
    (16, 4, "Thu", "可观测性进阶", False),
    (16, 5, "Fri 🔧", "LAB：网关 + 监控", False),
    (16, 6, "Sat", "零信任 + mTLS", True),
    (16, 7, "Sun 🌐", "Phase 4 综合 + Phase 5 预告", False),
    # Week 17 PostgreSQL
    (17, 1, "Mon", "关系数据库基础", False),
    (17, 2, "Tue", "索引", False),
    (17, 3, "Wed", "事务 + 隔离 + MVCC", False),
    (17, 4, "Thu", "查询优化", False),
    (17, 5, "Fri 🔧", "LAB：PG 实战", False),
    (17, 6, "Sat", "SQL 注入深入", True),
    (17, 7, "Sun 🌐", "复制备份 + 周复盘", False),
    # Week 18 Redis
    (18, 1, "Mon", "Redis 基础数据结构", False),
    (18, 2, "Tue", "持久化", False),
    (18, 3, "Wed", "集群", False),
    (18, 4, "Thu", "使用模式陷阱", False),
    (18, 5, "Fri 🔧", "LAB：Redis 实战", False),
    (18, 6, "Sat", "Redis 安全", True),
    (18, 7, "Sun 🌐", "LLM 服务中的 Redis + 周复盘", False),
    # Week 19 Vector DB
    (19, 1, "Mon", "向量数据库基础", False),
    (19, 2, "Tue", "向量数据库对比", False),
    (19, 3, "Wed", "RAG 架构", False),
    (19, 4, "Thu", "Embedding 工程", False),
    (19, 5, "Fri 🔧", "LAB：RAG 端到端", False),
    (19, 6, "Sat", "检索投毒 + indirect prompt injection", True),
    (19, 7, "Sun 🌐", "向量库性能调优 + 周复盘", False),
    # Week 20 Object + TS DB
    (20, 1, "Mon", "对象存储", False),
    (20, 2, "Tue", "时序数据库", False),
    (20, 3, "Wed", "大数据存储概览", False),
    (20, 4, "Thu", "存储选型实战", False),
    (20, 5, "Fri 🔧", "LAB：MinIO + Prometheus", False),
    (20, 6, "Sat", "数据脱敏 + 密钥管理", True),
    (20, 7, "Sun 🌐", "Phase 5 综合 + Phase 6 预告", False),
    # Week 21 Distributed Theory
    (21, 1, "Mon", "分布式基础", False),
    (21, 2, "Tue", "CAP + 一致性", False),
    (21, 3, "Wed", "共识算法", False),
    (21, 4, "Thu", "分布式存储", False),
    (21, 5, "Fri 🔧", "LAB：Raft 实战", False),
    (21, 6, "Sat", "分布式系统攻击面", True),
    (21, 7, "Sun 🌐", "综合 + Week 22 预告", False),
    # Week 22 HA + Chaos
    (22, 1, "Mon", "可用性指标", False),
    (22, 2, "Tue", "高可用模式", False),
    (22, 3, "Wed", "混沌工程", False),
    (22, 4, "Thu", "系统设计案例", False),
    (22, 5, "Fri 🔧", "LAB：混沌实验", False),
    (22, 6, "Sat", "供应链 + log4shell", True),
    (22, 7, "Sun 🌐", "综合 + Week 23 预告", False),
    # Week 23 LLM Serving
    (23, 1, "Mon", "推理引擎全景", False),
    (23, 2, "Tue", "推理网关", False),
    (23, 3, "Wed", "Agent 系统架构", False),
    (23, 4, "Thu", "多 Agent 协同", False),
    (23, 5, "Fri 🔧", "LAB：完整 Agent 服务", False),
    (23, 6, "Sat", "LLM / Agent 攻击面综述", True),
    (23, 7, "Sun 🌐", "综合 + Week 24 预告", False),
    # Week 24 Graduation
    (24, 1, "Mon", "需求与目标", False),
    (24, 2, "Tue", "架构设计", False),
    (24, 3, "Wed", "数据流设计", False),
    (24, 4, "Thu", "部署架构", False),
    (24, 5, "Fri 🔧", "LAB：设计文档", False),
    (24, 6, "Sat", "威胁建模 + 红蓝对抗", True),
    (24, 7, "Sun 🎓", "毕业总结", False),
]

WEEK_TITLES = {
    1: ("操作系统 Part 1：进程、线程、调度", "Linux 权限与提权"),
    2: ("操作系统 Part 2：内存、I/O、文件系统", "系统调用追踪 & eBPF 入门"),
    3: ("TCP/IP + HTTP/2/3 + TLS", "tcpdump + Wireshark 抓包"),
    4: ("REST / gRPC / WebSocket + Nginx + LB", "反弹 shell + C2 框架"),
    5: ("CPU 架构：流水线、缓存、SIMD", "侧信道：Spectre / Meltdown"),
    6: ("内存层级 + NUMA + LLM memory-bound", "内存安全：栈溢出、ASLR、ROP"),
    7: ("GPU 架构:SM、warp、HBM、NVLink", "GPU 多租户安全：MIG / MPS"),
    8: ("LLM 推理工程：KV cache、量化、vLLM", "AI 推理服务攻击面"),
    9: ("Linux 进阶 + 容器原理", "namespace / cgroup 滥用"),
    10: ("Docker 深入：镜像、网络、存储", "容器逃逸技术综述"),
    11: ("K8s 核心：Pod、Service、调度", "K8s 安全：RBAC、SA token"),
    12: ("K8s 生态 + 可观测性", "Falco / Tetragon 运行时检测"),
    13: ("Go 语言：goroutine + channel", "Go 安全编码"),
    14: ("Go 微服务 + 服务发现", "内网渗透概览：frp / Stowaway"),
    15: ("消息中间件：Kafka / RabbitMQ / Redis", "API 安全：JWT / OAuth / SSRF"),
    16: ("API 网关 + Service Mesh + Istio", "零信任 + mTLS + SPIFFE"),
    17: ("PostgreSQL：索引、事务、MVCC", "SQL 注入深入"),
    18: ("Redis：数据结构、集群、缓存陷阱", "Redis 未授权 + 缓存投毒"),
    19: ("向量数据库 + RAG", "⭐ 检索投毒 + indirect prompt injection"),
    20: ("对象存储 + 时序 DB + 大数据", "数据脱敏 + 密钥管理"),
    21: ("分布式理论：CAP / 一致性 / Raft", "分布式系统攻击面"),
    22: ("高可用 + 混沌工程 + SRE", "供应链：log4shell 复盘"),
    23: ("LLM 服务化 + Agent 系统架构", "⭐ LLM / Agent 攻击面综述"),
    24: ("毕业项目：10 万用户 Agent 安全平台", "威胁建模 + 红蓝对抗演练"),
}


def scan_existing_days():
    """返回 [(dd, week_num, file_path), ...] 列表，按 dd 排序"""
    days = []
    for week_dir in sorted(ROOT.glob("week-*")):
        m = re.match(r"week-(\d+)", week_dir.name)
        if not m:
            continue
        week_num = int(m.group(1))
        for f in sorted(week_dir.glob("day-*.html")):
            m2 = re.match(r"day-(\d+)\.html", f.name)
            if m2:
                days.append((int(m2.group(1)), week_num, f))
    return days


def build_index():
    existing_days = scan_existing_days()
    completed_count = len(existing_days)
    percent = completed_count / TOTAL_DAYS * 100

    # Latest day → current week / day-within-week
    if existing_days:
        latest_dd = existing_days[-1][0]
        latest_meta = CURRICULUM[latest_dd - 1]  # tuple
        cur_week, cur_dw, *_ = latest_meta
        progress_text = f"当前进度：Week {cur_week:02d} 进行中（Day {cur_dw} / 7）"
    else:
        progress_text = "尚未开始"

    # Build days grid
    day_cards = []
    for dd, week_num, _ in existing_days:
        meta = CURRICULUM[dd - 1]
        _, dw, label, topic, is_sec = meta
        sec_class = " sec" if is_sec else ""
        day_cards.append(
            f'    <a class="day-link{sec_class}" href="week-{week_num:02d}/day-{dd:02d}.html">'
            f'<span class="num">Day {dd:02d} · {label}</span>'
            f'<span class="topic">{topic}</span></a>'
        )
    days_grid = "\n".join(day_cards) if day_cards else "    <p>尚未开始</p>"

    # Build week rows
    completed_weeks = set()
    in_progress_weeks = set()
    if existing_days:
        weeks_with_days = set(w for _, w, _ in existing_days)
        # Count days per week
        from collections import Counter
        per_week = Counter(w for _, w, _ in existing_days)
        for w in weeks_with_days:
            if per_week[w] == 7:
                completed_weeks.add(w)
            else:
                in_progress_weeks.add(w)

    week_rows = []
    for week_num in range(1, 25):
        main_topic, sec_topic = WEEK_TITLES[week_num]
        if week_num in completed_weeks:
            status_html = '<div class="week-status done">已完成</div>'
        elif week_num in in_progress_weeks:
            status_html = '<div class="week-status done">进行中</div>'
        else:
            status_html = '<div class="week-status">待开始</div>'
        week_rows.append(
            f'  <div class="week-row">'
            f'<div class="week-num">Week {week_num:02d}</div>'
            f'<div class="week-main">{main_topic}</div>'
            f'<div class="week-sec">{sec_topic}</div>'
            f'{status_html}</div>'
        )
    week_list_html = "\n".join(week_rows)

    # Read existing index.html, find the dynamic regions, replace
    text = INDEX.read_text(encoding="utf-8")

    # 1. Progress numbers + bar
    text = re.sub(
        r'<div class="progress-text"><span><strong>\d+ / 168</strong> 天</span><span>[\d.]+%</span></div>\s*'
        r'<div class="progress-bar"><div class="progress-bar-fill" style="width: [\d.]+%"></div></div>\s*'
        r'<div style="font-size:12px;color:var\(--muted\);margin-top:8px;">[^<]+</div>',
        f'<div class="progress-text"><span><strong>{completed_count} / 168</strong> 天</span><span>{percent:.1f}%</span></div>\n'
        f'  <div class="progress-bar"><div class="progress-bar-fill" style="width: {percent:.1f}%"></div></div>\n'
        f'  <div style="font-size:12px;color:var(--muted);margin-top:8px;">{progress_text}</div>',
        text,
        count=1,
    )

    # 2. Week list rows
    text = re.sub(
        r'(<div class="week-list">)(.*?)(</div>\s*<h2 id="days">)',
        r'\1\n' + week_list_html + r'\n</div>\n\n<h2 id="days">',
        text,
        count=1,
        flags=re.DOTALL,
    )

    # 3. Days grid
    text = re.sub(
        r'(<div class="days-grid">)(.*?)(\s*</div>\s*<p style="margin-top: 16px;)',
        r'\1\n' + days_grid + r'\n  </div>\n  <p style="margin-top: 16px;',
        text,
        count=1,
        flags=re.DOTALL,
    )

    INDEX.write_text(text, encoding="utf-8")
    print(f"✓ index.html updated: {completed_count}/{TOTAL_DAYS} days ({percent:.1f}%)")


if __name__ == "__main__":
    build_index()
