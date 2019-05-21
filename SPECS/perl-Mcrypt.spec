Name:           perl-Mcrypt
Version:        2.5.7.0
Release:        1%{?dist}
Summary:        An Autoload-Capable Interface Module for libmcrypt
License:        Artistic-1.0
Group:          Development/Libraries
URL:            https://metacpan.org/pod/Mcrypt
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JESUS/Mcrypt-%{version}.tar.gz
Patch0:         Mcrypt-2.5.7.0-type.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libmcrypt-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Mcrypt module provides a simple and intuitive Perl abstraction of
the libmcrypt cryptography library.  It provides mechanisms for
encoding and decoding Perl scalars.

%prep
%setup -q -n Mcrypt-%{version}
%patch0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Tue Jan  8 2019 Alexander Ursu <aursu@hostopia.com> - 2.5.7.0-1
- Rebuild for CentOS7
