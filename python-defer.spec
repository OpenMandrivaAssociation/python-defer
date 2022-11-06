%define module_name defer

Name:		python-%{module_name}
Version:	1.0.4
Release:	1

Summary: 	Small framework for asynchrouns programming in Python
License: 	GPLv2
Group:		Development/Python
URL: 		http://launchpad.net/%{name}/trunk/%{version}/+download/%{module_name}-%{version}.tar.gz
Source0:	https://files.pythonhosted.org/packages/source/d/defer/defer-%{version}.tar.gz

BuildArch:	noarch


%description
The defer module provides an easy way to write asynchrouns Python
programms.  It is greatly inspired by Twisted's defer, but comes
without a lot of the dependencies, so It is a stripped down version.

At first defer was part of aptdaemon and moved to a separate project
in August of 2010.


%prep
%autosetup -p1 -n %{module_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --optimize 2 \
			     --root=%{buildroot} \
			     --prefix=%{_prefix}
find %{buildroot} -name '*.egg-info' -print0 | xargs -0 %{__rm} -r

%files
%defattr(-,root,root,0755)
%doc NEWS* README* COPYRIGHT AUTHORS
%{python_sitelib}/defer
