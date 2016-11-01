%global pypi_name netjsonconfig

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Network configuration management library based on NetJSON DeviceConfiguration

License:        GPLv3
URL:            http://netjsonconfig.openwisp.org/
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch


BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel

# BuildRequires for tests
BuildRequires:  python-nose
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python2-coverage
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python2-coveralls
BuildRequires:  python%{python3_pkgversion}-coveralls
BuildRequires:  python2-isort
BuildRequires:  python%{python3_pkgversion}-isort
BuildRequires:  python2-flake8
BuildRequires:  python%{python3_pkgversion}-flake8


%description
netjsonconfig is a python library that converts NetJSON DeviceConfiguration
objects into real router configurations that can be installed on systems like
OpenWRT, LEDE or OpenWisp Firmware.


%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:       python-jinja2
Requires:       python-jsonschema
Requires:       python-six
%description -n python2-%{pypi_name}
netjsonconfig is a python library that converts NetJSON DeviceConfiguration
objects into real router configurations that can be installed on systems like
OpenWRT, LEDE or OpenWisp Firmware.


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-jinja2
Requires:       python%{python3_pkgversion}-jsonschema
Requires:       python%{python3_pkgversion}-six
%description -n python%{python3_pkgversion}-%{pypi_name}
netjsonconfig is a python library that converts NetJSON DeviceConfiguration
objects into real router configurations that can be installed on systems like
OpenWRT, LEDE or OpenWisp Firmware.


%prep
%setup -q -n %{pypi_name}-%{version}

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

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Tue Nov 1 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.1-1
- First commit on Fedora's Git
