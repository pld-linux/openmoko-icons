#
Summary:	OpenMoko icons
Name:		openmoko-icons
Version:	0.0.0.2360
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1b1ea615820fcab22ec5ae1fde1f1a73
URL:		http://openmoko.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libmatchbox-devel >= 1.8
BuildRequires:	openmoko-libs-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define openmokoname %(echo %{name} | sed -e 's/openmoko-//')

%description
OpenMoko icons

%prep
%setup -q

%build
%{__libtoolize}
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
%{_iconsdir}/openmoko-standard/
