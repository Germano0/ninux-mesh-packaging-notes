%global pypi_name netdiff
%global sum Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.
# Python 3 only for Fedora for now.
%if 0%{?fedora} > 12
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.4.7
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/ninuxorg/netdiff
Source0:        https://pypi.python.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-libcnml
# python2-mock is missing, see https://bugzilla.redhat.com/show_bug.cgi?id=1301766
BuildRequires:  python-mock
#python2-networkx is missing, see https://bugzilla.redhat.com/show_bug.cgi?id=1301767
BuildRequires:  python-networkx
BuildRequires:  python2-nose
BuildRequires:  python2-requests
BuildRequires:  python2-responses
BuildRequires:  python2-six
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-libcnml
BuildRequires:  python3-mock
BuildRequires:  python3-networkx
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-responses
BuildRequires:  python3-six

%endif # if with_python3

%description
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:       python2-libcnml
# python2-mock is missing, see https://bugzilla.redhat.com/show_bug.cgi?id=1301766
Requires:       python-mock
#python2-networkx is missing, see https://bugzilla.redhat.com/show_bug.cgi?id=1301767
Requires:       python-networkx
Requires:       python2-nose
Requires:       python2-requests
Requires:       python2-six

%description -n python2-%{pypi_name}
Netdiff is a simple Python library that provides utilities for
parsing network topology data of open source dynamic
routing protocols and detecting changes in these topologies.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}
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
%endif # if with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # if with_python3

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif # if with_python3

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif # if with_python3

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif # if with_python3

%changelog
* Sat Jan 23 2016 Germano Massullo <germano.massullo@gmail.com> - 0.4.7-1
- First commit on Fedora's Git
