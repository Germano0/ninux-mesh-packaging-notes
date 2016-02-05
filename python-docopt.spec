%global pypi_name docopt
%global sum Pythonic argument parser, that will make you smile
# Python 3 only for Fedora for now.
%if 0%{?fedora} > 12
%global with_python3 1
%endif

Name:           python-docopt
Version:        0.6.2
Release:        1%{?dist}
Summary:        Pythonic argument parser, that will make you smile

License:        MIT
URL:            https://github.com/docopt/docopt
Source0:        http://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
BuildRequires:  pytest

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
%endif # if with_python3

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.


%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:  python2-devel
Requires:  python2-setuptools
Requires:  python2-nose
Requires:  pytest

%description -n python2-%{pypi_name}
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.


%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:  python3-devel
Requires:  python3-setuptools
Requires:  python3-nose
Requires:  python3-pytest

%description -n python3-%{pypi_name}
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.
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
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif # if with_python3

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
* Fri Feb 05 2016 Germano Massullo <germano.massullo@gmail.com> - 0.6.2-1
- Heavy edits to make spec file compliant to https://fedoraproject.org/wiki/Packaging:Python (package python-docopt did not provide a python2-docopt package in Fedora repositories)
- Removed egg files stuff since they are no longer present in upstream source file.
- 0.6.2 minor update

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Feb 03 2014 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.6.1-3
- Fix a mistake in spec file that prevented the subpackage from
  being created for Python 3

* Fri Nov 15 2013 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.6.1-2
- Enable python3 package

* Mon Aug 19 2013 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.6.1-1
- Upstream version sync

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.5.0-1
- Inital release
