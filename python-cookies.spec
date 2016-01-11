%global pypi_name cookies

Name:           python-%{pypi_name}
Version:        2.2.1
Release:        1%{?dist}
Summary:        Friendlier RFC 6265-compliant cookie parser/renderer

License:        MIT
URL:            https://github.com/sashahart/cookies
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python
Requires:       python3
Requires:       pytest

%description
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).

%package -n python2-%{pypi_name}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.

%description -n python2-%{pypi_name}
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).


%package -n python3-%{pypi_name}
Summary:        Python library for parsing network topology data (eg: dynamic routing protocols, NetJSON, CNML) and detect changes.

%description -n python3-%{pypi_name}
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).


%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf test_cookies.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
rm -rf test_cookies.py
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
