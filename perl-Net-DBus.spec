#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	DBus
Summary:	Net::DBus - Perl extension for the DBus message system 
Summary(pl.UTF-8):	Net::DBus - Rozszerzenie Perla dla systemu komunikacji DBus
Name:		perl-Net-DBus
Version:	0.33.6
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1dbce89b1b839fd0e46d74067ae2e35
URL:		http://search.cpan.org/dist/Net-DBus/
BuildRequires:	dbus-devel >= 0.90
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DBus provides a Perl XS API to the dbus inter-application
messaging system. The Perl API covers the core base level of the dbus
APIs, not concerning itself yet with the GLib or Qt wrappers. For more
information on dbus visit the project website at
<http://www.freedesktop.org/software/dbus/>.

%description -l pl.UTF-8
Moduł Net::DBus dostarcza API Perla XS dla dbusa - systemu komunikacji
między aplikacjami. API Perla pokrywa kluczową funkcjonalność API
dbusa, nie kłopocząc się jeszcze wrapperami GLiba albo Qt. Więcej
informacji na temat dbusa można znaleźć na stronie projektu:
<http://www.freedesktop.org/software/dbus/>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
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
