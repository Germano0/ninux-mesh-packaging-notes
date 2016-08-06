%global pypi_name django-netjsongraph
%global sum Reusable django app for collecting and visualizing network topology

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Reusable django app for collecting and visualizing network topology

License:        MIT
URL:            https://github.com/interop-dev/django-netjsongraph
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python2-pypandoc
BuildRequires:  python3-pypandoc

%description
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-pypandoc
Requires:       python2-django >= 1.9
Requires:       python2-django < 1.10
Requires:		python2-django-rest-framework >= 3.3
Requires:		python2-django-rest-framework < 3.4
Requires:		python2-netdiff
Requires:		python2-six

%description -n python2-%{pypi_name}
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pypandoc
Requires:       python3-django >= 1.9
Requires:       python3-django < 1.10
Requires:		python3-django-rest-framework >= 3.3
Requires:		python3-django-rest-framework < 3.4
Requires:		python3-netdiff
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

