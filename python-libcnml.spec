%global pypi_name libcnml
%global sum libcnml is a CNML parser library for Python
# Python 3 only for Fedora for now.
%if 0%{?fedora} > 12
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.9.4
Release:        1%{?dist}
Summary:        %{sum}

License:        GPLv3
URL:            https://github.com/PabloCastellano/libcnml
Source0:        https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-six
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-six
%endif # if with_python3

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

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}
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
%endif # if with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

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

# Disabled tests since they rely on internet connection and Koji does not allow
# internet connection during package creating process. Further informations at
# https://github.com/PabloCastellano/libcnml/issues/18
#%check
#%{__python2} setup.py test
#%if 0%{?with_python3}
#%{__python3} setup.py test
#%endif # if with_python3

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*
%endif # if with_python3

%changelog
* Sat Jan 23 2016 Germano Massullo <germano.massullo@gmail.com> - 0.9.4-1
- First commit on Fedora's Git
