%global pypi_name django-netjsongraph

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        Reusable django app for collecting and visualizing network topology

License:        MIT
URL:            https://github.com/interop-dev/django-netjsongraph
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3-devel
Requires:       python-django >= 1.9
Requires:       python-django < 1.10
Requires:		python-django-rest-framework >= 3.3
Requires:		python-django-rest-framework < 3.4
Requires:		python-netdiff
Requires:		python-six

%description
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%package -n python2-%{pypi_name}
Summary:        Reusable django app for collecting and visualizing network topology

%description -n python2-%{pypi_name}
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%package -n python3-%{pypi_name}
Summary:        Reusable django app for collecting and visualizing network topology

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
* Mon Jan 11 2016 Germano Massullo <germano.massullo@gmail.com> - 0.1.3-1
- First Fedora release
