Name:           perl-UUID
Version:        0.28
Release:        1%{?dist}
Summary:        DCE compatible Universally Unique Identifier library for Perl
License:        Artistic-2.0
Group:          Development/Libraries
URL:            https://metacpan.org/pod/UUID
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRM/UUID-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libuuid-devel
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The UUID library is used to generate unique identifiers for objects that may be
accessible beyond the local system. For instance, they could be used to
generate unique HTTP cookies across multiple web servers without communication
between the servers, and without fear of a name clash.

The generated UUIDs can be reasonably expected to be unique within a system,
and unique across all systems, and are compatible with those created by the
Open Software Foundation (OSF) Distributed Computing Environment (DCE) utility
uuidgen.

%prep
%setup -q -n UUID-%{version}

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
%doc Changes License README
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Tue Jan  8 2019 Alexander Ursu <alexander.ursu@gmail.com> - 0.28-1
- Rebuild for CentOS7