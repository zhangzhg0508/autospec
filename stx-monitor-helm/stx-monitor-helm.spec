#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stx-monitor-helm
Version  : 1.0
Release  : 2
URL      : file:///home/clear/tar/stx-monitor-helm-1.0.tar.gz
Source0  : file:///home/clear/tar/stx-monitor-helm-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : monitor-helm
Patch1: 0001-makefile_no_build.patch

%description
This directory contains all StarlingX charts that need to be built for this
application. Some charts are common across applications. These common charts
reside in the stx-config/kubernetes/helm-charts directory. To include these in
this application update the build_srpm.data file and use the COPY_LIST_TO_TAR
mechanism to populate these common charts.

%prep
%setup -q -n stx-monitor-helm-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570866889
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
export SOURCE_DATE_EPOCH=1570866889
rm -rf %{buildroot}
## install_prepend content
%global armada_folder  /usr/lib/armada
## install_prepend end
install -d -m 755 ${RPM_BUILD_ROOT}%{armada_folder}
## install_append content
install -p -D -m 755 manifests/*.yaml ${RPM_BUILD_ROOT}%{armada_folder}
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/armada/monitor_manifest.yaml
