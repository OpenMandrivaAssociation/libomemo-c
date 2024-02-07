%define major		0
%define libname		%mklibname omemo-c
%define develname	%mklibname omemo-c -d

Name:		libomemo-c
Version:	0.5.0
Release:	1
Summary:	Fork of libsignal-protocol-c adding support for OMEMO XEP-0384 0.5.0+
License:	GPL-3.0-only AND BSD-3-Clause
Group:		System/Libraries
URL:		https://github.com/dino/libomemo-c
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-remove-bundled-version-of-protobuf-c-and-link-to-system-lib.patch
Patch1:		0001-add_-lprotobuf-c_to_pkg-config.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(libprotobuf-c)
# testing dependencies
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(openssl)

%description
This is a fork of libsignal-protocol-c, an implementation of
Signal's ratcheting forward secrecy protocol that works in
synchronous and asynchronous messaging.
The fork adds support for OMEMO as defined in XEP-0384
versions 0.3.0 and later.

#------------------------------------------------

%package -n	%{libname}
Summary:	Fork of libsignal-protocol-c adding support for OMEMO XEP-0384 0.5.0+
Group:		System/Libraries

%description -n	%{libname}
This is a fork of libsignal-protocol-c, an implementation of
Signal's ratcheting forward secrecy protocol that works in
synchronous and asynchronous messaging.
The fork adds support for OMEMO as defined in XEP-0384
versions 0.3.0 and later.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	omemo-c-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libomemo-c.so.%{major}{,.*}

%files -n %{develname}
%doc README.md
%{_includedir}/omemo/
%{_libdir}/libomemo-c.so
%{_libdir}/pkgconfig/libomemo-c.pc
