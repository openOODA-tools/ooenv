# ooenv: Sovereign POSIX Environment Controller & Execution Simulator

<div align="center">

```
   _____ _____  ___  ______ _    __
  / ___// ___/ / _ \/ ____// |  / /
 / /__ / /__  /  __/ /_    | | / / 
 \___/ \___/  \___/\__/    | |/ /  
                           |___/   
```

**Sovereign Environment Variable Controller, Secret Sanitizer, and Execution Simulator**  
*Capability-bounded environment inspection, secret sanitization, and scoped export.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure native [openOODA](https://github.com/openOODA) (`.oo`).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Version: 0.2.0](https://img.shields.io/badge/version-0.2.0-blue.svg)](https://github.com/openOODA-tools/ooenv/releases/tag/v0.2.0)
[![Architecture: x86_64](https://img.shields.io/badge/Arch-x86__64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64)
```bash
curl -fsSL https://openooda-tools.github.io/ooenv/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (PKGBUILD)
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/ooenv/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/ooenv/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
ooenv-uninstall
# or: curl -fsSL https://openooda-tools.github.io/ooenv/uninstall.sh | bash
```

---

## 2. CLI Usage & Capabilities

```
usage: ooenv [options] [NAME=VALUE...] [COMMAND [ARG...]]

Capability-bounded environment inspection, secret sanitization, and execution simulation.

POSIX Options:
  -i, --ignore-environment   start with an empty environment
  -0, --null                 end each output line with NUL, not newline
  -u, --unset=NAME           remove variable from environment
  -C, --chdir=DIR            change working directory
  -S, --split-string=S       process and split S into separate arguments

Sovereign Security & Systemd Extensions:
      --audit                perform security audit for leaked credentials and unsafe PATH
      --sanitize             mask sensitive tokens and passwords in output
      --diff                 show differential between base and modified environments
      --filter <PREFIX>      display only variables beginning with PREFIX
      --systemd              generate systemd unit drop-in override configuration
      --unit <NAME>          specify systemd unit service name [default: service]
  -j, --json                 output formatted as JSON structure
  -D, --demo                 run multi-scenario sovereign environment showcase
      --mcp                  run as Model Context Protocol (MCP) stdio server
      --test                 run internal substrate anchor verification tests
  -h, --help                 display this help and exit
  -v, --version              output version information and exit
```

---

## 3. Security Auditing & Hygiene

`ooenv` contains built-in static analysis heuristics to detect environment-based security hazards:
* **Leaked Credentials:** Detects cloud tokens (`AWS_SECRET_ACCESS_KEY`), OAuth tokens (`GITHUB_TOKEN`), LLM provider keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`), and plaintext passwords.
* **Insecure PATH:** Identifies leading/trailing colons, empty segments (`::`), relative paths (`.`), and world-writable directories (`/tmp`, `/var/tmp`).
* **Injection Overrides:** Flags dangerous dynamic library injections (`LD_PRELOAD`, `LD_LIBRARY_PATH`, `DYLD_*`) and exported bash functions (`BASH_FUNC_*`).

---

## 4. Systemd & Fedora Server Integration

In accordance with Fedora Server conventions (`GEMINI.md`):
* `ooenv --systemd --unit <name>` produces unit drop-in configuration overrides targeted for `/etc/systemd/system/<name>.service.d/50-env.conf`.
* Supports generating Podman Quadlet container environment blocks for containerized workloads in `/etc/containers/systemd/`.

---

## 5. Model Context Protocol (MCP) Stdio Server

When executed with `--mcp`, `ooenv` provides a streaming JSON-RPC 2.0 stdio interface:

| Tool | Description |
| :--- | :--- |
| `env_list` | List variables with optional prefix filtering and secret sanitization |
| `env_get` | Retrieve variable by key with security risk classification |
| `env_simulate` | Apply unsets/overrides and compute environment diffs |
| `env_audit` | Audit environment against credential leaks and unsafe PATH hazards |
| `env_systemd` | Generate drop-in unit override configurations |
| `env_demo` | Multi-scenario sovereign environment showcase |

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
