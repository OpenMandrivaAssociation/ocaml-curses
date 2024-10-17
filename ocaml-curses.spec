%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml bindings for the ncurses library
Name:		ocaml-curses
Version:	1.0.3
Release:	4
License:	LGPLv2.1+
Group:		Development/Other
Url:		https://www.nongnu.org/ocaml-tmk/
Source0:	http://mirrors.linhub.com/savannah/ocaml-tmk/ocaml-curses-%{version}.tar.gz
BuildRequires:	gawk
BuildRequires:	ghostscript
BuildRequires:	ghostscript-common
BuildRequires:	libtool
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	texlive
BuildRequires:	pkgconfig(ncurses)

%description
The ncurses library provides functions to create rich text-mode interfaces.
This package contains the necessary files to use the ncurses library in OCaml.

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

#----------------------------------------------------------------------------

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
%doc doc
%{_libdir}/ocaml/curses/*.a
%{_libdir}/ocaml/curses/*.cmxa
%{_libdir}/ocaml/curses/*.mli

