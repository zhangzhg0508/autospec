%define tis_patch_ver 1
%define _tis_build_type std
%global milestone .0rc2
# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

#STX: Turn off doc building
%global with_doc 0
%global service keystone
# guard for package OSP does not support
%global rhosp 0

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Keystone is a Python implementation of the OpenStack \
(http://www.openstack.org) identity service API.

Name:           openstack-keystone
# Liberty semver reset
# https://review.openstack.org/#/q/I6a35fa0dda798fad93b804d00a46af80f08d475c,n,z
Epoch:          1
Version:        15.0.0
Release:        0.2.el7%{?_tis_dist}.%{tis_patch_ver}
Summary:        OpenStack Identity Service
License:        Apache-2.0
URL:            http://keystone.openstack.org/
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
#
# patches_base=15.0.0.0rc2
#

Source1:        openstack-keystone.logrotate
Source3:        openstack-keystone.sysctl
Source5:        openstack-keystone-sample-data
Source20:       keystone-dist.conf

#STX
Source99:       openstack-keystone.service
Source100:      keystone-all
Source101:      keystone-fernet-keys-rotate-active
Source102:      password-rules.conf
Source103:      public.py

# STX: Include patches here
Patch1:         0001-Rebasing-Keyring-integration.patch

BuildArch:      noarch
BuildRequires:  openstack-macros
#BuildRequires:  python%{pyver}-devel
BuildRequires:  osprofiler >= 1.1.0
BuildRequires:  pbr >= 1.8
BuildRequires:  git
# Required to build keystone.conf
BuildRequires:  oslo-cache >= 1.26.0
BuildRequires:  oslo-config >= 2:5.2.0
BuildRequires:  passlib >= 1.6
BuildRequires:  pycadf >= 2.1.0
# Required to compile translation files
BuildRequires:  babel
# Required to build man pages
BuildRequires:  oslo-policy
BuildRequires:  jsonschema
BuildRequires:  oslo-db >= 4.27.0
BuildRequires:  oauthlib
BuildRequires:  pysaml2
BuildRequires:  keystonemiddleware >= 4.17.0
BuildRequires:  testresources
BuildRequires:  testscenarios
BuildRequires:  oslotest
# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-redis
%if 0%{rhosp} == 0
BuildRequires:  python-zmq
%endif
BuildRequires:  python-ldappool
BuildRequires:  python-webtest
BuildRequires:  python-freezegun
BuildRequires:  python-pep8
%else
BuildRequires:  redis
%if 0%{rhosp} == 0
BuildRequires:  zmq
%endif
BuildRequires:  ldappool
BuildRequires:  webtest
BuildRequires:  freezegun
BuildRequires:  pep8
%endif

Requires:       keystone = %{epoch}:%{version}-%{release}
Requires:       keystoneclient >= 1:3.8.0

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif
BuildRequires: systemd
Requires(pre):    shadow-utils

%description
%{common_desc}

This package contains the Keystone daemon.

%package -n       keystone
Summary:          Keystone Python libraries
%{?python_provide:%python_provide keystone}

Requires:       pbr
Requires:       bcrypt
Requires:       sqlalchemy >= 1.1.0
Requires:       passlib >= 1.7.0
Requires:       openssl
Requires:       six >= 1.10.0
Requires:       babel >= 2.3.4
Requires:       oauthlib >= 0.6.2
Requires:       jsonschema
Requires:       pycadf >= 2.1.0
Requires:       keystonemiddleware >= 5.1.0
Requires:       oslo-cache >= 1.26.0
Requires:       oslo-concurrency >= 3.26.0
Requires:       oslo-config >= 2:5.2.0
Requires:       oslo-context >= 2.22.0
Requires:       oslo-db >= 4.27.0
Requires:       oslo-i18n >= 3.15.3
Requires:       oslo-log >= 3.38.0
Requires:       oslo-messaging >= 5.29.0
Requires:       oslo-middleware >= 3.31.0
Requires:       oslo-policy >= 1.43.1
Requires:       oslo-serialization >= 2.18.0
Requires:       oslo-upgradecheck >= 0.1.0
Requires:       oslo-utils >= 3.33.0
Requires:       osprofiler >= 1.4.0
Requires:       pysaml2 >= 4.5.0
Requires:       stevedore >= 1.20.0
Requires:       scrypt
Requires:       flask
Requires:       flask-restful
Requires:       jwt
Requires:       pytz
# for Keystone Lightweight Tokens (KLWT)
Requires:       cryptography
# Handle python2 exception
%if %{pyver} == 2
Requires:       python-ldap
Requires:       python-ldappool
Requires:       python-memcached
Requires:       python-migrate >= 0.11.0
Requires:       python-webob >= 1.7.1
Requires:       python-dogpile-cache >= 0.6.2
Requires:       python-msgpack
%else
Requires:       ldap
Requires:       ldappool
Requires:       memcached
Requires:       migrate >= 0.11.0
Requires:       webob >= 1.7.1
Requires:       dogpile-cache >= 0.6.2
Requires:       msgpack
%endif


%description -n   keystone
%{common_desc}

This package contains the Keystone Python library.

%package -n %{service}-tests
Summary:        Keystone tests
%{?python_provide:%python_provide python%{pyver}-%{service}-tests}
Requires:       openstack-%{service} = %{epoch}:%{version}-%{release}

# Adding python-keystone-tests-tempest as Requires to keep backward
# compatibilty
%if %{pyver} == 2
Requires:       keystone-tests-tempest
%endif

#%description -n python%{pyver}-%{service}-tests
#%{common_desc}

#his package contains the Keystone test files.


%if 0%{?with_doc}
%package doc
Summary:        Documentation for OpenStack Identity Service

# for API autodoc
BuildRequires:  sphinx >= 1.1.2
BuildRequires:  openstackdocstheme
BuildRequires:  sphinxcontrib-apidoc
BuildRequires:  sphinxcontrib-seqdiag
BuildRequires:  flask
BuildRequires:  flask-restful
BuildRequires:  cryptography
BuildRequires:  oslo-concurrency >= 3.26.0
BuildRequires:  oslo-log >= 3.37.0
BuildRequires:  oslo-messaging >= 5.29.0
BuildRequires:  oslo-middleware >= 3.31.0
BuildRequires:  oslo-policy >= 1.30.0
BuildRequires:  mock
# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-dogpile-cache >= 0.5.7
BuildRequires:  python-memcached
BuildRequires:  python-lxml
%else
BuildRequires:  dogpile-cache >= 0.5.7
BuildRequires:  memcached
BuildRequires:  lxml
%endif


%description doc
%{common_desc}

This package contains documentation for Keystone.
%endif

%prep
%autosetup -n keystone-%{upstream_version} -S git

find . \( -name .gitignore -o -name .placeholder \) -delete
find keystone -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;
# Let RPM handle the dependencies
%py_req_cleanup

# adjust paths to WSGI scripts
sed -i 's#/local/bin#/bin#' httpd/wsgi-keystone.conf
sed -i 's#apache2#httpd#' httpd/wsgi-keystone.conf

%build
PYTHONPATH=. oslo-config-generator --config-file=config-generator/keystone.conf
PYTHONPATH=. oslo-config-generator --config-file=config-generator/keystone.conf --format yaml --output-file=%{service}-schema.yaml
PYTHONPATH=. oslo-config-generator --config-file=config-generator/keystone.conf --format json --output-file=%{service}-schema.json
# distribution defaults are located in keystone-dist.conf

%{pyver_build}
# Generate i18n files
%{pyver_bin} setup.py compile_catalog -d build/lib/%{service}/locale -D keystone

%install
%{pyver_install}

# Keystone doesn't ship policy.json file but only an example
# that contains data which might be problematic to use by default.
# Instead, ship an empty file that operators can override.
echo "{}" > policy.json

# STX: default dir for fernet tokens
install -d -m 750 %{buildroot}%{_sysconfdir}/keystone/credential-keys/
install -d -m 755 %{buildroot}%{_sysconfdir}/keystone
install -p -D -m 640 etc/keystone.conf.sample %{buildroot}%{_sysconfdir}/keystone/keystone.conf
install -p -D -m 640 policy.json %{buildroot}%{_sysconfdir}/keystone/policy.json
install -p -D -m 640 %{service}-schema.yaml %{buildroot}%{_datadir}/%{service}/%{service}-schema.yaml
install -p -D -m 640 %{service}-schema.json %{buildroot}%{_datadir}/%{service}/%{service}-schema.json
install -p -D -m 644 %{SOURCE20} %{buildroot}%{_datadir}/keystone/keystone-dist.conf
install -p -D -m 644 etc/policy.v3cloudsample.json %{buildroot}%{_datadir}/keystone/policy.v3cloudsample.json
install -p -D -m 640 etc/logging.conf.sample %{buildroot}%{_sysconfdir}/keystone/logging.conf
install -p -D -m 640 etc/default_catalog.templates %{buildroot}%{_sysconfdir}/keystone/default_catalog.templates
install -p -D -m 640 etc/sso_callback_template.html %{buildroot}%{_sysconfdir}/keystone/sso_callback_template.html
# STX: don't install a separate keystone logrotate file as this is managed by syslog-ng
#install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-keystone
install -d -m 755 %{buildroot}%{_prefix}/lib/sysctl.d
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/sysctl.d/openstack-keystone.conf
# Install sample data script.
install -p -D -m 755 tools/sample_data.sh %{buildroot}%{_datadir}/keystone/sample_data.sh
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/openstack-keystone-sample-data
# Install sample HTTPD integration files
install -p -D -m 644 httpd/wsgi-keystone.conf  %{buildroot}%{_datadir}/keystone/

# STX install keystone cron script
install -p -D -m 755 %{SOURCE101} %{buildroot}%{_bindir}/keystone-fernet-keys-rotate-active

# STX: install password rules(readable only)
install -p -D -m 440 %{SOURCE102} %{buildroot}%{_sysconfdir}/keystone/password-rules.conf

# STX: install keystone public gunicorn app
install -p -D -m 755 %{SOURCE103}  %{buildroot}/%{_datarootdir}/keystone/public.py

# STX: install openstack-keystone service script
install -p -D -m 644 %{SOURCE99} %{buildroot}%{_unitdir}/openstack-keystone.service

# STX: Install keystone-all bash script
install -p -D -m 755 %{SOURCE100} %{buildroot}%{_bindir}/keystone-all

install -d -m 755 %{buildroot}%{_sharedstatedir}/keystone
install -d -m 755 %{buildroot}%{_localstatedir}/log/keystone

# cleanup config files installed by keystone
# we already generate them w/ oslo-config-generator-%{pyver}
rm -rf %{buildroot}/%{_prefix}%{_sysconfdir}

# docs generation requires everything to be installed first
%if 0%{?with_doc}
sphinx-build-%{pyver} -b html doc/source doc/build/html

sphinx-build-%{pyver} -b man doc/source doc/build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/
%endif
%if 0%{?with_doc}
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{pyver_sitelib}/%{service}/locale/*/LC_*/%{service}*po
rm -f %{buildroot}%{pyver_sitelib}/%{service}/locale/*pot
mv %{buildroot}%{pyver_sitelib}/%{service}/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang %{service} --all-name

%pre
# 163:163 for keystone (openstack-keystone) - rhbz#752842
getent group keystone >/dev/null || groupadd -r --gid 163 keystone
getent passwd keystone >/dev/null || \
useradd --uid 163 -r -g keystone -d %{_sharedstatedir}/keystone -s /sbin/nologin \
-c "OpenStack Keystone Daemons" keystone
exit 0

%post
%sysctl_apply openstack-keystone.conf
# Install keystone.log file before, so both keystone & root users can write in it.
touch %{_localstatedir}/log/keystone/keystone.log
chown root:keystone %{_localstatedir}/log/keystone/keystone.log
chmod 660 %{_localstatedir}/log/keystone/keystone.log

%files
%license LICENSE
%doc README.rst
%if 0%{?with_doc}
%{_mandir}/man1/keystone*.1.gz
%endif
%{_bindir}/keystone-wsgi-admin
%{_bindir}/keystone-wsgi-public
%{_bindir}/keystone-manage
%{_bindir}/keystone-status
%{_bindir}/openstack-keystone-sample-data
# STX: add keystone-all
%{_bindir}/keystone-all
# STX: add Keystone fernet keys cron job
%{_bindir}/keystone-fernet-keys-rotate-active
%dir %{_datadir}/keystone
%attr(0644, root, keystone) %{_datadir}/keystone/keystone-dist.conf
%attr(0644, root, keystone) %{_datadir}/keystone/policy.v3cloudsample.json
%attr(0644, root, keystone) %{_datadir}/keystone/%{service}-schema.yaml
%attr(0644, root, keystone) %{_datadir}/keystone/%{service}-schema.json
%attr(0755, root, root) %{_datadir}/keystone/sample_data.sh
%attr(0644, root, keystone) %{_datadir}/keystone/wsgi-keystone.conf
# STX: add openstack-keystone sysinit script
%{_unitdir}/openstack-keystone.service
%dir %attr(0750, root, keystone) %{_sysconfdir}/keystone
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/keystone.conf
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/logging.conf
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/policy.json
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/default_catalog.templates
%config(noreplace) %attr(0640, keystone, keystone) %{_sysconfdir}/keystone/sso_callback_template.html
# STX: log rotate not needed
#%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-keystone
%dir %attr(-, keystone, keystone) %{_sharedstatedir}/keystone
%dir %attr(0750, keystone, keystone) %{_localstatedir}/log/keystone
%ghost %attr(0660, root, keystone) %{_localstatedir}/log/keystone/keystone.log
%{_prefix}/lib/sysctl.d/openstack-keystone.conf
# STX: add password rules configuration
%attr(0440, root, keystone) %{_sysconfdir}/keystone/password-rules.conf

%files -n python%{pyver}-keystone -f %{service}.lang
# STX: public.py addition
%{_datarootdir}/keystone/public*.py*
%defattr(-,root,root,-)
%license LICENSE
%{pyver_sitelib}/keystone
%{pyver_sitelib}/keystone-*.egg-info
%exclude %{pyver_sitelib}/%{service}/tests

%files -n python%{pyver}-%{service}-tests
%license LICENSE
%{pyver_sitelib}/%{service}/tests

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
* Wed Apr 03 2019 RDO <dev@lists.rdoproject.org> 1:15.0.0-0.2.0rc1
- Update to 15.0.0.0rc2

* Fri Mar 22 2019 RDO <dev@lists.rdoproject.org> 1:15.0.0-0.1.0rc1
- Update to 15.0.0.0rc1


