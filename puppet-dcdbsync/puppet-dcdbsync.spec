#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-dcdbsync
Version  : 1.0.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-dcdbsync-1.0.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-dcdbsync-1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-dcdbsync-data = %{version}-%{release}
BuildRequires : python-dev
Patch1: 0001-add-makefile.patch

%description
No detailed description available

%package data
Summary: data components for the puppet-dcdbsync package.
Group: Data

%description data
data components for the puppet-dcdbsync package.


%prep
%setup -q -n puppet-dcdbsync-1.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568797908
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
export SOURCE_DATE_EPOCH=1568797908
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/puppet/modules/dcdbsync
## install_append content
cp -R dcdbsync %{buildroot}%{_datadir}/puppet/modules
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/puppet/modules/dcdbsync/LICENSE
/usr/share/puppet/modules/dcdbsync/lib/puppet/provider/dcdbsync_config/ini_setting.rb
/usr/share/puppet/modules/dcdbsync/lib/puppet/type/dcdbsync_config.rb
/usr/share/puppet/modules/dcdbsync/manifests/api.pp
/usr/share/puppet/modules/dcdbsync/manifests/init.pp
/usr/share/puppet/modules/dcdbsync/manifests/keystone/auth.pp
/usr/share/puppet/modules/dcdbsync/manifests/params.pp
