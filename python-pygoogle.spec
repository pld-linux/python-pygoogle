
%define		module	pygoogle

Summary:	Python interface to Google API
Summary(pl):	Interfejs Pythona do Google API
Name:		python-%{module}
Version:	0.6
Release:	0.3
License:	PSF
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	334e2d9e5a765ffa9769e2c4cdfcd110
URL:		http://pygoogle.sourceforge.net/
%pyrequires_eq	python-modules
Requires:	python-SOAP >= 0.11.3
BuildRequires:	python-devel >= 2.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to Google API.

%description -l pl
Interfejs do Google API.

%prep
%setup -q -n %{module}-%{version}

python setup.py build_py --compile --optimize=2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

cp build/lib/{google,GoogleSOAPFacade}.py{c,o} $RPM_BUILD_ROOT%{py_sitescriptdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{py_sitescriptdir}/*.py?
