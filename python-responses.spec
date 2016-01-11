%global pypi_name responses

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        A utility library for mocking out the requests Python library.
License:        Apache License, Version 2.0
URL:            https://pypi.python.org/pypi/responses/0.5.0
Source0:        https://github.com/getsentry/responses/archive/%{pypi_name}-%{version}.tar.gz


BuildArch:      noarch

Requires:       python-requests
Requires:       python3-requests

%description
A utility library for mocking out the requests Python library.

%package -n python2-%{pypi_name}
Summary:        Reusable django app for collecting and visualizing network topology

%description -n python2-%{pypi_name}
A utility library for mocking out the requests Python library.

%package -n python3-%{pypi_name}
Summary:        Reusable django app for collecting and visualizing network topology

%description -n python3-%{pypi_name}
A utility library for mocking out the requests Python library.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

#%check
#%{__python2} setup.py test
#%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%{_bindir}/sample-exec-2.7

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/sample-exec
%{_bindir}/sample-exec-3.4

%changelog
