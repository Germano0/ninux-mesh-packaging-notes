%global pypi_name libcnml

Name:           python-%{pypi_name}
Version:        0.9.3
Release:        1%{?dist}
Summary:        libcnml is a CNML parser library for Python.

License:        GPLv3
URL:            https://github.com/PabloCastellano/libcnml
Source0:        https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3-devel

%description
Community Network Mark Up Language (CNML) is a project that aims to define
an open ISO standard and scalable for describing mesh clouds,
though it's not limited to this kind of networks and nowadays it's being
used also in point to point infrastructure networks.

CNML is a specification based on XML, which makes it easily extendible
and readable for humans besides of computers. It includes some ideas
from other implementations and previous concepts like nodeXchange and SNDX.

Some advantages of using CNML is that it allows to uncouple different
functionalities independently of the web application used to show the data,
reducing dependence from it and its internal tables of the database.

%package -n python2-%{pypi_name}
Summary:        libcnml is a CNML parser library for Python.
Requires:		python-six

%description -n python2-%{pypi_name}
Community Network Mark Up Language (CNML) is a project that aims to define
an open ISO standard and scalable for describing mesh clouds,
though it's not limited to this kind of networks and nowadays it's being
used also in point to point infrastructure networks.

CNML is a specification based on XML, which makes it easily extendible
and readable for humans besides of computers. It includes some ideas
from other implementations and previous concepts like nodeXchange and SNDX.

Some advantages of using CNML is that it allows to uncouple different
functionalities independently of the web application used to show the data,
reducing dependence from it and its internal tables of the database.

%package -n python3-%{pypi_name}
Summary:        libcnml is a CNML parser library for Python.
Requires:		python3-six

%description -n python3-%{pypi_name}
Community Network Mark Up Language (CNML) is a project that aims to define
an open ISO standard and scalable for describing mesh clouds,
though it's not limited to this kind of networks and nowadays it's being
used also in point to point infrastructure networks.

CNML is a specification based on XML, which makes it easily extendible
and readable for humans besides of computers. It includes some ideas
from other implementations and previous concepts like nodeXchange and SNDX.

Some advantages of using CNML is that it allows to uncouple different
functionalities independently of the web application used to show the data,
reducing dependence from it and its internal tables of the database.

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

%files -n python2-%{pypi_name}
%license LICENSE.txt
#%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE.txt
#%doc README.rst
%{python3_sitelib}/*

%changelog
* Mon Jan 11 2016 Germano Massullo <germano.massullo@gmail.com> - 0.9.3-1
- First Fedora release
