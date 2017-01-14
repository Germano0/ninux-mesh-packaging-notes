# Created by pyp2rpm-3.2.1
# Missing test requires, python3 version macro
%global pypi_name django-sortedm2m

Name:           python-%{pypi_name}
Version:        1.3.3
Release:        1%{?dist}
Summary:        Drop-in replacement for django's many to many field with sorted relations

License:        BSD
URL:            http://github.com/gregmuellegger/django-sortedm2m
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but remembers
the order of added relations.

%package -n     python2-%{pypi_name}
Summary:        Drop-in replacement for django's many to many field with sorted relations
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but remembers
the order of added relations.

%package -n     python3-%{pypi_name}
Summary:        Drop-in replacement for django's many to many field with sorted relations
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but remembers
the order of added relations.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/sortedm2m
%{python2_sitelib}/django_sortedm2m-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/sortedm2m
%{python3_sitelib}/django_sortedm2m-%{version}-py?.?.egg-info

%changelog
* Sat Jan 14 2017 Germano Massullo <germano.massullo@gmail.com> - 1.3.3-1
- Initial package.

