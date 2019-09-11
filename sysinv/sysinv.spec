#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysinv
Version  : 1.0
Release  : 13
URL      : file:///home/clr/stx-tar/sysinv-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/sysinv-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: sysinv-bin = %{version}-%{release}
Requires: sysinv-python = %{version}-%{release}
Requires: sysinv-python3 = %{version}-%{release}
Requires: Django
Requires: WSME
Requires: WebTest
Requires: docker
Requires: eventlet
Requires: ipaddr
Requires: keyring
Requires: kubernetes
Requires: mox3
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.db
Requires: oslo.log
Requires: oslo.utils
Requires: parted
Requires: pbr
Requires: pecan
Requires: pyudev
Requires: six
Requires: tsconfig
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : systemd
BuildRequires : tox
BuildRequires : virtualenv

%description
Placeholder to allow setup.py to work.
Removing this requires modifying the
setup.py manifest.

%package bin
Summary: bin components for the sysinv package.
Group: Binaries

%description bin
bin components for the sysinv package.


%package python
Summary: python components for the sysinv package.
Group: Default
Requires: sysinv-python3 = %{version}-%{release}

%description python
python components for the sysinv package.


%package python3
Summary: python3 components for the sysinv package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sysinv package.


%prep
%setup -q -n sysinv-1.0

%build
## build_prepend content
%define local_bindir         /usr/bin/
%define local_etc_goenabledd /usr/local/etc/goenabled.d/
%define local_etc_sysinv     /usr/local/etc/sysinv/
%define local_etc_motdd      /usr/local/etc/motd.d/
%define pythonroot           /usr/lib64/python2.7/site-packages
%define ocf_resourced        /usr/lib/ocf/resource.d
%define debug_package %{nil}
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568183900
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
rm -rf *.egg-info
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
export PBR_VERSION=%{version}
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
python3 setup.py install --root=%{buildroot} --install-lib=%{pythonroot} --prefix=/usr --install-data=usr/share --single-version-externally-managed
install -d -m 755 %{buildroot}%{local_etc_goenabledd}
install -p -D -m 755 etc/sysinv/sysinv_goenabled_check.sh %{buildroot}%{local_etc_goenabledd}/sysinv_goenabled_check.sh
install -d -m 755 %{buildroot}%{local_etc_sysinv}
install -p -D -m 755 etc/sysinv/policy.json %{buildroot}%{local_etc_sysinv}/policy.json
install -p -D -m 640 etc/sysinv/profileSchema.xsd %{buildroot}%{local_etc_sysinv}/profileSchema.xsd
install -p -D -m 644 etc/sysinv/crushmap-storage-model.txt %{buildroot}%{local_etc_sysinv}/crushmap-storage-model.txt
install -p -D -m 644 etc/sysinv/crushmap-controller-model.txt %{buildroot}%{local_etc_sysinv}/crushmap-controller-model.txt
install -p -D -m 644 etc/sysinv/crushmap-aio-sx.txt %{buildroot}%{local_etc_sysinv}/crushmap-aio-sx.txt
install -d -m 755 %{buildroot}%{local_etc_motdd}
install -p -D -m 755 etc/sysinv/motd-system %{buildroot}%{local_etc_motdd}/10-system
install -d -m 755 %{buildroot}%{local_etc_sysinv}/upgrades
install -p -D -m 755 etc/sysinv/delete_load.sh %{buildroot}%{local_etc_sysinv}/upgrades/delete_load.sh
install -m 755 -p -D scripts/sysinv-api %{buildroot}/usr/lib/ocf/resource.d/platform/sysinv-api
install -m 755 -p -D scripts/sysinv-conductor %{buildroot}/usr/lib/ocf/resource.d/platform/sysinv-conductor
install -m 644 -p -D scripts/sysinv-api.service %{buildroot}%{_unitdir}/sysinv-api.service
install -m 644 -p -D scripts/sysinv-conductor.service %{buildroot}%{_unitdir}/sysinv-conductor.service
install -d -m 755 %{buildroot}%{local_bindir}
install -p -D -m 755 sysinv/cmd/partition_info.sh %{buildroot}%{local_bindir}/partition_info.sh
install -p -D -m 755 sysinv/cmd/manage-partitions %{buildroot}%{local_bindir}/manage-partitions
install -p -D -m 755 sysinv/cmd/query_pci_id %{buildroot}%{local_bindir}/query_pci_id
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/ocf/resource.d/platform/sysinv-api
/usr/lib/ocf/resource.d/platform/sysinv-conductor
/usr/local/etc/goenabled.d/sysinv_goenabled_check.sh
/usr/local/etc/motd.d/10-system
/usr/local/etc/sysinv/crushmap-aio-sx.txt
/usr/local/etc/sysinv/crushmap-controller-model.txt
/usr/local/etc/sysinv/crushmap-storage-model.txt
/usr/local/etc/sysinv/policy.json
/usr/local/etc/sysinv/profileSchema.xsd
/usr/local/etc/sysinv/upgrades/delete_load.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/manage-partitions
/usr/bin/partition_info.sh
/usr/bin/query_pci_id
/usr/bin/sysinv-agent
/usr/bin/sysinv-api
/usr/bin/sysinv-conductor
/usr/bin/sysinv-dbsync
/usr/bin/sysinv-dnsmasq-lease-update
/usr/bin/sysinv-helm
/usr/bin/sysinv-puppet
/usr/bin/sysinv-rootwrap
/usr/bin/sysinv-upgrade

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
