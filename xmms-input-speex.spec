Summary:	Speex input plugin for XMMS
Summary(pl):	Wtyczka wej¶ciowa formatu speex dla XMMS
Name:		xmms-input-speex
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.speex.org/download/speex-xmms-nightly.tar.gz
URL:		http://www.speex.org/projects.html
BuildRequires:	libogg-devel
BuildRequires:	speex-devel >= 1.0
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugin_dir	%(xmms-config --input-plugin-dir)

%description
Speex input plugin for XMMS.

%description -l pl
Wtyczka wej¶ciowa formatu speex dla XMMS.

%prep
%setup -q -n speex-xmms

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugin_dir}

install libspeex.so $RPM_BUILD_ROOT%{plugin_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{plugin_dir}/*
