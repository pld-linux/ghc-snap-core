%define		pkgname	snap-core
Summary:	Snap: A Haskell Web Framework (core interfaces and types)
Name:		ghc-%{pkgname}
Version:	0.9.4.1
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	56863d2614ae698aa7c35ebf9835cee1
URL:		http://hackage.haskell.org/package/PACKAGE_NAME/
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-prof
BuildRequires:	ghc-attoparsec
BuildRequires:	ghc-attoparsec-prof
BuildRequires:	ghc-attoparsec-enumerator
BuildRequires:	ghc-attoparsec-enumerator-prof
BuildRequires:	ghc-blaze-builder >= 0.2.1.4
BuildRequires:	ghc-blaze-builder-prof >= 0.2.1.4
BuildRequires:	ghc-blaze-builder-enumerator
BuildRequires:	ghc-blaze-builder-enumerator-prof
BuildRequires:	ghc-case-insensitive >= 0.3
BuildRequires:	ghc-case-insensitive-prof >= 0.3
BuildRequires:	ghc-hashable
BuildRequires:	ghc-hashable-prof
BuildRequires:	ghc-HUnit >= 1.2
BuildRequires:	ghc-HUnit-prof >= 1.2
BuildRequires:	ghc-MonadCatchIO-transformers >= 0.2.1
BuildRequires:	ghc-MonadCatchIO-transformers-prof >= 0.2.1
BuildRequires:	ghc-mtl >= 2.0
BuildRequires:	ghc-mtl-prof >= 2.0
BuildRequires:	ghc-random
BuildRequires:	ghc-random-prof
BuildRequires:	ghc-regex-posix >= 0.95
BuildRequires:	ghc-regex-posix-prof >= 0.95
BuildRequires:	ghc-unix-compat >= 0.2
BuildRequires:	ghc-unix-compat-prof >= 0.2
BuildRequires:	ghc-unordered-containers >= 0.1.4.3
BuildRequires:	ghc-unordered-containers-prof >= 0.1.4.3
BuildRequires:	ghc-vector >= 0.6
BuildRequires:	ghc-vector-prof >= 0.6
BuildRequires:	ghc-zlib-enum >= 0.2.1
BuildRequires:	ghc-zlib-enum-prof >= 0.2.1
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_releq	ghc
Requires(post,postun):	/usr/bin/ghc-pkg
Requires:	ghc-attoparsec
Requires:	ghc-attoparsec-enumerator
Requires:	ghc-blaze-builder >= 0.2.1.4
Requires:	ghc-blaze-builder-enumerator
Requires:	ghc-case-insensitive >= 0.3
Requires:	ghc-hashable
Requires:	ghc-HUnit >= 1.2
Requires:	ghc-MonadCatchIO-transformers >= 0.2.1
Requires:	ghc-mtl >= 2.0
Requires:	ghc-random
Requires:	ghc-regex-posix >= 0.95
Requires:	ghc-unix-compat >= 0.2
Requires:	ghc-unordered-containers >= 0.1.4.3
Requires:	ghc-vector >= 0.6
Requires:	ghc-zlib-enum >= 0.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddoc files
%define		_noautocompressdoc	*.haddock

%description
Snap is a simple and fast web development framework and server written
in Haskell. For more information or to download the latest version,
you can visit the Snap project website at http://snapframework.com/.

%package prof
Summary:	Profiling %{pkgname} library for GHC
Summary(pl.UTF-8):	Biblioteka profilująca %{pkgname} dla GHC.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghc-attoparsec-prof
Requires:	ghc-attoparsec-enumerator-prof
Requires:	ghc-blaze-builder-prof
Requires:	ghc-blaze-builder-enumerator-prof
Requires:	ghc-case-insensitive-prof
Requires:	ghc-hashable-prof
Requires:	ghc-HUnit-prof
Requires:	ghc-MonadCatchIO-transformers-prof
Requires:	ghc-mtl-prof
Requires:	ghc-random-prof
Requires:	ghc-regex-posix-prof
Requires:	ghc-unix-compat-prof
Requires:	ghc-unordered-containers-prof
Requires:	ghc-vector-prof
Requires:	ghc-zlib-enum-prof

%description prof
Profiling %{pkgname} library for GHC.  Should be installed when
GHC's profiling subsystem is needed.

%description prof -l pl.UTF-8
Biblioteka profilująca %{pkgname} dla GHC. Powinna być zainstalowana
kiedy potrzebujemy systemu profilującego z GHC.

%prep
%setup -q -n %{pkgname}-%{version}

%build
runhaskell Setup.hs configure -v2 --enable-library-profiling \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version}

runhaskell Setup.hs build
runhaskell Setup.hs haddock --executables

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d

runhaskell Setup.hs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

runhaskell Setup.hs register \
	--gen-pkg-config=$RPM_BUILD_ROOT/%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%ghc_pkg_recache

%postun
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README*
%doc %{name}-%{version}-doc/*
%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*.o
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*.a
%exclude %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*_p.a

%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Http
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Http/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Iteratee
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Iteratee/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Parsing
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Parsing/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Test
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Test/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Types
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Types/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Util
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Util/*.hi

%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*_p.a
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Http/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Iteratee/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Parsing/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Test/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Types/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Util/*.p_hi
