Name:           ksshaskpass
Version:        0.5.1
Release:        4.1%{?dist}
Summary:        A KDE version of ssh-askpass with KWallet support

Group:          Applications/Internet
License:        GPLv2
URL:            http://www.kde-apps.org/content/show.php?content=50971
Source0:        http://www.kde-apps.org/CONTENT/content-files/50971-ksshaskpass-%{version}.tar.gz
Source1:        ksshaskpass-README.Fedora
Patch0:         ksshaskpass-0.5.1-desktopfile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  kdelibs-devel cmake desktop-file-utils
#Requires:       openssh-clients

%description
%{summary}.

Please read %{_docdir}/%{name}-%{version}/README.Fedora for usage
instructions


%prep
%setup -q
%patch0 -p1 -b .desktopfile
cp -p %{SOURCE1} README.Fedora


%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=YES .
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Setup environment variables
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/kde/env/
cat > $RPM_BUILD_ROOT%{_sysconfdir}/kde/env/ksshaskpass.sh << EOF
SSH_ASKPASS=%{_bindir}/ksshaskpass
export SSH_ASKPASS
EOF

desktop-file-install  \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde4 \
    src/%{name}.desktop

# Remove *.la files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README.Fedora
%{_bindir}/ksshaskpass
%config(noreplace) %{_sysconfdir}/kde/env/ksshaskpass.*
%{_mandir}/*/*.gz
%{_datadir}/applications/kde4/*.desktop


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5.1-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.5.1-3
- fix bug 485009
- install the desktop file with desktop-file-install

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.5.1-1
- version 0.5.1

* Tue Jun 24 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.4.1-1
- version 0.4.1

* Sun Mar 30 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.4-2
- buildrequires cmake

* Sun Mar 30 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.4-1
- new version

* Tue Mar 11 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.3-5
- BR kdelibs3-devel instead of kdelibs-devel (#433963)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-4
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.3-3
- fix license tag
- rebuild for BuildID

* Tue Jan 09 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.3-2
- remove useless workaround
- put the environment script in /etc/kde/env

* Sun Jan 07 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.3-1
- initial package
