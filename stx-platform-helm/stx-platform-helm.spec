#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stx-platform-helm
Version  : 1.0
Release  : 2
URL      : file:///home/clear/tar/stx-platform-helm-1.0.tar.gz
Source0  : file:///home/clear/tar/stx-platform-helm-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : helm
BuildRequires : monitor-helm
BuildRequires : openstack-helm-infra
Patch1: 0001-add_makefile.patch

%description
This directory contains all StarlingX charts that need to be built to support
platform integration immediately after installation. Some charts are common
across applications. These common charts reside in the
stx-config/kubernetes/helm-charts directory. To include these in this
application update the build_srpm.data file and use the COPY_LIST_TO_TAR
mechanism to populate these commom charts.

%prep
%setup -q -n stx-platform-helm-1.0
%patch1 -p1

%build
## build_prepend content
%define helm_home  %{getenv:HOME}/.helm
%global app_name platform-integ-apps
%global helm_repo stx-platform
%global app_folder /usr/local/share/applications/helm
%global helm_folder /usr/lib/helm
%global toolkit_version 0.1.0
mkdir  %{helm_home}
mkdir  %{helm_home}/repository
mkdir  %{helm_home}/repository/cache
mkdir  %{helm_home}/repository/local
mkdir  %{helm_home}/plugins
mkdir  %{helm_home}/starters
mkdir  %{helm_home}/cache
mkdir  %{helm_home}/cache/archive
cp files/repositories.yaml %{helm_home}/repository/repositories.yaml
cp files/index.yaml %{helm_home}/repository/local/index.yaml
cp  %{helm_folder}/helm-toolkit-%{toolkit_version}.tgz helm-charts/
helm serve --repo-path . &
helm repo rm local
helm repo add local http://localhost:8879/charts
cd helm-charts
make rbd-provisioner
make ceph-pools-audit
make node-feature-discovery
cd -
kill %1
%define app_staging %{_builddir}/staging
%define app_tarball %{app_name}-%{version}-%{release}.tgz
mkdir -p %{app_staging}
cp files/metadata.yaml %{app_staging}
cp manifests/manifest.yaml %{app_staging}
mkdir -p %{app_staging}/charts
cp helm-charts/*.tgz %{app_staging}/charts
cd %{app_staging}
sed -i 's/@APP_NAME@/%{app_name}/g' %{app_staging}/metadata.yaml
sed -i 's/@APP_VERSION@/%{version}-%{release}/g' %{app_staging}/metadata.yaml
sed -i 's/@HELM_REPO@/%{helm_repo}/g' %{app_staging}/metadata.yaml
find . -type f ! -name '*.md5' -print0 | xargs -0 md5sum > checksum.md5
tar -zcf %{_builddir}/%{app_tarball} -C %{app_staging}/ .
cd -
rm -fr %{app_staging}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571033993
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
export SOURCE_DATE_EPOCH=1571033993
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{app_folder}
## install_append content
install -p -D -m 755 %{_builddir}/%{app_tarball} %{buildroot}/%{app_folder}
install -d -m 755 ${RPM_BUILD_ROOT}/opt/extracharts
install -p -D -m 755 helm-charts/node-feature-discovery-*.tgz ${RPM_BUILD_ROOT}/opt/extracharts
## install_append end

%files
%defattr(-,root,root,-)
/opt/extracharts/node-feature-discovery-0.3.0.tgz
/usr/local/share/applications/helm/platform-integ-apps-1.0-2.tgz