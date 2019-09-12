#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnsmasq-config
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/dnsmasq-config-1.0.tar.gz
Source0  : file:///home/clear/tar/dnsmasq-config-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: dnsmasq
Patch1: 0001-add_makefile.patch

%description
No detailed description available

%prep
%setup -q -n dnsmasq-config-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568191306
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
export SOURCE_DATE_EPOCH=1568191306
rm -rf %{buildroot}
## install_prepend content
%define _sysconfdir /usr/local/etc
## install_prepend end
mkdir -p %{buildroot}%{_sysconfdir}/init.d
## install_append content
install -m 755 init  %{buildroot}%{_sysconfdir}/init.d/dnsmasq
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/init.d/dnsmasq