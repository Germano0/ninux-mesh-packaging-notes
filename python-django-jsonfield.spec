%global pypi_name django-jsonfield

# Python 3 only for Fedora for now.
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A reusable Django field that allows you to store validated JSON in your model

License:        BSD
URL:            https://github.com/bradjasper/django-jsonfield
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-django
BuildRequires:  python2-setuptools
BuildRequires:  python2-django-formtools
# for testing purposes
BuildRequires:  sqlite
%if 0%{?with_python3}
BuildRequires:  python3-django
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-django-formtools
%endif # if with_python3

%description
django-jsonfield is a reusable Django field that allows you to store validated JSON in your model.
It silently takes care of serialization. To use, simply add the field to one of your models.

%package -n python2-django-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:  python2-django
Requires:  python2-django-formtools
%description -n python2-django-%{pypi_name}
django-jsonfield is a reusable Django field that allows you to store validated JSON in your model.
It silently takes care of serialization. To use, simply add the field to one of your models.

%if 0%{?with_python3}
%package -n python3-django-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:  python3-django
Requires:  python3-django-formtools
%description -n python3-django-%{pypi_name}
django-jsonfield is a reusable Django field that allows you to store validated JSON in your model.
It silently takes care of serialization. To use, simply add the field to one of your models.
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

%check
sqlite3 FILETEMP
export DB_ENGINE=sqlite3
export DB_NAME="mydb"
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif # if with_python3

%files -n python2-django-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-django-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif # if with_python3

%changelog
* Wed Aug 10 2016 Germano Massullo <germano.massullo@gmail.com> - 1.0.3-1
- First commit on Fedora's Git
