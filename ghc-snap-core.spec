#
# Conditional build:
%bcond_without	prof	# profiling library
#
%define		pkgname	snap-core
Summary:	Snap: A Haskell Web Framework (core interfaces and types)
Summary(pl.UTF-8):	Snap - szkielet WWW dla Haskella (główne interfejsy i typy)
Name:		ghc-%{pkgname}
Version:	0.9.5.0
Release:	1
License:	BSD
Group:		Development/Languages
#Source0Download: http://hackage.haskell.org/package/snap-core
Source0:	http://hackage.haskell.org/package/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	e347d1aeee7a2990d211b9d1556c125d
Patch0:		%{name}-deps.patch
URL:		http://hackage.haskell.org/package/snap-core
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-HUnit >= 1.2
BuildRequires:	ghc-HUnit < 2
BuildRequires:	ghc-MonadCatchIO-transformers >= 0.2.1
BuildRequires:	ghc-MonadCatchIO-transformers < 0.4
BuildRequires:	ghc-attoparsec >= 0.10
BuildRequires:	ghc-attoparsec < 0.11
BuildRequires:	ghc-attoparsec-enumerator >= 0.3
BuildRequires:	ghc-attoparsec-enumerator < 0.4
BuildRequires:	ghc-base >= 4
BuildRequires:	ghc-base < 5
BuildRequires:	ghc-blaze-builder >= 0.2.1.4
BuildRequires:	ghc-blaze-builder < 0.4
BuildRequires:	ghc-blaze-builder-enumerator >= 0.2
BuildRequires:	ghc-blaze-builder-enumerator < 0.3
BuildRequires:	ghc-bytestring >= 0.9
BuildRequires:	ghc-bytestring < 0.11
BuildRequires:	ghc-case-insensitive >= 0.3
BuildRequires:	ghc-case-insensitive < 1.2
BuildRequires:	ghc-containers >= 0.3
BuildRequires:	ghc-containers < 1.0
BuildRequires:	ghc-deepseq >= 1.1
BuildRequires:	ghc-deepseq < 1.4
BuildRequires:	ghc-directory >= 1
BuildRequires:	ghc-directory < 2
BuildRequires:	ghc-enumerator >= 0.4.15
BuildRequires:	ghc-enumerator < 0.5
BuildRequires:	ghc-filepath >= 1.1
BuildRequires:	ghc-filepath < 2.0
BuildRequires:	ghc-hashable >= 1.2.1
BuildRequires:	ghc-hashable < 1.3
BuildRequires:	ghc-mtl >= 2.0
BuildRequires:	ghc-mtl < 2.2
BuildRequires:	ghc-random >= 1
BuildRequires:	ghc-random < 2
BuildRequires:	ghc-regex-posix >= 0.95
BuildRequires:	ghc-regex-posix < 1
BuildRequires:	ghc-text >= 0.11
BuildRequires:	ghc-time >= 1.0
BuildRequires:	ghc-time < 1.5
BuildRequires:	ghc-unix >= 2.4
BuildRequires:	ghc-unix < 3.0
BuildRequires:	ghc-unix-compat >= 0.2
BuildRequires:	ghc-unix-compat < 0.5
BuildRequires:	ghc-unordered-containers >= 0.1.4.3
BuildRequires:	ghc-unordered-containers < 0.3
BuildRequires:	ghc-vector >= 0.6
BuildRequires:	ghc-vector < 0.11
BuildRequires:	ghc-zlib-enum >= 0.2.1
BuildRequires:	ghc-zlib-enum < 0.3
%if %{with prof}
BuildRequires:	ghc-prof >= 6.12.3
BuildRequires:	ghc-HUnit-prof >= 1.2
BuildRequires:	ghc-HUnit-prof < 2
BuildRequires:	ghc-MonadCatchIO-transformers-prof >= 0.2.1
BuildRequires:	ghc-MonadCatchIO-transformers-prof < 0.4
BuildRequires:	ghc-attoparsec-prof >= 0.10
BuildRequires:	ghc-attoparsec-prof < 0.11
BuildRequires:	ghc-attoparsec-enumerator-prof >= 0.3
BuildRequires:	ghc-attoparsec-enumerator-prof < 0.4
BuildRequires:	ghc-base-prof >= 4
BuildRequires:	ghc-base-prof < 5
BuildRequires:	ghc-blaze-builder-prof >= 0.2.1.4
BuildRequires:	ghc-blaze-builder-prof < 0.4
BuildRequires:	ghc-blaze-builder-enumerator-prof >= 0.2
BuildRequires:	ghc-blaze-builder-enumerator-prof < 0.3
BuildRequires:	ghc-bytestring-prof >= 0.9
BuildRequires:	ghc-bytestring-prof < 0.11
BuildRequires:	ghc-case-insensitive-prof >= 0.3
BuildRequires:	ghc-case-insensitive-prof < 1.2
BuildRequires:	ghc-containers-prof >= 0.3
BuildRequires:	ghc-containers-prof < 1.0
BuildRequires:	ghc-deepseq-prof >= 1.1
BuildRequires:	ghc-deepseq-prof < 1.4
BuildRequires:	ghc-directory-prof >= 1
BuildRequires:	ghc-directory-prof < 2
BuildRequires:	ghc-enumerator-prof >= 0.4.15
BuildRequires:	ghc-enumerator-prof < 0.5
BuildRequires:	ghc-filepath-prof >= 1.1
BuildRequires:	ghc-filepath-prof < 2.0
BuildRequires:	ghc-hashable-prof >= 1.2.1
BuildRequires:	ghc-hashable-prof < 1.3
BuildRequires:	ghc-mtl-prof >= 2.0
BuildRequires:	ghc-mtl-prof < 2.2
BuildRequires:	ghc-random-prof >= 1
BuildRequires:	ghc-random-prof < 2
BuildRequires:	ghc-regex-posix-prof >= 0.95
BuildRequires:	ghc-regex-posix-prof < 1
BuildRequires:	ghc-text-prof >= 0.11
BuildRequires:	ghc-time-prof >= 1.0
BuildRequires:	ghc-time-prof < 1.5
BuildRequires:	ghc-unix-prof >= 2.4
BuildRequires:	ghc-unix-prof < 3.0
BuildRequires:	ghc-unix-compat-prof >= 0.2
BuildRequires:	ghc-unix-compat-prof < 0.5
BuildRequires:	ghc-unordered-containers-prof >= 0.1.4.3
BuildRequires:	ghc-unordered-containers-prof < 0.3
BuildRequires:	ghc-vector-prof >= 0.6
BuildRequires:	ghc-vector-prof < 0.11
BuildRequires:	ghc-zlib-enum-prof >= 0.2.1
BuildRequires:	ghc-zlib-enum-prof < 0.3
%endif
BuildRequires:	rpmbuild(macros) >= 1.608
Requires(post,postun):	/usr/bin/ghc-pkg
%requires_releq	ghc
Requires:	ghc-HUnit >= 1.2
Requires:	ghc-HUnit < 2
Requires:	ghc-MonadCatchIO-transformers >= 0.2.1
Requires:	ghc-MonadCatchIO-transformers < 0.4
Requires:	ghc-attoparsec >= 0.10
Requires:	ghc-attoparsec < 0.11
Requires:	ghc-attoparsec-enumerator >= 0.3
Requires:	ghc-attoparsec-enumerator < 0.4
Requires:	ghc-base >= 4
Requires:	ghc-base < 5
Requires:	ghc-blaze-builder >= 0.2.1.4
Requires:	ghc-blaze-builder < 0.4
Requires:	ghc-blaze-builder-enumerator >= 0.2
Requires:	ghc-blaze-builder-enumerator < 0.3
Requires:	ghc-bytestring >= 0.9
Requires:	ghc-bytestring < 0.11
Requires:	ghc-case-insensitive >= 0.3
Requires:	ghc-case-insensitive < 1.2
Requires:	ghc-containers >= 0.3
Requires:	ghc-containers < 1.0
Requires:	ghc-deepseq >= 1.1
Requires:	ghc-deepseq < 1.4
Requires:	ghc-directory >= 1
Requires:	ghc-directory < 2
Requires:	ghc-enumerator >= 0.4.15
Requires:	ghc-enumerator < 0.5
Requires:	ghc-filepath >= 1.1
Requires:	ghc-filepath < 2.0
Requires:	ghc-hashable >= 1.2.1
Requires:	ghc-hashable < 1.3
Requires:	ghc-mtl >= 2.0
Requires:	ghc-mtl < 2.2
Requires:	ghc-random >= 1
Requires:	ghc-random < 2
Requires:	ghc-regex-posix >= 0.95
Requires:	ghc-regex-posix < 1
Requires:	ghc-text >= 0.11
Requires:	ghc-time >= 1.0
Requires:	ghc-time < 1.5
Requires:	ghc-unix >= 2.4
Requires:	ghc-unix < 3.0
Requires:	ghc-unix-compat >= 0.2
Requires:	ghc-unix-compat < 0.5
Requires:	ghc-unordered-containers >= 0.1.4.3
Requires:	ghc-unordered-containers < 0.3
Requires:	ghc-vector >= 0.6
Requires:	ghc-vector < 0.11
Requires:	ghc-zlib-enum >= 0.2.1
Requires:	ghc-zlib-enum < 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddock files
%define		_noautocompressdoc	*.haddock

