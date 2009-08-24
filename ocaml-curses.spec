Name:           ocaml-curses
Version:        1.0.3
Release:        %mkrel 1
Summary:        OCaml bindings for the ncurses library
License:        LGPL
Group:          Development/Other
URL:            http://www.nongnu.org/ocaml-tmk/
Source0:        http://mirrors.linhub.com/savannah/ocaml-tmk/ocaml-curses-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  tetex-latex
#BuildRequires:  texlive-texmf-cmsuper
BuildRequires:  ghostscript
BuildRequires:  ghostscript-common
BuildRequires:  ncurses-devel
BuildRequires:  gawk
BuildRequires:  autoconf, automake, libtool

%description
The ncurses library provides functions to create rich text-mode interfaces.
This package contains the necessary files to use the ncurses library in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q
autoreconf

%build
%configure
make all opt
make doc

strip dllcurses_stubs.so

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/curses
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES
%dir %{_libdir}/ocaml/curses
%{_libdir}/ocaml/curses/META
%{_libdir}/ocaml/curses/*.cma
%{_libdir}/ocaml/curses/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc
%{_libdir}/ocaml/curses/*.a
%{_libdir}/ocaml/curses/*.cmxa
%{_libdir}/ocaml/curses/*.mli

