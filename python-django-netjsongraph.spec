%global pypi_name django-netjsongraph

# Python 3 only for Fedora for now.
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Reusable django app for collecting and visualizing network topology

License:        MIT
URL:            https://github.com/interop-dev/django-netjsongraph
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-django >= 1.9, < 1.10
BuildRequires:  python2-django-model-utils
BuildRequires:  python2-django-rest-framework >= 3.3, < 3.4
BuildRequires:  python2-netdiff >= 0.4.7, <= 5.0
BuildRequires:  python2-setuptools

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-django >= 1.9, < 1.10
BuildRequires:  python3-django-model-utils
BuildRequires:  python3-django-rest-framework >= 3.3, < 3.4
BuildRequires:  python3-netdiff >= 0.4.7, <= 5.0
BuildRequires:  python3-setuptools
%endif

%description
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%package -n python2-%{pypi_name}
Summary:        %{Summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-django >= 1.9, < 1.10
Requires:       python2-django-model-utils
Requires:		python2-django-rest-framework >= 3.3, < 3.4
Requires:		python2-netdiff >= 0.4.7, <= 5.0
Requires:		python2-six

%description -n python2-%{pypi_name}
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%package -n python3-%{pypi_name}
Summary:        %{Summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-django >= 1.9, < 1.10
Requires:       python3-django-model-utils
Requires:		python3-django-rest-framework >= 3.3, < 3.4
Requires:		python3-netdiff >= 0.4.7, <= 5.0
Requires:		python3-six

%description -n python3-%{pypi_name}
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%prep
%setup -q -n %{pypi_name}-%{version}
# remove rm -rf %{pypi_name}.egg-info

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

