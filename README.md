# SARIF to GitLab SAST Converter

This is a lightweight Python CLI tool that converts **Snyk SARIF** files into the GitLab **SAST JSON** format, enabling integration with GitLab's Security Dashboard.

---

## 🚀 Features

- Parse SARIF reports from `snyk code test --sarif`
- Generate GitLab-compliant `gl-sast-report.json`
- CLI interface for easy automation
- No external dependencies

---

## 📦 Installation

```bash
git clone https://github.com/your-username/sarif-to-gitlab-sast.git
cd sarif-to-gitlab-sast
pip install .
