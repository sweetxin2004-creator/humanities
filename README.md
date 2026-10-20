# humanities

面向人文社科科研的 Codex 技能工作区。十个来源已固定到具体 Git 提交，
安装后通过 `.agents/skills/` 提供十个入口，再按任务读取上游技能和参考资料。
原始技能库放在 `.local/skill-sources/`，不会把上千份技能描述同时塞入上下文。

## 安装与使用

需要 Git、Python 3.12、uv、Node.js/npm，以及浏览器流程需要的 Chromium。
当前云环境已提供这些基础工具。首次安装或重新构建依赖时运行：

```bash
bash install.sh
```

安装器校验 `skills.lock.json` 中的 15 个源仓库版本（十个来源及 AI Research
Skills 目录引用的五个 canonical 源仓库），并初始化 AERS 的 Paper-WorkFlow
子模块。它不会重置已有源仓库的改动。Python 依赖使用上游冻结锁文件或带哈希的
`requirements.humanities.lock`，浏览器工具使用 npm 锁文件。

日常检查已保留的安装状态：

```bash
bash startup.sh
```

新开一个位于此仓库的 Codex 会话即可重新发现技能，例如：

> 请使用 humanities-thesis，帮我诊断这个论文选题……

> 请使用 academic-humanizer，修改这段学术文字，保留数据、引用和论断边界……

已有会话可能不会即时刷新技能目录，可以显式读取 `skills/<入口>/SKILL.md`。
`codex skill load` 不是当前 Codex CLI 支持的命令；本项目不依赖该命令。

## 十个入口

| 来源 | 入口目录 | 使用方式 |
| --- | --- | --- |
| [Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | `skills/auto-empirical-research-skills/` | 原生目录路由，保留完整技能库和子模块 |
| [research-writing-skill](https://github.com/Norman-bury/research-writing-skill) | `skills/research-writing-skill/` | 读取上游科研写作主入口及模块 |
| [AcademicForge](https://github.com/HughYau/AcademicForge) | `skills/academic-forge/` | 索引本地 33 个技能；其他远程 pack 按需另装 |
| [paper-search-mcp](https://github.com/openags/paper-search-mcp) | `skills/paper-search/` | 上游技能、可运行 CLI 和 stdio MCP |
| [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | `skills/academic-humanizer/` | 上游学术润色指引和示例 |
| [cnki-skills](https://github.com/cookjohn/cnki-skills) | `skills/cnki-skills/` | 索引 10 个知网技能，配合浏览器 MCP |
| [humanities-thesis-skill](https://github.com/ganzhi-black/humanities-thesis-skill) | `skills/humanities-thesis-skill/` | 上游方法论、文本评估和文献脚本 |
| [research-plugins](https://github.com/wentorai/research-plugins) | `skills/research-plugins/` | 索引本地 473 个技能文件；不含其 OpenClaw 专用 API 插件 |
| [social-science-paper-writing-skill](https://github.com/fakerqwq/social-science-paper-writing-skill) | `skills/social-science-paper-writing-skill/` | 上游社科论文十阶段工作流 |
| [ai-research-skills](https://github.com/WenyuChiou/ai-research-skills) | `skills/ai-research-skills/` | 从五个 canonical 源仓库索引目录中的 17 个核心技能 |

入口的 `name` 由各个 `SKILL.md` 的 frontmatter 决定，可能与目录名略有不同。
上游来源、提交、许可证和附属文件均在本地保留；不修改上游技能内容。

## 本地工具与 MCP

```bash
./bin/paper-search sources
./bin/paper-search search "social capital" -s crossref,openalex -n 2 --source-timeout 20
./bin/humanities-review your-paper.md --format json
./bin/humanities-search --help
```

`.codex/config.toml` 为支持并信任项目配置的 Codex 客户端声明了
`paper-search` 和 `chrome-devtools` 两个 stdio MCP 服务。请从仓库目录启动客户端。
服务由客户端启动和关闭，不依赖安装时遗留的后台进程。
云端聊天的工具清单由平台管理，写入此文件不会直接改变当前聊天的工具列表；
上述 CLI 命令始终可供终端调用。

此云容器没有可用的 Chromium SUID/user-namespace 沙箱，因此项目 MCP 配置显式
设置了 `RESEARCH_CHROME_NO_SANDBOX=1`。浏览器在云容器内运行，TLS 校验保持开启。
在具备浏览器沙箱的桌面环境中应移除此环境变量。
Chrome 配置目录保存在忽略的 `.local/chrome-profile/`；不要把登录状态提交到 Git。

## 验证与访问条件

```bash
.local/skill-sources/paper-search-mcp/.venv/bin/python scripts/verify_runtime.py
```

该命令实际调用 Codex `skills/list`，检查十个入口无解析错误，运行人文文本评估，
初始化论文检索 MCP，并通过浏览器 MCP 打开本地测试页面及执行页面脚本。
它不调用付费模型，也不将本地通过等同于学术网站已可访问。

当前实例对 Crossref 的请求曾返回代理 `403 Forbidden`。
所需公开检索域名和知网域名已写入云环境的网络配置草稿，需要在环境设置中
审阅、保存并发布；设置应用后应重新执行真实检索，并检查返回论文的题名与 DOI。
上游工具在网络失败时可能返回退出码 0 和零条结果，因此退出码本身不能证明检索成功。

安装技能说明不等同于开通第三方服务：知网下载仍需要合法访问权限和可能的人工登录、
验证码；Zotero、NotebookLM、research-hub 自动化、R/Stata 和模型委派在选择相应
流程时再配置。默认公开文献检索不需要新增密钥。

云环境的可复用安装脚本和启动说明已另存到平台配置草稿。
仅提交 `.codex/environments/environment.toml` 不会发布云环境，也不会执行安装。
