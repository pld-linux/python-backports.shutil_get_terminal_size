#
# Conditional build:
%bcond_with	tests	# unit tests (no tests included in release tarball)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (makes sense only for Python < 3.3)

Summary:	Backport of get_terminal_size function from Python 3.3 shutil
Summary(pl.UTF-8):	Backport funkcji get_terminal_size z modułu shutil Pythona 3.3
Name:		python-backports.shutil_get_terminal_size
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backports.shutil_get_terminal_size/
Source0:	https://files.pythonhosted.org/packages/source/b/backports.shutil_get_terminal_size/backports.shutil_get_terminal_size-%{version}.tar.gz
# Source0-md5:	03267762480bd86b50580dc19dff3c66
URL:		https://pypi.org/project/backports.shutil_get_terminal_size/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 2.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 2.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A backport of the get_terminal_size function from Python 3.3's shutil.

Unlike the original version it is written in pure Python rather than
C, so it might be a tiny bit slower.

%description -l pl.UTF-8
Backport funkcji get_terminal_size z modułu shutil Pythona 3.3.

W przeciwieństwie do oryginalnej wersji, ta jest napisana w czystym
Pythonie, więc może być odrobinę wolniejsza.

%package -n python3-backports.shutil_get_terminal_size
Summary:	Backport of get_terminal_size function from Python 3.3 shutil
Summary(pl.UTF-8):	Backport funkcji get_terminal_size z modułu shutil Pythona 3.3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-backports.shutil_get_terminal_size
A backport of the get_terminal_size function from Python 3.3's shutil.

Unlike the original version it is written in pure Python rather than
C, so it might be a tiny bit slower.

%description -n python3-backports.shutil_get_terminal_size -l pl.UTF-8
Backport funkcji get_terminal_size z modułu shutil Pythona 3.3.

W przeciwieństwie do oryginalnej wersji, ta jest napisana w czystym
Pythonie, więc może być odrobinę wolniejsza.

%prep
%setup -q -n backports.shutil_get_terminal_size-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
# packaged in python-backports package
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/*.py[co]
%endif

%if %{with python3}
%py3_install

# not needed for python3 (PEP-420)?
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/backports/{*.py,__pycache__}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/backports/shutil_get_terminal_size
%{py_sitescriptdir}/backports.shutil_get_terminal_size-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-backports.shutil_get_terminal_size
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%dir %{py3_sitescriptdir}/backports
%{py3_sitescriptdir}/backports/shutil_get_terminal_size
%{py3_sitescriptdir}/backports.shutil_get_terminal_size-%{version}-py*.egg-info
%endif
