%define keepstatic 1
Name:           bison
BuildRequires:  gcc-c++
Version:        2.7.1
Release:        0
Summary:        The GNU Parser Generator
License:        GPL-3.0+
Group:          Platform Development/Utilities
Url:            http://www.gnu.org/software/bison/bison.html
Source:         bison-%{version}.tar.xz
Source2:        baselibs.conf
Source1001:     bison.manifest
Requires:       m4

%description
Bison is a parser generator similar to yacc(1).

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
%configure --disable-nls
%__make %{?_smp_mflags}

%check
%__make %{?_smp_mflags} check

%install
%make_install

%files 
%manifest %{name}.manifest
%license COPYING
%{_bindir}/bison
%{_bindir}/yacc
%{_libdir}/liby.a
%{_datadir}/bison
%{_datadir}/aclocal/bison-i18n.m4
%doc %{_infodir}/bison.info*.gz
%doc %{_mandir}/man1/bison.1.gz
%doc %{_mandir}/man1/yacc.1.gz
