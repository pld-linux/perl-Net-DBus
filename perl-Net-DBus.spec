#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	DBus
Summary:	Net::ACL - Perl extension for the DBus message system 
Summary(pl):	Net::ACL - Rozszerzenie Perla dla systemu komunikacji DBus
Name:		perl-Net-DBus
Version:	0.33.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1663f7d4440fe2756c3dc315a80aeadc
Patch0:		%{name}-dbus.patch
URL:		http://search.cpan.org/dist/Net-DBus/
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DBus provides a Perl XS API to the dbus inter-application
messaging system. The Perl API covers the core base level of the dbus
APIs, not concerning itself yet with the GLib or Qt wrappers. For more
information on dbus visit the project website at
<http://www.freedesktop.org/software/dbus/>.

%description -l pl
Modu³ Net::DBus dostarcza API Perla XS dla dbusa - systemu komunikacji
miêdzy aplikacjami. API Perla pokrywa kluczow± funkcjonalno¶æ API
dbusa, nie k³opocz±c siê jeszcze wrapperami GLiba albo Qt. Wiêcej
informacji na temat dbusa mo¿na znale¼æ na stronie projektu:
<http://www.freedesktop.org/software/dbus/>.

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

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Net/DBus/*.pod
rm -rf $RPM_BUILD_ROOT%{perl_vendorarch}/Net/DBus/Tutorial

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%{perl_vendorarch}/Net/DBus.pm
%dir %{perl_vendorarch}/Net/DBus
%{perl_vendorarch}/Net/DBus/*.pm
%dir %{perl_vendorarch}/Net/DBus/Binding
%{perl_vendorarch}/Net/DBus/Binding/*.pm
%dir %{perl_vendorarch}/Net/DBus/Binding/Message
%{perl_vendorarch}/Net/DBus/Binding/Message/*.pm
%dir %{perl_vendorarch}/Net/DBus/Test
%{perl_vendorarch}/Net/DBus/Test/*.pm
%dir %{perl_vendorarch}/auto/Net/DBus
%{perl_vendorarch}/auto/Net/DBus/DBus.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/DBus/DBus.so
%{_mandir}/man3/*
