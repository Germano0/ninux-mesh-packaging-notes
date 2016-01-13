%global pypi_name libcnml
%global sum libcnml is a CNML parser library for Python

Name:           python-%{pypi_name}
Version:        0.9.3
Release:        1%{?dist}
Summary:        %{sum}

License:        GPLv3
URL:            https://github.com/PabloCastellano/libcnml
Source0:        https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python2-devel
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
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:		python2-six

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
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}
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
%doc README.md
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*

%changelog

