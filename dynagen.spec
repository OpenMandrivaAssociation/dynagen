Name:		dynagen
Version:	0.9.0
Release:	%mkrel 1
Group:		Emulators
URL:		http://dyna-gen.sourceforge.net/
Source:		http://downloads.sourceforge.net/dyna-gen/dynagen-%{version}.tar.gz
# Patch for gdynagen, shipped in gdynagen tarball, merged in dynagen svn
# http://gdynagen.sourceforge.net/
Summary:	A configuration tool the dynamips Cisco router simulator
License:	GPL
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root
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
install con* validate.py dynamips_lib.py %{buildroot}/%{_datadir}/%{name}
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


