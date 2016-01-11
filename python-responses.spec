%global pypi_name responses

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        A utility library for mocking out the requests Python library.
License:        Apache License, Version 2.0
URL:            https://pypi.python.org/pypi/responses/0.5.0
Source0:        https://github.com/getsentry/responses/archive/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3-devel

%description
A utility library for mocking out the requests Python library.

%package -n python2-%{pypi_name}
Summary:        Reusable django app for collecting and visualizing network topology
Requires:       python-requests
Requires:       python2-cookies
Requires:       python-six

%description -n python2-%{pypi_name}
A utility library for mocking out the requests Python library.

%package -n python3-%{pypi_name}
Summary:        Reusable django app for collecting and visualizing network topology
Requires:       python3-requests
Requires:       python3-cookies
Requires:       python3-six

%description -n python3-%{pypi_name}
A utility library for mocking out the requests Python library.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

#%check
#%{__python2} setup.py test
#%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Mon Jan 11 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.0-1
- First Fedora release
