Name: fiptool
Version: 2.8.0
Release: 1
Source0: https://github.com/ARM-software/arm-trusted-firmware/archive/refs/tags/v%{version}.tar.gz
Summary: Tools for working with FIP (Firmware Image Package) images
URL: https://github.com/ARM-software/arm-trusted-firmware
License: BSD-3-Clause
Group: Development/Tools
BuildRequires: make
BuildRequires: pkgconfig(libcrypto)

%description
Tools for working with FIP (Firmware Image Package) images.

FIPs are commonly used on ARM boards to combine
arm-trusted-firmware and other early bootup code (e.g. u-boot) into
one image that can be flashed to the board.

%prep
%autosetup -p1 -n arm-trusted-firmware-%{version}/tools/fiptool

%build
%make_build HOSTCC="%{__cc} %{optflags}" LDLIBS=-lcrypto

%install
mkdir -p %{buildroot}%{_bindir}
cp -a fiptool %{buildroot}%{_bindir}/

%files
%{_bindir}/fiptool
