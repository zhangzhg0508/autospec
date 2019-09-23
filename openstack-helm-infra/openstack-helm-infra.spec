#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstack-helm-infra
Version  : 1.0
Release  : 1
URL      : file:///home/clr/stx-tar/openstack-helm-infra-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/openstack-helm-infra-1.0.tar.gz
Source1  : file:///home/clr/stx-tar/repositories.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: openstack-helm-infra-python = %{version}-%{release}
Requires: openstack-helm-infra-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : helm
BuildRequires : pbr
Patch1: 0001-Allow-multiple-containers-per-daemonset-pod.patch
Patch2: 0002-Add-imagePullSecrets-in-service-account.patch
Patch3: 0003-Set-Min-NGINX-handles.patch
Patch4: 0004-Partial-revert-of-31e3469d28858d7b5eb6355e88b6f49fd6.patch
Patch5: 0005-Add-a-configmap-for-ingress-controller-config.patch
Patch6: 0006-Add-TLS-support-for-Gnocchi-public-endpoint.patch
Patch7: 0007-Fix-pod-restarts-on-all-workers-when-worker-added-re.patch
Patch8: 0008-Add-io_thread_pool-for-rabbitmq.patch
Patch9: 0009-Enable-override-of-rabbitmq-probe-parameters.patch
Patch10: 0001-fix-ip-address.patch

%description
====================
Openstack-Helm-Infra
====================
Mission
-------
The goal of OpenStack-Helm-Infra is to provide charts for services or
integration of third-party solutions that are required to run OpenStack-Helm.

%package python
Summary: python components for the openstack-helm-infra package.
Group: Default
Requires: openstack-helm-infra-python3 = %{version}-%{release}

%description python
python components for the openstack-helm-infra package.


%package python3
Summary: python3 components for the openstack-helm-infra package.
Group: Default
Requires: python3-core

%description python3
python3 components for the openstack-helm-infra package.


%prep
%setup -q -n openstack-helm-infra
cd ..
%setup -q -T -D -n openstack-helm-infra -b 1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p2

%build
## build_prepend content
%define helm_home %{getenv:HOME}/.helm
export PBR_VERSION=%{version}
mkdir %{helm_home}
mkdir %{helm_home}/repository
mkdir %{helm_home}/repository/cache
mkdir %{helm_home}/repository/local
mkdir %{helm_home}/plugins
mkdir %{helm_home}/starters
mkdir %{helm_home}/cache
mkdir %{helm_home}/cache/archive
tar -zxvf %{SOURCE1}
cp repositories.yaml %{helm_home}/repository/repositories.yaml
helm serve /tmp/charts --address 127.0.0.1:8879 --url http://127.0.0.1:8879/charts &
helm repo rm local
helm repo add local http://127.0.0.1:8879/charts
make helm-toolkit
make gnocchi
make ingress
make libvirt
make mariadb
make memcached
make openvswitch
make rabbitmq
make ceph-rgw
kill %1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568963215
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
echo "dont need check"
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
%global helm_folder  /usr/lib/helm
export PBR_VERSION=%{version}
install -d -m 755 ${RPM_BUILD_ROOT}%{helm_folder}
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
install -p -D -m 755 *.tgz %{buildroot}%{helm_folder}
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/helm/ceph-rgw-0.1.0.tgz
/usr/lib/helm/gnocchi-0.1.0.tgz
/usr/lib/helm/helm-toolkit-0.1.0.tgz
/usr/lib/helm/ingress-0.1.0.tgz
/usr/lib/helm/libvirt-0.1.0.tgz
/usr/lib/helm/mariadb-0.1.0.tgz
/usr/lib/helm/memcached-0.1.0.tgz
/usr/lib/helm/openvswitch-0.1.0.tgz
/usr/lib/helm/rabbitmq-0.1.0.tgz

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
