%global pypi_name netjsonconfig

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Network configuration management library based on NetJSON DeviceConfiguration

License:        GPLv3
URL:            http://netjsonconfig.openwisp.org/
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-jinja2
BuildRequires:  python2-setuptools
BuildRequires:  python2-jsonschema
BuildRequires:  python-six
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description
netjsonconfig is a python library that converts NetJSON DeviceConfiguration
objects into real router configurations that can be installed on systems like
OpenWRT, LEDE or OpenWisp Firmware.

%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:  python2-nose
%description -n python2-%{pypi_name}
netjsonconfig is a python library that converts NetJSON DeviceConfiguration
objects into real router configurations that can be installed on systems like
OpenWRT, LEDE or OpenWisp Firmware.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:  python3-
%description -n python3-%{pypi_name}
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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Wed Aug 10 2016 Germano Massullo <germano.massullo@gmail.com> - 0.5.1-1
- First commit on Fedora's Git
