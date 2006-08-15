#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	DBus
Summary:	Net::ACL - Perl extension for the DBus message system 
Summary(pl):	Net::ACL - Rozszerzenie Perla dla DBusa
Name:		perl-Net-DBus
Version:	0.33.3
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1663f7d4440fe2756c3dc315a80aeadc
Patch0:		%{name}-dbus.patch
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-XML-Twig
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DBus provides a Perl XS API to the dbus inter-application
messaging system. The Perl API covers the core base level 
of the dbus APIs, not concerning itself yet with the GLib
or QT wrappers. For more information on dbus visit the 
project website at:

  http://www.freedesktop.org/software/dbus/

%description -l pl
Modu³ Net::DBus dostarcza API Perla XS dla dbusa - demona komunikacji mieêdzy aplikacjami. API Perla pokrywa kluczow± funkcjonalno¶æ API dbusa, nie k³opocz±c siê jeszcze wrapperami GLiba albo QT. Po wiêcej informacji na temat dbusa odwied¼ stronê projektu na:
  http://www.freedesktop.org/software/dbus/

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Net/DBus.pm
%dir %{perl_vendorarch}/Net/DBus
%{perl_vendorarch}/Net/DBus/*.pm
%{perl_vendorarch}/Net/DBus/*.pod
%dir %{perl_vendorarch}/Net/DBus/Binding
%{perl_vendorarch}/Net/DBus/Binding/*.pm
%dir %{perl_vendorarch}/Net/DBus/Binding/Message
%{perl_vendorarch}/Net/DBus/Binding/Message/*.pm
%dir %{perl_vendorarch}/Net/DBus/Test
%{perl_vendorarch}/Net/DBus/Test/*.pm
%dir %{perl_vendorarch}/Net/DBus/Tutorial
%{perl_vendorarch}/Net/DBus/Tutorial/*.pod
%dir %{perl_vendorarch}/auto/Net/DBus
%{perl_vendorarch}/auto/Net/DBus/DBus*
%{_mandir}/man3/*
