# 🛠️ Algorithms & Data Structures Collection
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A curated archive of every algorithm and data structure I’ve implemented so far—clean, tested, and ready to reuse.

- **Primary language:** Python (plus the occasional C++/Java snippet for performance comparisons)  
- **Layout:** top-level folders group implementations by **algorithmic paradigm** or **data-structure family** (e.g. `graph/`, `dp/`, `trees/`).

---

## ✨ Why this repo exists
1. **Reference** – quick, copy-paste templates for problem-solving, coding interviews, and contests.  
2. **Learning log** – commit history doubles as a record of what I learned and how each solution evolved.  
3. **Open-source karma** – free for anyone to fork, improve, and use.

---

## 📁 Directory structure (example)

```text
.
├── graph/        # shortest paths, MST, flow, SCC …
│   ├── dijkstra.py
│   ├── kruskal.py
│   └── dinic.py
├── dp/           # classical DP patterns
│   ├── lis.py
│   └── knapsack.py
├── trees/
│   ├── segment_tree.py
│   └── fenwick_tree.py
├── strings/
│   ├── kmp.py
│   └── suffix_array.py
└── others/
```
Naming convention
boj_<id>_<keyword>.py for solutions tied to a specific online-judge problem; plain <algorithm>.py for general templates.

---

📜 License
Distributed under the MIT License. See LICENSE for details.
