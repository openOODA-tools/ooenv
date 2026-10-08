Name:           ooenv
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign POSIX environment controller, secret sanitizer, and execution simulator
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/ooenv
Source0:        ooenv-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooenv is a sovereign POSIX environment variable controller and executor
in 100% pure native openOODA (.oo). Features include capability-bounded
environment inspection, secret token redaction, dangerous variable auditing,
systemd unit override generation, and streaming Model Context Protocol (MCP).

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooenv
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooenv-uninstall

%files
/usr/bin/ooenv
/usr/bin/ooenv-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevation to v0.2.0 in pure native openOODA with execution simulation and streaming MCP
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
