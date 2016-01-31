%global pypi_name responses
%global sum Reusable django app for collecting and visualizing network topology
# Python 3 only for Fedora for now.
%if 0%{?fedora} > 12
%global with_python3 1
%endif


Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        %{sum}
License:        ASL 2.0
URL:            https://github.com/getsentry/responses
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-cookies
BuildRequires:  python2-requests
BuildRequires:  python2-six
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-cookies
BuildRequires:  python3-requests
BuildRequires:  python3-six
%endif # if with_python3

%description
A utility library for mocking out the requests Python library.

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-requests
Requires:       python2-cookies
Requires:       python2-six

%description -n python2-%{pypi_name}
A utility library for mocking out the requests Python library.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-requests
Requires:       python3-cookies
Requires:       python3-six

%description -n python3-%{pypi_name}
A utility library for mocking out the requests Python library.
%endif # if with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

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

# upstream developer has not inserted tests in the current pypi release.
# Uncomment in version > 0.5.1
#%check
#%{__python2} setup.py test
#%if 0%{?with_python3}
#%{__python3} setup.py test
#%endif # if with_python3

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif # if with_python3

%changelog
* Mon Jan 25 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.1-1
- LICENSE file added in upstream update
- Commented %check section due test file missing in pypi release. See https://github.com/getsentry/responses/issues/98

* Sat Jan 23 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.0-1
- Package review submission
