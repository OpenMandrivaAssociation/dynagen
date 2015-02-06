Name:		dynagen
Version:	0.11.0
Release:	2
Group:		Emulators
URL:		http://dyna-gen.sourceforge.net/
Source:		http://downloads.sourceforge.net/dyna-gen/dynagen-%{version}.tar.gz
# Patch for gdynagen, shipped in gdynagen tarball, merged in dynagen svn
# http://gdynagen.sourceforge.net/
Summary:	A configuration tool the dynamips Cisco router simulator
License:	GPL
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root
Suggests:	dynamips >= 0.2.8
Suggests:	xterm
#Requires:	dynamips


%description
Dynagen is a front-end for use with the  Dynamips Cisco router emulator. It
uses an INI-like configuration file to provision Dynamips emulator networks. It
takes care of specifying the right port adapters, generating and matching up
those pesky NIO descriptors, specifying bridges, frame-relay, ATM switches,
etc. It also provides a management CLI for listing devices, suspending and
reloading instances, determining and managing idle-pc values, etc.

%prep
%setup -q
for file in `find . -type f`
do perl -pi -e 'BEGIN {exit unless -T $ARGV[0];}s/\r\n$/\n/;' $file
done

%build

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/{%{_datadir}/%{name},%{_sysconfdir},%{_bindir},%{python_sitelib}}
install configspec *.py *.sh %{buildroot}/%{_datadir}/%{name}
#install dynamips_lib.py %{buildroot}/%{python_sitelib}
install -m755 dynagen %{buildroot}/%{_datadir}/%{name}
install %{name}.ini %{buildroot}/%{_sysconfdir}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}/%{_bindir}/%{name}

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%attr (644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.ini
%{_datadir}/%{name}
#%{python_sitelib}/dynamips_lib.py
%defattr(644,root,root,755)
%doc docs sample_labs README.txt dynagen.ini




%changelog
* Sat Jan 31 2009 Buchan Milne <bgmilne@mandriva.org> 0.11.0-1mdv2009.1
+ Revision: 335804
- New version 0.11.0
-suggest xterm and dynamips (neither are required for use, but in many cases
 would be useful to have)

* Fri Jul 18 2008 Buchan Milne <bgmilne@mandriva.org> 0.10.1-1mdv2009.0
+ Revision: 238174
- update to new version 0.10.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 68199
- New version 0.9.3

* Mon Jun 04 2007 Buchan Milne <bgmilne@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 35017
- New version 0.9.2


* Sun Mar 11 2007 Buchan Milne <bgmilne@mandriva.org> 0.9.0-1mdv2007.1
+ Revision: 141268
- New version 0.9.0
- Import dynagen

* Wed Jan 10 2007 Buchan Milne <bgmilne@mandriva.org> 0.8.3-1mdv
- 0.8.3

* Sat Jan 06 2007 Buchan Milne <bgmilne@mandriva.org> 0.8.2-1mdv
- initial package

