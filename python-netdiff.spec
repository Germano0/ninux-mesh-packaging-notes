%global pypi_name netdiff

Name:           python-%{pypi_name}
Version:        0.4.7
Release:        1%{?dist}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.

License:        MIT
URL:            https://github.com/ninuxorg/netdiff
Source0:        https://pypi.python.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

# EDIT REQUIRES
Requires:       python-networkx
Requires:       python-nose
Requires:       python3-nose
Requires:       python-requests
Requires:       python-six
Requires:       python-libcnml
Requires:       python-mock
Requires:       python3-mock

%description
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%package -n python2-%{pypi_name}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.

%description -n python2-%{pypi_name}
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%package -n python3-%{pypi_name}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.
%description -n python3-%{pypi_name}
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%prep
%setup -q -n %{pypi_name}-%{version}
# rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
