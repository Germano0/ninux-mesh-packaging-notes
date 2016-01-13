%global pypi_name netdiff

Name:           python-%{pypi_name}
Version:        0.4.7
Release:        1%{?dist}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.

License:        MIT
URL:            https://github.com/ninuxorg/netdiff
Source0:        https://pypi.python.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  python2-responses
BuildRequires:  python3-responses

%description
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%package -n python2-%{pypi_name}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.
Requires:       python2-libcnml
Requires:       python-mock
Requires:       python-networkx
Requires:       python-nose
Requires:       python-requests
Requires:       python-six

%description -n python2-%{pypi_name}
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%package -n python3-%{pypi_name}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.
Requires:       python3-libcnml
Requires:       python3-mock
Requires:       python3-networkx
Requires:       python3-nose
Requires:       python3-requests
Requires:       python3-six

%description -n python3-%{pypi_name}
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog

