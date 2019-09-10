#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sm-api
Version  : 1.0
Release  : 5
URL      : file:///home/clr/stx-tar/sm-api-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/sm-api-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: sm-api-bin = %{version}-%{release}
Requires: sm-api-python = %{version}-%{release}
Requires: sm-api-services = %{version}-%{release}
Requires: sm-api-legacypython
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
Patch1: 0001-change-sysconfig-dir.patch

%description
No detailed description available

%package bin
Summary: bin components for the sm-api package.
Group: Binaries
Requires: sm-api-services = %{version}-%{release}

%description bin
bin components for the sm-api package.


%package legacypython
Summary: legacypython components for the sm-api package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the sm-api package.


%package python
Summary: python components for the sm-api package.
Group: Default

%description python
python components for the sm-api package.


%package services
Summary: services components for the sm-api package.
Group: Systemd services

%description services
services components for the sm-api package.


%prep
%setup -q -n sm-api-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566378266
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
%global _buildsubdir %{_builddir}/%{name}-%{version}
%global _sysconfdir "/usr/local/etc"
%global _unitdir "/usr/lib/systemd/system"
## install_prepend end
python2 -tt setup.py build -b py2 install --root=%{buildroot}
## install_append content
install -d %{buildroot}%{_sysconfdir}/sm
install -d %{buildroot}%{_sysconfdir}/init.d
install -d %{buildroot}%{_sysconfdir}/pmon.d
install -d %{buildroot}%{_sysconfdir}/sm-api
install -d %{buildroot}%{_unitdir}
install -m 644 %{_buildsubdir}/scripts/sm_api.ini %{buildroot}%{_sysconfdir}/sm
install -m 755 %{_buildsubdir}/scripts/sm-api %{buildroot}%{_sysconfdir}/init.d
install -m 644 %{_buildsubdir}/scripts/sm-api.service %{buildroot}%{_unitdir}
install -m 644 %{_buildsubdir}/scripts/sm-api.conf %{buildroot}%{_sysconfdir}/pmon.d
install -m 644 %{_buildsubdir}/etc/sm-api/policy.json %{buildroot}%{_sysconfdir}/sm-api
%post
/usr/bin/systemctl enable sm-api.service >/dev/null 2>&1
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/init.d/sm-api
/usr/local/etc/pmon.d/sm-api.conf
/usr/local/etc/sm-api/policy.json
/usr/local/etc/sm/sm_api.ini

%files bin
%defattr(-,root,root,-)
/usr/bin/sm-api

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/sm-api.service
