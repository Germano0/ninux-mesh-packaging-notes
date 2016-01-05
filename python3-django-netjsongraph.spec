%global pypi_name django-netjsongraph

Name:           python3-%{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Reusable django app for collecting and visualizing network topology

Group:          Development/Libraries
License:        MIT
URL:            https://pypi.python.org/pypi/django-netjsongraph
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  ncurses-devel
Requires:       ncurses

%description
django-netjsongraph is a network topology collector and
network topology visualizer.
It supports collecting network topology from OLSR,
BATMAN-advanced, BMX and NetJSON NetworkGraph.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files 
%license LICENSE
%doc README.rst
%{python3_sitearch}/*

%changelog