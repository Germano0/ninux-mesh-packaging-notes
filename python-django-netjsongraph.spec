%global pypi_name django-netjsongraph

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Reusable django app for collecting and visualizing network topology

Group:          Development/Libraries # would you change it?
License:        MIT
URL:            https://github.com/interop-dev/django-netjsongraph
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

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
rm -rf %{pypi_name}.egg-info

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
%files -n python2-%{srcname}
%license COPYING
%doc README.rst
%{python2_sitelib}/*
%{_bindir}/sample-exec-2.7

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/sample-exec
%{_bindir}/sample-exec-3.4

%changelog