%description
Snap is a simple and fast web development framework and server written
in Haskell. For more information you can visit the Snap project
website at <http://snapframework.com/>.

%description -l pl.UTF-8
Snap to prosty i szybki szkielet programistyczny oraz serwer WWW,
napisany w Haskellu. Więcej informacji można znaleźć na stronie
projektu: <http://snapframework.com/>.

%package prof
Summary:	Profiling %{pkgname} library for GHC
Summary(pl.UTF-8):	Biblioteka profilująca %{pkgname} dla GHC.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghc-HUnit-prof >= 1.2
Requires:	ghc-HUnit-prof < 2
Requires:	ghc-MonadCatchIO-transformers-prof >= 0.2.1
Requires:	ghc-MonadCatchIO-transformers-prof < 0.4
Requires:	ghc-attoparsec-prof >= 0.10
Requires:	ghc-attoparsec-prof < 0.11
Requires:	ghc-attoparsec-enumerator-prof >= 0.3
Requires:	ghc-attoparsec-enumerator-prof < 0.4
Requires:	ghc-base-prof >= 4
Requires:	ghc-base-prof < 5
Requires:	ghc-blaze-builder-prof >= 0.2.1.4
Requires:	ghc-blaze-builder-prof < 0.4
Requires:	ghc-blaze-builder-enumerator-prof >= 0.2
Requires:	ghc-blaze-builder-enumerator-prof < 0.3
Requires:	ghc-bytestring-prof >= 0.9
Requires:	ghc-bytestring-prof < 0.11
Requires:	ghc-case-insensitive-prof >= 0.3
Requires:	ghc-case-insensitive-prof < 1.2
Requires:	ghc-containers-prof >= 0.3
Requires:	ghc-containers-prof < 1.0
Requires:	ghc-deepseq-prof >= 1.1
Requires:	ghc-deepseq-prof < 1.4
Requires:	ghc-directory-prof >= 1
Requires:	ghc-directory-prof < 2
Requires:	ghc-enumerator-prof >= 0.4.15
Requires:	ghc-enumerator-prof < 0.5
Requires:	ghc-filepath-prof >= 1.1
Requires:	ghc-filepath-prof < 2.0
Requires:	ghc-hashable-prof >= 1.2.1
Requires:	ghc-hashable-prof < 1.3
Requires:	ghc-mtl-prof >= 2.0
Requires:	ghc-mtl-prof < 2.2
Requires:	ghc-random-prof >= 1
Requires:	ghc-random-prof < 2
Requires:	ghc-regex-posix-prof >= 0.95
Requires:	ghc-regex-posix-prof < 1
Requires:	ghc-text-prof >= 0.11
Requires:	ghc-time-prof >= 1.0
Requires:	ghc-time-prof < 1.5
Requires:	ghc-unix-prof >= 2.4
Requires:	ghc-unix-prof < 3.0
Requires:	ghc-unix-compat-prof >= 0.2
Requires:	ghc-unix-compat-prof < 0.5
Requires:	ghc-unordered-containers-prof >= 0.1.4.3
Requires:	ghc-unordered-containers-prof < 0.3
Requires:	ghc-vector-prof >= 0.6
Requires:	ghc-vector-prof < 0.11
Requires:	ghc-zlib-enum-prof >= 0.2.1
Requires:	ghc-zlib-enum-prof < 0.3

%description prof
Profiling %{pkgname} library for GHC. Should be installed when GHC's
profiling subsystem is needed.

%description prof -l pl.UTF-8
Biblioteka profilująca %{pkgname} dla GHC. Powinna być zainstalowana
kiedy potrzebujemy systemu profilującego z GHC.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
runhaskell Setup.hs configure -v2 \
	%{?with_prof:--enable-library-profiling} \
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
	--gen-pkg-config=$RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%ghc_pkg_recache

%postun
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README* %{name}-%{version}-doc/*
%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/HSsnap-core-%{version}.o
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSsnap-core-%{version}.a
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
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSsnap-core-%{version}_p.a
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Http/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Iteratee/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Parsing/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Internal/Test/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Types/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Snap/Util/*.p_hi
