Summary:	OpenMoko icons
Summary(pl.UTF-8):	Ikony dla OpenMoko
Name:		openmoko-icons
Version:	0.0.0.2360
Release:	1
# ? no license mentioned in package
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1b1ea615820fcab22ec5ae1fde1f1a73
URL:		http://openmoko.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standard icon theme for OpenMoko.

%description -l pl.UTF-8
Standardowy motyw ikon dla OpenMoko.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_iconsdir}/openmoko-standard
