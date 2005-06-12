
%define		module	pygoogle

Summary:	Python interface to Google API
Summary(pl):	Interfejs Pythona do Google API
Name:		python-%{module}
Version:	0.6
Release:	0.1
License:	PSF
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	8a613ac4d294bdd45601f9177d957090
URL:		http://pygoogle.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.2.1
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

cp build/lib/{google,SOAP,GoogleSOAPFacade}.py{c,o} $RPM_BUILD_ROOT%{py_sitescriptdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{py_sitescriptdir}/*.py?
