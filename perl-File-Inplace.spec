#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	File
%define		pnam	Inplace
Summary:	File::Inplace - Perl module for in-place editing of files
Summary(pl.UTF-8):	File::Inplace - moduł Perla do modyfikowania plików w miejscu
Name:		perl-File-Inplace
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fae0848ebef6969502dde017805a31a1
URL:		http://search.cpan.org/dist/File-Inplace/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Inplace is a Perl module intended to ease the common task of
editing a file in-place. Inspired by variations of perl's -i option,
this module is intended for somewhat more structured and reusable
editing than command line perl typically allows. File::Inplace
endeavors to guarantee file integrity; that is, either all of the
changes made will be saved to the file, or none will. It also offers
functionality such as backup creation, automatic field splitting
per-line, automatic chomping/unchomping, and aborting edits partially
through without affecting the original file.

%description -l pl.UTF-8
File::Inplace to moduł Perla mający na celu ułatwienie modyfikowania
plików w miejscu. Jest zainspirowany wariantami opcji -i programu perl
i ma udostępniać bardziej strukturalne i nadające się do ponownego
zastosowania formy edycji, niż zwykle pozwala wywoływanie perla z
linii poleceń. File::Inplace próbuje zagwarantować integralność pliku
- co oznacza, że albo wszystkie zmiany zostaną zapisane, albo żadna.
Oferuje także funkcje takie jak tworzenie kopii zapasowych,
automatyczny podział na pola w linii, automatyczne usuwanie i
dodawanie separatorów (chomp/unchomp) oraz przerywanie nie
zakończonych modyfikacji bez naruszania oryginalnego pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/Inplace.pm
%{_mandir}/man3/File::Inplace.3pm*
