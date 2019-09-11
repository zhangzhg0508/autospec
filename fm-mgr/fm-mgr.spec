#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fm-mgr
Version  : 1.0
Release  : 14
URL      : file:///home/clear/clearlinux/fm-mgr-1.0.tar.gz
Source0  : file:///home/clear/clearlinux/fm-mgr-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: fm-mgr-services = %{version}-%{release}
Requires: logrotate
BuildRequires : fm-common-dev
BuildRequires : systemd-devel
BuildRequires : util-linux-dev
Patch1: 0001-change-sysconfig-dir.patch

%description
No detailed description available

%package services
Summary: services components for the fm-mgr package.
Group: Systemd services

%description services
services components for the fm-mgr package.


%prep
%setup -q -n fm-mgr-1.0
%patch1 -p1

%build
## build_prepend content
VER=%{version}
MAJOR=`echo $VER | awk -F . '{print $1}'`
MINOR=`echo $VER | awk -F . '{print $2}'`
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565771941
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} MAJOR=$MAJOR MINOR=$MINOR


%install
export SOURCE_DATE_EPOCH=1565771941
rm -rf %{buildroot}
## install_prepend content
%global _sysconfdir	'/usr/local/etc'
%define local_dir /usr/local
%define local_bindir %{local_dir}/bin
%define _unitdir /usr/lib/systemd/system/
VER=%{version}
MAJOR=`echo $VER | awk -F . '{print $1}'`
MINOR=`echo $VER | awk -F . '{print $2}'`
## install_prepend end
make DESTDIR=%{buildroot} BINDIR=%{local_bindir} SYSCONFDIR=%{_sysconfdir} UNITDIR=%{_unitdir} MAJOR=$MAJOR MINOR=$MINOR install

%files
%defattr(-,root,root,-)
/usr/local/bin/fmManager
/usr/local/etc/init.d/fminit
/usr/local/etc/logrotate.d/fm.logrotate

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fminit.service