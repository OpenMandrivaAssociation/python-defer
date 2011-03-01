%define module_name defer

Name:		python-%{module_name}
Version:	1.0.2
Release:	%mkrel 1

Summary: 	Small framework for asynchrouns programming in Python
License: 	GPLv2
Group:		Development/Python
URL: 		http://launchpad.net/%{name}/trunk/%{version}/+download/%{module_name}-%{version}.tar.gz
Source0:	%{module_name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch


%description
The defer module provides an easy way to write asynchrouns Python
programms.  It is greatly inspired by Twisted's defer, but comes
without a lot of the dependencies, so It is a stripped down version.

At first defer was part of aptdaemon and moved to a separate project
in August of 2010.


%prep
%setup -q -n %{module_name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --optimize 2 \
			     --root=%{buildroot} \
			     --prefix=%{_prefix}
find %{buildroot} -name '*.egg-info' -print0 | xargs -0 %{__rm} -r


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,0755)
%doc NEWS* README* COPYRIGHT AUTHORS
%{python_sitearch}/defer
