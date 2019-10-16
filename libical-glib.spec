# NOTE: for versions >= 3 see libical.spec
#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	GObject interface of the libical library
Summary(pl.UTF-8):	Interfejs GObject do biblioteki libical
Name:		libical-glib
Version:	1.0.4
Release:	3.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libical-glib/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	403e9b4f86f025024d49bc67d632f7a5
URL:		https://wiki.gnome.org/Projects/libical-glib
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.10
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libical-devel >= 1.0
BuildRequires:	libxml2-devel >= 1:2.7.3
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2.3
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	glib2 >= 1:2.32
Requires:	libical >= 1.0
Requires:	libxml2 >= 1:2.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GObject interface of the libical library.

%description -l pl.UTF-8
Interfejs GObject do biblioteki libical.

%package devel
Summary:	Header files for libical-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libical-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32
Requires:	libical-devel >= 1.0

%description devel
Header files for libical-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libical-glib.

%package static
Summary:	Static libical-glib library
Summary(pl.UTF-8):	Statyczna biblioteka libical-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libical-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka libical-glib.

%package apidocs
Summary:	libical-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libical-glib
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libical-glib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libical-glib.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libical-glib-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libical-glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libical-glib-1.0.so.0
%{_libdir}/girepository-1.0/ICalGLib-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libical-glib-1.0.so
%{_includedir}/libical-glib
%{_datadir}/gir-1.0/ICalGLib-1.0.gir
%{_pkgconfigdir}/libical-glib-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libical-glib-1.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libical-glib
