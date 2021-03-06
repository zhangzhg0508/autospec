#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mtce-storage
Version  : 1.0
Release  : 9
URL      : file:///home/clear/tar/mtce-storage-1.0.tar.gz
Source0  : file:///home/clear/tar/mtce-storage-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mtce-storage-data = %{version}-%{release}
Requires: mtce-storage-services = %{version}-%{release}
Requires: bash
Requires: systemd
BuildRequires : systemd
BuildRequires : systemd-devel
Patch1: 0001-change-sysconfig-dir.patch

%description
No detailed description available

%package data
Summary: data components for the mtce-storage package.
Group: Data

%description data
data components for the mtce-storage package.


%package services
Summary: services components for the mtce-storage package.
Group: Systemd services

%description services
services components for the mtce-storage package.


%prep
%setup -q -n mtce-storage-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567135861
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1567135861
rm -rf %{buildroot}
## install_prepend content
%define _sysconfdir /usr/local/etc
%define _unitdir /usr/lib/systemd/system/
## install_prepend end
make install buildroot=%{buildroot} _sysconfdir=%{_sysconfdir} _unitdir=%{_unitdir} _datarootdir=%{_datarootdir}
## install_append content
%post
systemctl enable goenabled-storage.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/init.d/goenabledStorage

%files data
%defattr(-,root,root,-)
/usr/share/licenses/mtce-storage-1.0/LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/goenabled-storage.service
